#!/usr/bin/env python3
"""
ARC Principle Analysis Toolkit
==============================

Statistical analysis tools for testing Eastwood's Principle of Recursive Amplification.

Core equation: U = I × R^α  where α = 1/(1-β)

Author: Michael Darius Eastwood
License: MIT
Version: 1.0.0
"""

import numpy as np
import pandas as pd
from scipy import stats
from scipy.optimize import curve_fit
import argparse
import json
from typing import Tuple, Dict, Optional
import warnings


def power_law(R: np.ndarray, U0: float, alpha: float) -> np.ndarray:
    """
    Power law model: U = U0 × R^α

    For error formulation: E = E0 × R^(-α)
    """
    return U0 * np.power(R, alpha)


def power_law_error(R: np.ndarray, E0: float, alpha: float) -> np.ndarray:
    """
    Error formulation: E = E0 × R^(-α)
    """
    return E0 * np.power(R, -alpha)


def logarithmic_model(R: np.ndarray, a: float, b: float) -> np.ndarray:
    """Alternative model: U = a + b × log(R)"""
    return a + b * np.log(R)


def exponential_model(R: np.ndarray, a: float, b: float) -> np.ndarray:
    """Alternative model: U = a × exp(b × R)"""
    return a * np.exp(b * R)


def linear_model(R: np.ndarray, a: float, b: float) -> np.ndarray:
    """Alternative model: U = a + b × R"""
    return a + b * R


def fit_power_law(R: np.ndarray, U: np.ndarray,
                  errors: bool = False) -> Dict:
    """
    Fit power law to data and return α estimate with confidence interval.

    Parameters
    ----------
    R : array-like
        Recursive depth values
    U : array-like
        Capability/error values
    errors : bool
        If True, fit error model E = E0 × R^(-α)
        If False, fit capability model U = U0 × R^α

    Returns
    -------
    dict with keys:
        - alpha: point estimate
        - alpha_ci: 95% confidence interval (low, high)
        - U0/E0: baseline estimate
        - r_squared: coefficient of determination
        - residuals: fit residuals
    """
    R = np.array(R, dtype=float)
    U = np.array(U, dtype=float)

    # Log-transform for linear regression
    log_R = np.log(R)
    log_U = np.log(U)

    # Remove any invalid values
    valid = np.isfinite(log_R) & np.isfinite(log_U)
    log_R = log_R[valid]
    log_U = log_U[valid]

    # Linear regression on log-log scale
    slope, intercept, r_value, p_value, std_err = stats.linregress(log_R, log_U)

    # For error model, α is negative of slope
    if errors:
        alpha = -slope
    else:
        alpha = slope

    # 95% CI for slope (and thus α)
    n = len(log_R)
    t_crit = stats.t.ppf(0.975, n - 2)
    alpha_ci = (alpha - t_crit * std_err, alpha + t_crit * std_err)

    # Back-transform intercept
    U0 = np.exp(intercept)

    # Calculate R-squared
    r_squared = r_value ** 2

    # Calculate residuals
    if errors:
        predicted = power_law_error(R[valid], U0, alpha)
    else:
        predicted = power_law(R[valid], U0, alpha)
    residuals = U[valid] - predicted

    return {
        'alpha': alpha,
        'alpha_ci': alpha_ci,
        'alpha_std_err': std_err,
        'U0': U0,
        'r_squared': r_squared,
        'p_value': p_value,
        'n': n,
        'residuals': residuals.tolist()
    }


