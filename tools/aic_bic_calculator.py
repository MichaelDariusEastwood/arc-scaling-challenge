#!/usr/bin/env python3
"""
AIC/BIC Model Comparison Calculator
===================================

Compare power-law model against alternatives for ARC Principle testing.

Author: Michael Darius Eastwood
License: MIT
"""

import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy import stats
import argparse
import json


def power_law(R, U0, alpha):
    """U = U0 × R^α"""
    return U0 * np.power(R, alpha)


def logarithmic(R, a, b):
    """U = a + b × log(R)"""
    return a + b * np.log(R)


def exponential(R, a, b):
    """U = a × exp(b × R)"""
    return a * np.exp(b * R)


def linear(R, a, b):
    """U = a + b × R"""
    return a + b * R


def quadratic(R, a, b, c):
    """U = a + b×R + c×R²"""
    return a + b * R + c * R**2


def calculate_metrics(R, U, model_func, n_params, model_name):
    """Calculate AIC, BIC, and other fit metrics."""
    n = len(R)

    try:
        # Fit model
        if model_name == 'power_law':
            # Use log-transform for better stability
            log_R = np.log(R)
            log_U = np.log(U)
            slope, intercept, _, _, _ = stats.linregress(log_R, log_U)
            popt = [np.exp(intercept), slope]
            predicted = power_law(R, *popt)
        else:
            popt, _ = curve_fit(model_func, R, U, maxfev=10000)
            predicted = model_func(R, *popt)

        # Residual sum of squares
        rss = np.sum((U - predicted) ** 2)

        # Log-likelihood
        sigma2 = rss / n
        if sigma2 <= 0:
            sigma2 = 1e-10
        log_lik = -n/2 * np.log(2 * np.pi * sigma2) - rss / (2 * sigma2)

        # AIC and BIC
        k = n_params + 1  # +1 for variance parameter
        aic = 2 * k - 2 * log_lik
        bic = k * np.log(n) - 2 * log_lik

        # AICc (corrected for small samples)
        if n - k - 1 > 0:
            aicc = aic + (2 * k * (k + 1)) / (n - k - 1)
        else:
            aicc = np.inf

        # R-squared
        ss_tot = np.sum((U - np.mean(U)) ** 2)
        r_squared = 1 - rss / ss_tot if ss_tot > 0 else 0

        return {
            'model': model_name,
            'n_params': n_params,
            'aic': aic,
            'aicc': aicc,
            'bic': bic,
            'log_likelihood': log_lik,
            'rss': rss,
            'r_squared': r_squared,
            'params': list(popt)
        }

    except Exception as e:
        return {
            'model': model_name,
            'n_params': n_params,
            'aic': np.inf,
            'aicc': np.inf,
            'bic': np.inf,
            'log_likelihood': -np.inf,
            'error': str(e)
        }


def compare_all_models(R, U):
    """Compare all models and rank by AIC/BIC."""

    models = [
        (power_law, 2, 'power_law'),
        (logarithmic, 2, 'logarithmic'),
        (exponential, 2, 'exponential'),
        (linear, 2, 'linear'),
        (quadratic, 3, 'quadratic')
    ]

    results = []
    for func, n_params, name in models:
        metrics = calculate_metrics(R, U, func, n_params, name)
        results.append(metrics)

    # Sort by AIC
    results_sorted = sorted(results, key=lambda x: x['aic'])

    # Calculate delta AIC/BIC
    best_aic = results_sorted[0]['aic']
    best_bic = min(r['bic'] for r in results)

    for r in results_sorted:
        r['delta_aic'] = r['aic'] - best_aic
        r['delta_bic'] = r['bic'] - best_bic

        # Akaike weights
        r['aic_weight'] = np.exp(-0.5 * r['delta_aic'])

    # Normalise weights
    total_weight = sum(r['aic_weight'] for r in results_sorted)
    for r in results_sorted:
        r['aic_weight'] = r['aic_weight'] / total_weight

    return results_sorted


def interpret_results(results):
    """Provide interpretation of model comparison."""

    best = results[0]
    power_law_result = next(r for r in results if r['model'] == 'power_law')

    interpretation = {
        'best_model': best['model'],
        'best_model_aic': best['aic'],
        'power_law_rank': next(i+1 for i, r in enumerate(results)
                               if r['model'] == 'power_law'),
        'power_law_delta_aic': power_law_result['delta_aic'],
        'power_law_weight': power_law_result['aic_weight']
    }

    # Interpretation guidelines (Burnham & Anderson, 2002)
    delta = power_law_result['delta_aic']
    if delta == 0:
        interpretation['support'] = 'STRONG - Power-law is best model'
    elif delta < 2:
        interpretation['support'] = 'SUBSTANTIAL - Power-law has substantial support'
    elif delta < 4:
        interpretation['support'] = 'MODERATE - Power-law has moderate support'
    elif delta < 7:
        interpretation['support'] = 'WEAK - Power-law has weak support'
    else:
        interpretation['support'] = 'NONE - Power-law not supported (Δ AIC > 7)'

    return interpretation


def main():
    parser = argparse.ArgumentParser(
        description='AIC/BIC Model Comparison for ARC Principle'
    )
    parser.add_argument('--data', type=str, required=True,
                        help='Path to CSV file')
    parser.add_argument('--R-col', type=str, default='R',
                        help='Column for recursive depth')
    parser.add_argument('--value-col', type=str, default='error_rate',
                        help='Column for measured values')
    parser.add_argument('--output', type=str, default=None,
                        help='Output JSON file')

    args = parser.parse_args()

    # Load data
    df = pd.read_csv(args.data)
    R = df[args.R_col].values.astype(float)
    U = df[args.value_col].values.astype(float)

    # Compare models
    results = compare_all_models(R, U)
    interpretation = interpret_results(results)

    # Print results
    print("\n" + "="*70)
    print("MODEL COMPARISON RESULTS (AIC/BIC)")
    print("="*70)
    print(f"\n{'Model':<15} {'AIC':>10} {'ΔAIC':>10} {'Weight':>10} {'R²':>10}")
    print("-"*55)

    for r in results:
        print(f"{r['model']:<15} {r['aic']:>10.2f} {r['delta_aic']:>10.2f} "
              f"{r['aic_weight']:>10.3f} {r.get('r_squared', 0):>10.3f}")

    print("\n" + "-"*55)
    print(f"Best model: {interpretation['best_model']}")
    print(f"Power-law support: {interpretation['support']}")
    print(f"Power-law Akaike weight: {interpretation['power_law_weight']:.3f}")
    print("="*70 + "\n")

    # Save results
    if args.output:
        output = {
            'models': results,
            'interpretation': interpretation
        }
        with open(args.output, 'w') as f:
            json.dump(output, f, indent=2, default=str)
        print(f"Results saved to: {args.output}")


if __name__ == '__main__':
    main()
