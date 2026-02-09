#!/usr/bin/env Rscript
#' Install Required Packages for ARC Principle Analysis
#' ====================================================
#'
#' Run this script to install all required R packages:
#'   Rscript install_packages.R
#'
#' Author: Michael Darius Eastwood
#' License: MIT

# Required packages
required_packages <- c(
  # Core statistical analysis
  "stats",        # Base R (usually pre-installed)

  # Robust regression
  "MASS",         # Robust linear models, Theil-Sen
  "robustbase",   # Additional robust methods

  # Confidence intervals
  "boot",         # Bootstrap confidence intervals

  # Data manipulation
  "jsonlite",     # JSON output

  # Optional but recommended
  "ggplot2",      # Publication-quality figures
  "dplyr",        # Data manipulation
  "tidyr",        # Data tidying
  "readr"         # Fast CSV reading
)

# Function to install missing packages
install_if_missing <- function(packages) {
  new_packages <- packages[!(packages %in% installed.packages()[, "Package"])]

  if (length(new_packages) > 0) {
    cat("Installing missing packages:\n")
    cat(paste(" -", new_packages, collapse = "\n"), "\n\n")
    install.packages(new_packages, repos = "https://cloud.r-project.org/")
  } else {
    cat("All required packages are already installed.\n")
  }

  # Verify installation
  cat("\nVerifying installations:\n")
  for (pkg in packages) {
    if (pkg %in% installed.packages()[, "Package"]) {
      version <- packageVersion(pkg)
      cat(sprintf("  [OK] %s (%s)\n", pkg, version))
    } else {
      cat(sprintf("  [FAIL] %s - installation failed\n", pkg))
    }
  }
}

# Run installation
cat("=" |> rep(60) |> paste(collapse = ""), "\n")
cat("ARC PRINCIPLE: R Package Installer\n")
cat("=" |> rep(60) |> paste(collapse = ""), "\n\n")

install_if_missing(required_packages)

cat("\n")
cat("=" |> rep(60) |> paste(collapse = ""), "\n")
cat("Installation complete.\n")
cat("You can now run: Rscript arc_analysis.R\n")
cat("=" |> rep(60) |> paste(collapse = ""), "\n")
