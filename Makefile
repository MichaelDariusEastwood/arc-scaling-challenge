# ARC Scaling Challenge - Makefile
# ================================
#
# Quick commands for setup and verification.
#
# Author: Michael Darius Eastwood
# License: MIT

.PHONY: help install install-r test verify example clean

# Default target
help:
	@echo ""
	@echo "ARC SCALING CHALLENGE - Makefile Commands"
	@echo "=========================================="
	@echo ""
	@echo "Setup:"
	@echo "  make install      Install Python dependencies"
	@echo "  make install-r    Install R dependencies"
	@echo "  make install-all  Install both Python and R dependencies"
	@echo ""
	@echo "Testing:"
	@echo "  make test         Run Python unit tests"
	@echo "  make verify       Verify all code runs correctly"
	@echo "  make example      Run example analysis"
	@echo ""
	@echo "Utilities:"
	@echo "  make clean        Remove generated files"
	@echo ""

# Install Python dependencies
install:
	@echo "Installing Python dependencies..."
	pip install -r requirements.txt
	@echo "Done."

# Install R dependencies
install-r:
	@echo "Installing R dependencies..."
	Rscript analysis/r/install_packages.R
	@echo "Done."

# Install all dependencies
install-all: install install-r

# Run Python unit tests
test:
	@echo "Running unit tests..."
	python -m pytest tests/ -v
	@echo "Done."

# Verify all code runs without errors
verify:
	@echo ""
	@echo "=============================================="
	@echo "VERIFYING ARC SCALING CHALLENGE TOOLKIT"
	@echo "=============================================="
	@echo ""
	@echo "[1/5] Checking Python imports..."
	python -c "from analysis.python.arc_analysis import fit_power_law, compare_models; print('    OK: arc_analysis.py')"
	@echo ""
	@echo "[2/5] Checking tools..."
	python -c "from tools.beta_estimator import alpha_to_beta; print('    OK: beta_estimator.py')"
	python -c "from tools.aic_bic_calculator import compare_all_models; print('    OK: aic_bic_calculator.py')"
	@echo ""
	@echo "[3/5] Testing beta estimator..."
	python tools/beta_estimator.py --alpha 2.2
	@echo ""
	@echo "[4/5] Running example analysis..."
	python analysis/python/arc_analysis.py --data examples/data/example_ai_sequential_parallel.csv
	@echo ""
	@echo "[5/5] Running unit tests..."
	python -m pytest tests/ -v --tb=short
	@echo ""
	@echo "=============================================="
	@echo "ALL VERIFICATIONS PASSED"
	@echo "=============================================="
	@echo ""

# Run example analysis
example:
	@echo "Running example analysis on synthetic data..."
	@echo ""
	python analysis/python/arc_analysis.py \
		--data examples/data/example_ai_sequential_parallel.csv \
		--output examples/expected_output/my_results.json
	@echo ""
	@echo "Results saved to examples/expected_output/my_results.json"

# Clean generated files
clean:
	@echo "Cleaning generated files..."
	rm -rf __pycache__ */__pycache__ */*/__pycache__
	rm -rf .pytest_cache */.pytest_cache
	rm -rf *.pyc */*.pyc */*/*.pyc
	rm -rf .coverage htmlcov
	rm -f examples/expected_output/my_results.json
	@echo "Done."
