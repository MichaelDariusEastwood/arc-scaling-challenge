#!/usr/bin/env python3
"""
Unit Tests for ARC Principle Analysis Toolkit
=============================================

Run with: pytest tests/ -v
Or:       python -m pytest tests/ -v

Author: Michael Darius Eastwood
License: MIT
"""

import pytest
import numpy as np
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analysis.python.arc_analysis import (
    power_law,
    power_law_error,
    fit_power_law,
    compare_models,
    estimate_beta,
    check_arc_predictions
)

from tools.beta_estimator import alpha_to_beta, beta_to_alpha


class TestPowerLawFunctions:
    """Test power law model functions."""

    def test_power_law_basic(self):
        """Test basic power law calculation."""
        R = np.array([1, 2, 4, 8])
        result = power_law(R, U0=1.0, alpha=2.0)
        expected = np.array([1, 4, 16, 64])
        np.testing.assert_array_almost_equal(result, expected)

    def test_power_law_error_basic(self):
        """Test error formulation (inverse power law)."""
        R = np.array([1, 2, 4, 8])
        result = power_law_error(R, E0=1.0, alpha=2.0)
        expected = np.array([1, 0.25, 0.0625, 0.015625])
        np.testing.assert_array_almost_equal(result, expected)

    def test_power_law_alpha_one(self):
        """Test linear case (alpha = 1)."""
        R = np.array([1, 2, 3, 4])
        result = power_law(R, U0=2.0, alpha=1.0)
        expected = np.array([2, 4, 6, 8])
        np.testing.assert_array_almost_equal(result, expected)


class TestFitPowerLaw:
    """Test power law fitting function."""

    def test_fit_perfect_data(self):
        """Test fitting on perfect power law data."""
        R = np.array([1, 2, 4, 8, 16])
        # Create perfect alpha=2 data
        U = power_law(R, U0=1.0, alpha=2.0)

        result = fit_power_law(R, U, errors=False)

        assert abs(result['alpha'] - 2.0) < 0.01
        assert result['r_squared'] > 0.99
        assert result['n'] == 5

    def test_fit_returns_confidence_interval(self):
        """Test that CI is returned."""
        R = np.array([1, 2, 4, 8, 16])
        U = power_law(R, U0=1.0, alpha=2.0)

        result = fit_power_law(R, U, errors=False)

        assert 'alpha_ci' in result
        assert len(result['alpha_ci']) == 2
        assert result['alpha_ci'][0] <= result['alpha']
        assert result['alpha_ci'][1] >= result['alpha']

    def test_fit_error_formulation(self):
        """Test error formulation fitting."""
        R = np.array([1, 2, 4, 8, 16])
        # Create error data: E = E0 * R^(-alpha)
        E = power_law_error(R, E0=0.5, alpha=2.0)

        result = fit_power_law(R, E, errors=True)

        # Alpha should be positive even though slope is negative
        assert result['alpha'] > 0
        assert abs(result['alpha'] - 2.0) < 0.1

    def test_fit_noisy_data(self):
        """Test fitting with noise."""
        np.random.seed(42)
        R = np.array([1, 2, 4, 8, 16])
        U = power_law(R, U0=1.0, alpha=2.0)
        U_noisy = U * (1 + np.random.normal(0, 0.05, len(U)))

        result = fit_power_law(R, U_noisy, errors=False)

        # Should still get approximately alpha=2
        assert 1.5 < result['alpha'] < 2.5


class TestModelComparison:
    """Test AIC/BIC model comparison."""

    def test_compare_identifies_power_law(self):
        """Test that power law is identified as best for power law data."""
        R = np.array([1, 2, 4, 8, 16])
        U = power_law(R, U0=1.0, alpha=1.5)

        result = compare_models(R, U)

        assert 'models' in result
        assert 'best_aic' in result
        # Power law should be best or close to best
        assert result['power_law_supported'] or result['best_aic'] == 'power_law'

    def test_compare_returns_all_models(self):
        """Test that all model results are returned."""
        R = np.array([1, 2, 4, 8, 16])
        U = power_law(R, U0=1.0, alpha=2.0)

        result = compare_models(R, U)

        assert 'power_law' in result['models']
        assert 'linear' in result['models']
        assert 'logarithmic' in result['models']


class TestBetaEstimation:
    """Test alpha <-> beta conversion."""

    def test_alpha_to_beta_superlinear(self):
        """Test beta for superlinear alpha."""
        # alpha = 2 -> beta = 0.5
        beta = alpha_to_beta(2.0)
        assert abs(beta - 0.5) < 0.001

    def test_alpha_to_beta_linear(self):
        """Test beta for linear scaling."""
        # alpha = 1 -> beta = 0
        beta = alpha_to_beta(1.0)
        assert abs(beta - 0.0) < 0.001

    def test_beta_to_alpha_round_trip(self):
        """Test round-trip conversion."""
        original_alpha = 2.5
        beta = alpha_to_beta(original_alpha)
        recovered_alpha = beta_to_alpha(beta)
        assert abs(recovered_alpha - original_alpha) < 0.001

    def test_beta_to_alpha_basic(self):
        """Test basic beta to alpha."""
        # beta = 0.5 -> alpha = 2
        alpha = beta_to_alpha(0.5)
        assert abs(alpha - 2.0) < 0.001

    def test_estimate_beta_function(self):
        """Test the estimate_beta wrapper."""
        beta = estimate_beta(2.2)
        expected = 1 - 1/2.2
        assert abs(beta - expected) < 0.001