def calculate_aic_bic(R: np.ndarray, U: np.ndarray,
                      model_func, n_params: int) -> Dict:
    """
    Calculate AIC and BIC for a fitted model.

    Parameters
    ----------
    R : array-like
        Recursive depth values
    U : array-like
        Observed values
    model_func : callable
        Fitted model function
    n_params : int
        Number of model parameters

    Returns
    -------
    dict with AIC, BIC, and log-likelihood
    """
    n = len(R)

    try:
        popt, _ = curve_fit(model_func, R, U, maxfev=5000)
        predicted = model_func(R, *popt)

        # Residual sum of squares
        rss = np.sum((U - predicted) ** 2)

        # Log-likelihood (assuming Gaussian errors)
        sigma2 = rss / n
        log_likelihood = -n/2 * np.log(2 * np.pi * sigma2) - rss / (2 * sigma2)

        # AIC and BIC
        aic = 2 * n_params - 2 * log_likelihood
        bic = n_params * np.log(n) - 2 * log_likelihood

        return {
            'aic': aic,
            'bic': bic,
            'log_likelihood': log_likelihood,
            'params': popt.tolist(),
            'rss': rss
        }
    except Exception as e:
        return {
            'aic': np.inf,
            'bic': np.inf,
            'log_likelihood': -np.inf,
            'error': str(e)
        }


def compare_models(R: np.ndarray, U: np.ndarray) -> Dict:
    """
    Compare power-law against alternative models using AIC/BIC.

    Returns dict with model comparison results.
    """
    R = np.array(R, dtype=float)
    U = np.array(U, dtype=float)

    models = {
        'power_law': (power_law, 2),
        'logarithmic': (logarithmic_model, 2),
        'exponential': (exponential_model, 2),
        'linear': (linear_model, 2)
    }

    results = {}
    for name, (func, n_params) in models.items():
        results[name] = calculate_aic_bic(R, U, func, n_params)

    # Find best model by AIC and BIC
    aic_values = {k: v['aic'] for k, v in results.items() if 'aic' in v}
    bic_values = {k: v['bic'] for k, v in results.items() if 'bic' in v}

    best_aic = min(aic_values, key=aic_values.get)
    best_bic = min(bic_values, key=bic_values.get)

    # Calculate delta AIC/BIC from best model
    for name in results:
        if 'aic' in results[name]:
            results[name]['delta_aic'] = results[name]['aic'] - aic_values[best_aic]
            results[name]['delta_bic'] = results[name]['bic'] - bic_values[best_bic]

    return {
        'models': results,
        'best_aic': best_aic,
        'best_bic': best_bic,
        'power_law_supported': best_aic == 'power_law' or best_bic == 'power_law'
    }


def estimate_beta(alpha: float) -> float:
    """
    Estimate β from α using the relationship α = 1/(1-β)

    Parameters
    ----------
    alpha : float
        Measured scaling exponent

    Returns
    -------
    float : estimated β (self-referential coupling)
    """
    if alpha <= 0:
        warnings.warn("α ≤ 0 implies β ≤ 0 (no self-referential coupling)")
        return 1 - 1/alpha if alpha != 0 else 0

    beta = 1 - 1/alpha
    return beta


def test_arc_predictions(results_sequential: Dict,
                         results_parallel: Dict) -> Dict:
    """
    Test ARC Principle predictions against measured results.

    Predictions:
    - P1: Sequential α > 1
    - P2: Parallel α < 1
    - P3: Sequential α > Parallel α
    """
    alpha_seq = results_sequential['alpha']
    alpha_par = results_parallel['alpha']

    ci_seq = results_sequential['alpha_ci']
    ci_par = results_parallel['alpha_ci']

    tests = {
        'P1_sequential_superlinear': {
            'prediction': 'α_sequential > 1',
            'result': alpha_seq,
            'ci': ci_seq,
            'supported': ci_seq[0] > 1,  # Lower CI bound > 1
            'strongly_supported': alpha_seq > 1 and ci_seq[0] > 1
        },
        'P2_parallel_sublinear': {
            'prediction': 'α_parallel < 1',
            'result': alpha_par,
            'ci': ci_par,
            'supported': ci_par[1] < 1,  # Upper CI bound < 1
            'strongly_supported': alpha_par < 1 and ci_par[1] < 1
        },
        'P3_sequential_greater': {
            'prediction': 'α_sequential > α_parallel',
            'difference': alpha_seq - alpha_par,
            'supported': alpha_seq > alpha_par,
            'strongly_supported': ci_seq[0] > ci_par[1]  # CIs don't overlap
        }
    }

    # Overall assessment
    n_supported = sum(1 for t in tests.values() if t['supported'])
    n_strongly = sum(1 for t in tests.values() if t['strongly_supported'])

    tests['summary'] = {
        'predictions_supported': n_supported,
        'predictions_strongly_supported': n_strongly,
        'total_predictions': len(tests) - 1,
        'arc_principle_supported': n_supported >= 2,
        'arc_principle_falsified': n_supported == 0
    }

    return tests


