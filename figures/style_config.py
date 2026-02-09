"""
Style Configuration for ARC Principle Figures
==============================================

Nature-style formatting for publication-quality figures.
"""

import matplotlib.pyplot as plt


def set_nature_style():
    """Configure matplotlib for Nature-style figures."""

    plt.rcParams.update({
        # Font
        'font.family': 'sans-serif',
        'font.sans-serif': ['Arial', 'Helvetica', 'DejaVu Sans'],
        'font.size': 10,

        # Axes
        'axes.labelsize': 12,
        'axes.titlesize': 14,
        'axes.linewidth': 1.0,
        'axes.spines.top': False,
        'axes.spines.right': False,

        # Ticks
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'xtick.major.width': 1.0,
        'ytick.major.width': 1.0,
        'xtick.direction': 'out',
        'ytick.direction': 'out',

        # Legend
        'legend.fontsize': 10,
        'legend.frameon': True,
        'legend.framealpha': 0.9,
        'legend.edgecolor': '0.8',

        # Figure
        'figure.figsize': (8, 6),
        'figure.dpi': 150,
        'savefig.dpi': 300,
        'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.1,

        # Lines
        'lines.linewidth': 1.5,
        'lines.markersize': 6,

        # Grid
        'grid.alpha': 0.3,
        'grid.linestyle': '-',
    })


# Color palettes
COLORS = {
    'sequential': '#1f77b4',     # Blue
    'parallel': '#d62728',       # Red
    'reference': '#7f7f7f',      # Gray
    'highlight': '#2ca02c',      # Green
    'accent': '#ff7f0e',         # Orange
}

DOMAIN_COLORS = {
    'ai': '#1f77b4',             # Blue
    'quantum': '#2ca02c',        # Green
    'physics': '#ff7f0e',        # Orange
    'neuroscience': '#9467bd',   # Purple
}

# Marker styles
MARKERS = {
    'sequential': 'o',
    'parallel': 's',
    'ai': 'o',
    'quantum': '^',
    'physics': 's',
    'neuroscience': 'D',
}
