#!/usr/bin/env python3
"""
Alpha (α) Estimator for ARC Principle
=====================================

Estimate scaling exponent α from recursive depth vs capability/error data.

Author: Michael Darius Eastwood
License: MIT
"""

import numpy as np
import pandas as pd
from scipy import stats
from scipy.optimize import curve_fit
import argparse
import json


def estimate_alpha(R, values, method='ols', errors=True):
    """
    Estimate α from data using specified method.

    Parameters
    ----------
    R : array-like
        Recursive depth values
    values : array-like
        Capability (if errors=False) or error rate (if errors=True)
    method : str
        'ols' = Ordinary least squares on log-log
        'mle' = Maximum likelihood estimation
        'robust' = Robust regression (Theil-Sen)
    errors : bool
        If True, values are error rates (α should be positive for suppression)
        If False, values are capabilities (α should be positive for amplification)

    Returns
    -------
    dict with alpha estimate and statistics
    """
    R = np.array(R, dtype=float)
    values = np.array(values, dtype=float)

    # Filter valid data
    valid = (R > 0) & (values > 0)
    R = R[valid]
    values = values[valid]

    log_R = np.log(R)
    log_values = np.log(values)

    n = len(R)

    if method == 'ols':
        # Ordinary least squares
        slope, intercept, r_value, p_value, std_err = stats.linregress(log_R, log_values)

        # For errors, α = -slope; for capability, α = slope
        alpha = -slope if errors else slope

        # Confidence interval
        t_crit = stats.t.ppf(0.975, n - 2)
        ci = (alpha - t_crit * std_err, alpha + t_crit * std_err)

        return {
            'alpha': alpha,
            'std_err': std_err,
            'ci_95': ci,
            'r_squared': r_value ** 2,
            'p_value': p_value,
            'intercept': intercept,
            'baseline': np.exp(intercept),
            'n': n,
            'method': 'ols'
        }

    elif method == 'robust':
        # Theil-Sen estimator (robust to outliers)
        result = stats.theilslopes(log_values, log_R)
        slope = result[0]
        intercept = result[1]

        alpha = -slope if errors else slope

        # Bootstrap CI
        n_boot = 1000
        alphas_boot = []
        for _ in range(n_boot):
            idx = np.random.choice(n, n, replace=True)
            res = stats.theilslopes(log_values[idx], log_R[idx])
            alphas_boot.append(-res[0] if errors else res[0])

        ci = (np.percentile(alphas_boot, 2.5), np.percentile(alphas_boot, 97.5))

        return {
            'alpha': alpha,
            'ci_95': ci,
            'intercept': intercept,
            'baseline': np.exp(intercept),
            'n': n,
            'method': 'robust_theil_sen'
        }

    elif method == 'mle':
        # Maximum likelihood with assumed log-normal errors
        def neg_log_likelihood(params):
            alpha, log_baseline, log_sigma = params
            baseline = np.exp(log_baseline)
            sigma = np.exp(log_sigma)

            if errors:
                predicted = baseline * R ** (-alpha)
            else:
                predicted = baseline * R ** alpha

            # Log-normal likelihood
            residuals = np.log(values) - np.log(predicted)
            nll = n/2 * np.log(2 * np.pi) + n * log_sigma + np.sum(residuals**2) / (2 * sigma**2)
            return nll

        from scipy.optimize import minimize

        # Initial guess from OLS
        ols_result = estimate_alpha(R, values, method='ols', errors=errors)
        x0 = [ols_result['alpha'], np.log(ols_result['baseline']), np.log(0.1)]

        result = minimize(neg_log_likelihood, x0, method='Nelder-Mead')
        alpha = result.x[0]
        baseline = np.exp(result.x[1])

        return {
            'alpha': alpha,
            'baseline': baseline,
            'n': n,
            'neg_log_likelihood': result.fun,
            'method': 'mle'
        }

    else:
        raise ValueError(f"Unknown method: {method}")


def estimate_beta_from_alpha(alpha):
    """
    Estimate β (self-referential coupling) from α.

    From α = 1/(1-β), we get β = 1 - 1/α
    """
    if alpha <= 0:
        return None

    beta = 1 - 1/alpha
    return beta


def main():
    parser = argparse.ArgumentParser(
        description='Estimate α for ARC Principle'
    )
    parser.add_argument('--data', type=str, required=True,
                        help='CSV file path')
    parser.add_argument('--R-col', type=str, default='R',
                        help='Column for recursive depth')
    parser.add_argument('--value-col', type=str, default='error_rate',
                        help='Column for values')
    parser.add_argument('--method', type=str, default='ols',
                        choices=['ols', 'robust', 'mle'],
                        help='Estimation method')
    parser.add_argument('--errors', action='store_true',
                        help='Values are error rates (not capabilities)')
    parser.add_argument('--output', type=str, default=None,
                        help='Output JSON file')

    args = parser.parse_args()

    # Load data
    df = pd.read_csv(args.data)
    R = df[args.R_col].values
    values = df[args.value_col].values

    # Estimate alpha
    result = estimate_alpha(R, values, method=args.method, errors=args.errors)

    # Estimate beta
    beta = estimate_beta_from_alpha(result['alpha'])
    result['beta'] = beta

    # Print results
    print("\n" + "="*50)
    print("ALPHA ESTIMATION RESULTS")
    print("="*50)
    print(f"\nMethod: {result['method']}")
    print(f"n = {result['n']}")
    print(f"\nα = {result['alpha']:.4f}")
    if 'ci_95' in result:
        print(f"95% CI: [{result['ci_95'][0]:.4f}, {result['ci_95'][1]:.4f}]")
    if 'std_err' in result:
        print(f"Std Error: {result['std_err']:.4f}")
    if 'r_squared' in result:
        print(f"R² = {result['r_squared']:.4f}")

    print(f"\nβ = {beta:.4f}" if beta else "\nβ = undefined (α ≤ 0)")
    print(f"Baseline = {result['baseline']:.4f}")

    # Interpretation
    print("\nINTERPRETATION:")
    if result['alpha'] > 1:
        print("→ α > 1: SUPER-LINEAR scaling (ARC prediction for sequential)")
    elif result['alpha'] > 0:
        print("→ 0 < α < 1: SUB-LINEAR scaling (ARC prediction for parallel)")
    else:
        print("→ α ≤ 0: No scaling benefit or negative scaling")

    print("="*50 + "\n")

    # Save
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(result, f, indent=2, default=str)
        print(f"Saved to: {args.output}")


if __name__ == '__main__':
    main()
