#!/usr/bin/env python3
"""
Generate Scaling Plot for ARC Principle
=======================================

Create publication-quality figures showing power-law scaling.

Author: Michael Darius Eastwood
License: MIT
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import argparse
from style_config import set_nature_style


def generate_scaling_plot(data_file, output_file, condition_col='condition',
                          R_col='R', value_col='error_rate',
                          title='ARC Principle: Scaling Analysis'):
    """Generate log-log scaling plot."""

    set_nature_style()

    df = pd.read_csv(data_file)

    fig, ax = plt.subplots(figsize=(8, 6))

    colors = {'sequential': '#1f77b4', 'parallel': '#d62728'}
    markers = {'sequential': 'o', 'parallel': 's'}

    for condition in df[condition_col].unique():
        subset = df[df[condition_col] == condition]
        R = subset[R_col].values
        values = subset[value_col].values

        # Plot data points
        ax.loglog(R, values,
                  marker=markers.get(condition, 'o'),
                  color=colors.get(condition, '#333333'),
                  label=condition.capitalize(),
                  markersize=8,
                  linewidth=0,
                  markeredgecolor='white',
                  markeredgewidth=1)

        # Fit line
        log_R = np.log(R)
        log_values = np.log(values)
        slope, intercept = np.polyfit(log_R, log_values, 1)
        alpha = -slope  # For error formulation

        R_fit = np.logspace(np.log10(R.min()), np.log10(R.max()), 100)
        values_fit = np.exp(intercept) * R_fit ** slope

        ax.loglog(R_fit, values_fit,
                  color=colors.get(condition, '#333333'),
                  linestyle='--',
                  alpha=0.7,
                  linewidth=2)

        # Annotate alpha
        mid_idx = len(R_fit) // 2
        ax.annotate(f'α = {alpha:.2f}',
                    xy=(R_fit[mid_idx], values_fit[mid_idx]),
                    xytext=(10, 10),
                    textcoords='offset points',
                    fontsize=11,
                    color=colors.get(condition, '#333333'))

    ax.set_xlabel('Recursive Depth (R)', fontsize=12)
    ax.set_ylabel('Error Rate', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')

    ax.legend(loc='upper right', frameon=True, fontsize=10)
    ax.grid(True, which='both', alpha=0.3, linestyle='-')

    # Reference line at α = 1
    R_ref = np.logspace(np.log10(df[R_col].min()), np.log10(df[R_col].max()), 100)
    ax.loglog(R_ref, 0.5 * R_ref ** (-1), 'k:', alpha=0.5, label='α = 1 (linear)')

    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Saved: {output_file}")

    return fig


def main():
    parser = argparse.ArgumentParser(description='Generate ARC scaling plot')
    parser.add_argument('--data', type=str, required=True, help='CSV data file')
    parser.add_argument('--output', type=str, default='scaling_plot.png',
                        help='Output file path')
    parser.add_argument('--title', type=str, default='ARC Principle: Scaling Analysis',
                        help='Plot title')

    args = parser.parse_args()
    generate_scaling_plot(args.data, args.output, title=args.title)


if __name__ == '__main__':
    main()