def analyze_data(filepath: str, condition_col: str = 'condition',
                 R_col: str = 'R', value_col: str = 'error_rate') -> Dict:
    """
    Full analysis pipeline for ARC scaling data.

    Parameters
    ----------
    filepath : str
        Path to CSV data file
    condition_col : str
        Column name for condition (sequential/parallel)
    R_col : str
        Column name for recursive depth
    value_col : str
        Column name for measured value

    Returns
    -------
    dict with complete analysis results
    """
    # Load data
    df = pd.read_csv(filepath)

    results = {'data_file': filepath}

    # Analyze each condition
    for condition in df[condition_col].unique():
        subset = df[df[condition_col] == condition]
        R = subset[R_col].values
        values = subset[value_col].values

        # Determine if error or capability formulation
        is_error = 'error' in value_col.lower()

        # Fit power law
        fit_results = fit_power_law(R, values, errors=is_error)

        # Model comparison
        model_comparison = compare_models(R, values)

        # Estimate β
        beta = estimate_beta(fit_results['alpha'])

        results[condition] = {
            'fit': fit_results,
            'beta_estimate': beta,
            'model_comparison': model_comparison,
            'n_datapoints': len(R),
            'R_range': [float(R.min()), float(R.max())]
        }

    # Test predictions if both conditions present
    if 'sequential' in results and 'parallel' in results:
        results['prediction_tests'] = test_arc_predictions(
            results['sequential']['fit'],
            results['parallel']['fit']
        )

    return results


def main():
    parser = argparse.ArgumentParser(
        description='ARC Principle Analysis Toolkit'
    )
    parser.add_argument('--data', type=str, required=True,
                        help='Path to CSV data file')
    parser.add_argument('--condition-col', type=str, default='condition',
                        help='Column name for condition')
    parser.add_argument('--R-col', type=str, default='R',
                        help='Column name for recursive depth')
    parser.add_argument('--value-col', type=str, default='error_rate',
                        help='Column name for measured value')
    parser.add_argument('--output', type=str, default=None,
                        help='Output JSON file path')

    args = parser.parse_args()

    # Run analysis
    results = analyze_data(
        args.data,
        args.condition_col,
        args.R_col,
        args.value_col
    )

    # Print summary
    print("\n" + "="*60)
    print("ARC PRINCIPLE ANALYSIS RESULTS")
    print("="*60)

    for condition in ['sequential', 'parallel']:
        if condition in results:
            r = results[condition]
            print(f"\n{condition.upper()}:")
            print(f"  α = {r['fit']['alpha']:.3f} "
                  f"[{r['fit']['alpha_ci'][0]:.3f}, {r['fit']['alpha_ci'][1]:.3f}]")
            print(f"  β = {r['beta_estimate']:.3f}")
            print(f"  R² = {r['fit']['r_squared']:.3f}")
            print(f"  Best model (AIC): {r['model_comparison']['best_aic']}")

    if 'prediction_tests' in results:
        print("\nPREDICTION TESTS:")
        pt = results['prediction_tests']
        for key, test in pt.items():
            if key != 'summary':
                status = "✓ SUPPORTED" if test['supported'] else "✗ NOT SUPPORTED"
                print(f"  {test['prediction']}: {status}")

        summary = pt['summary']
        print(f"\nOVERALL: {summary['predictions_supported']}/{summary['total_predictions']} "
              f"predictions supported")
        if summary['arc_principle_supported']:
            print("→ ARC Principle SUPPORTED by this data")
        elif summary['arc_principle_falsified']:
            print("→ ARC Principle FALSIFIED by this data")

    print("="*60 + "\n")

    # Save results
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        print(f"Results saved to: {args.output}")

    return results


if __name__ == '__main__':
    main()