class TestARCPredictions:
    """Test ARC prediction testing."""

    def test_predictions_all_supported(self):
        """Test when all predictions are supported."""
        # Sequential: alpha > 1
        sequential = {
            'alpha': 2.2,
            'alpha_ci': (1.8, 2.6)
        }
        # Parallel: alpha < 1
        parallel = {
            'alpha': 0.1,
            'alpha_ci': (-0.1, 0.3)
        }

        result = check_arc_predictions(sequential, parallel)

        assert result['P1_sequential_superlinear']['supported']
        assert result['P2_parallel_sublinear']['supported']
        assert result['P3_sequential_greater']['supported']
        assert result['summary']['arc_principle_supported']
        assert not result['summary']['arc_principle_falsified']

    def test_predictions_falsified(self):
        """Test when predictions are falsified."""
        # If sequential alpha < 1, P1 fails
        sequential = {
            'alpha': 0.5,
            'alpha_ci': (0.3, 0.7)
        }
        parallel = {
            'alpha': 0.8,
            'alpha_ci': (0.6, 1.0)
        }

        result = check_arc_predictions(sequential, parallel)

        # P1 should not be supported (sequential not superlinear)
        assert not result['P1_sequential_superlinear']['strongly_supported']

    def test_strong_support_requires_ci_separation(self):
        """Test that strong support requires CI separation."""
        # Sequential CI must be entirely > 1 for strong support
        sequential = {
            'alpha': 1.5,
            'alpha_ci': (0.9, 2.1)  # CI includes 1
        }
        parallel = {
            'alpha': 0.5,
            'alpha_ci': (0.3, 0.7)
        }

        result = check_arc_predictions(sequential, parallel)

        # Not strongly supported because CI includes 1
        assert not result['P1_sequential_superlinear']['strongly_supported']


class TestEdgeCases:
    """Test edge cases and error handling."""

    def test_small_sample_size(self):
        """Test with minimum sample size."""
        R = np.array([1, 2, 4])
        U = np.array([1, 4, 16])

        result = fit_power_law(R, U, errors=False)

        assert 'alpha' in result
        assert result['n'] == 3

    def test_negative_alpha_handling(self):
        """Test beta estimation with edge case alpha."""
        with pytest.raises(ValueError):
            alpha_to_beta(0)  # Should raise error for alpha=0

    def test_beta_near_one(self):
        """Test alpha calculation for beta near 1."""
        with pytest.raises(ValueError):
            beta_to_alpha(1.0)  # Would give infinite alpha


class TestIntegration:
    """Integration tests using example data."""

    @pytest.fixture
    def example_data(self):
        """Load example data."""
        import pandas as pd
        data_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'examples', 'data', 'example_ai_sequential_parallel.csv'
        )
        if os.path.exists(data_path):
            return pd.read_csv(data_path)
        return None

    def test_example_data_exists(self, example_data):
        """Test that example data file exists."""
        assert example_data is not None, "Example data file not found"

    def test_example_sequential_vs_parallel(self, example_data):
        """Test that sequential α > parallel α (key ARC prediction)."""
        if example_data is None:
            pytest.skip("Example data not available")

        # Get sequential data
        seq_data = example_data[example_data['condition'] == 'sequential']
        seq_R = seq_data['R'].values
        seq_error = seq_data['error_rate'].values
        seq_result = fit_power_law(seq_R, seq_error, errors=True)

        # Get parallel data
        par_data = example_data[example_data['condition'] == 'parallel']
        par_R = par_data['R'].values
        par_error = par_data['error_rate'].values
        par_result = fit_power_law(par_R, par_error, errors=True)

        # KEY ARC PREDICTION: Sequential α > Parallel α
        assert seq_result['alpha'] > par_result['alpha'], \
            f"Expected sequential α ({seq_result['alpha']}) > parallel α ({par_result['alpha']})"

    def test_example_parallel_sublinear(self, example_data):
        """Test that parallel data shows sublinear/minimal scaling."""
        if example_data is None:
            pytest.skip("Example data not available")

        par_data = example_data[example_data['condition'] == 'parallel']
        R = par_data['R'].values
        error_rate = par_data['error_rate'].values

        result = fit_power_law(R, error_rate, errors=True)

        # Parallel should show alpha < 1 (minimal improvement)
        assert result['alpha'] < 1.0, f"Expected alpha < 1, got {result['alpha']}"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
