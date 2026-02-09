# ARC Principle Python Analysis Module
# =====================================
#
# Usage:
#   from analysis.python.arc_analysis import fit_power_law, compare_models, analyze_data
#
# Or run directly:
#   python -m analysis.python.arc_analysis --data data.csv
#
# Author: Michael Darius Eastwood
# License: MIT

from .arc_analysis import (
    power_law,
    power_law_error,
    fit_power_law,
    compare_models,
    calculate_aic_bic,
    estimate_beta,
    check_arc_predictions,
    analyze_data
)

__all__ = [
    'power_law',
    'power_law_error',
    'fit_power_law',
    'compare_models',
    'calculate_aic_bic',
    'estimate_beta',
    'check_arc_predictions',
    'analyze_data'
]

__version__ = "1.0.0"
