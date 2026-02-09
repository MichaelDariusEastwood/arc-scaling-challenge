# ARC Principle Analysis Toolkit - R Version
# ==========================================
#
# Statistical analysis tools for testing Eastwood's Principle of Recursive Amplification.
# Core equation: U = I × R^α  where α = 1/(1-β)
#
# Author: Michael Darius Eastwood
# License: MIT
# Version: 1.0.0

library(stats)

#' Fit power law model to data
#'
#' @param R Recursive depth values
#' @param values Capability or error values
#' @param errors If TRUE, fit E = E0 × R^(-α); if FALSE, fit U = U0 × R^α
#' @return List with alpha estimate, CI, and fit statistics
fit_power_law <- function(R, values, errors = TRUE) {
  # Log transform
  log_R <- log(R)
  log_values <- log(values)

  # Remove invalid values
  valid <- is.finite(log_R) & is.finite(log_values)
  log_R <- log_R[valid]
  log_values <- log_values[valid]

  # Linear regression on log-log scale
  fit <- lm(log_values ~ log_R)
  summary_fit <- summary(fit)

  slope <- coef(fit)[2]
  intercept <- coef(fit)[1]
  std_err <- summary_fit$coefficients[2, 2]

  # For error model, α = -slope
  alpha <- ifelse(errors, -slope, slope)

  # 95% CI
  n <- length(log_R)
  t_crit <- qt(0.975, n - 2)
  ci <- c(alpha - t_crit * std_err, alpha + t_crit * std_err)

  # R-squared
  r_squared <- summary_fit$r.squared

  list(
    alpha = as.numeric(alpha),
    alpha_ci = ci,
    alpha_std_err = as.numeric(std_err),
    baseline = exp(as.numeric(intercept)),
    r_squared = r_squared,
    n = n,
    fit = fit
  )
}


#' Estimate β from α
#'
#' @param alpha Scaling exponent
#' @return β (self-referential coupling)
estimate_beta <- function(alpha) {
  if (alpha <= 0) {
    warning("α ≤ 0: β undefined or ≤ 0")
    return(NA)
  }
  1 - 1/alpha
}


#' Compare models using AIC/BIC
#'
#' @param R Recursive depth values
#' @param values Observed values
#' @return Data frame with model comparison
compare_models <- function(R, values) {

  # Power law (via log-linear)
  log_R <- log(R)
  log_values <- log(values)
  fit_power <- lm(log_values ~ log_R)

  # Linear
  fit_linear <- lm(values ~ R)

  # Logarithmic
  fit_log <- lm(values ~ log(R))

  # Quadratic
  fit_quad <- lm(values ~ R + I(R^2))

  # Calculate AIC/BIC
  # Note: For power law, need to adjust for transformation
  n <- length(values)
  rss_power <- sum((values - exp(fitted(fit_power)))^2)
  sigma2_power <- rss_power / n
  loglik_power <- -n/2 * log(2 * pi * sigma2_power) - rss_power / (2 * sigma2_power)
  aic_power <- 4 - 2 * loglik_power  # k=2 params
  bic_power <- 2 * log(n) - 2 * loglik_power

  results <- data.frame(
    model = c("power_law", "linear", "logarithmic", "quadratic"),
    aic = c(aic_power, AIC(fit_linear), AIC(fit_log), AIC(fit_quad)),
    bic = c(bic_power, BIC(fit_linear), BIC(fit_log), BIC(fit_quad))
  )

  # Add delta AIC/BIC
  results$delta_aic <- results$aic - min(results$aic)
  results$delta_bic <- results$bic - min(results$bic)

  # Akaike weights
  results$aic_weight <- exp(-0.5 * results$delta_aic)
  results$aic_weight <- results$aic_weight / sum(results$aic_weight)

  # Sort by AIC
  results <- results[order(results$aic), ]

  results
}


#' Test ARC predictions
#'
#' @param results_seq Results from fit_power_law for sequential condition
#' @param results_par Results from fit_power_law for parallel condition
#' @return List with prediction test results
test_arc_predictions <- function(results_seq, results_par) {

  alpha_seq <- results_seq$alpha
  alpha_par <- results_par$alpha
  ci_seq <- results_seq$alpha_ci
  ci_par <- results_par$alpha_ci

  tests <- list(
    P1_sequential_superlinear = list(
      prediction = "α_sequential > 1",
      result = alpha_seq,
      ci = ci_seq,
      supported = ci_seq[1] > 1
    ),
    P2_parallel_sublinear = list(
      prediction = "α_parallel < 1",
      result = alpha_par,
      ci = ci_par,
      supported = ci_par[2] < 1
    ),
    P3_sequential_greater = list(
      prediction = "α_sequential > α_parallel",
      difference = alpha_seq - alpha_par,
      supported = alpha_seq > alpha_par,
      strongly_supported = ci_seq[1] > ci_par[2]
    )
  )

  n_supported <- sum(sapply(tests, function(x) x$supported))

  tests$summary <- list(
    predictions_supported = n_supported,
    total_predictions = 3,
    arc_supported = n_supported >= 2,
    arc_falsified = n_supported == 0
  )

  tests
}


#' Full analysis pipeline
#'
#' @param data Data frame with condition, R, and value columns
#' @param condition_col Name of condition column
#' @param R_col Name of recursive depth column
#' @param value_col Name of value column
#' @return List with complete analysis results
analyze_arc_data <- function(data, condition_col = "condition",
                             R_col = "R", value_col = "error_rate") {

  results <- list()
  is_error <- grepl("error", value_col, ignore.case = TRUE)

  for (cond in unique(data[[condition_col]])) {
    subset <- data[data[[condition_col]] == cond, ]
    R <- subset[[R_col]]
    values <- subset[[value_col]]

    # Fit power law
    fit_results <- fit_power_law(R, values, errors = is_error)

    # Model comparison
    model_comp <- compare_models(R, values)

    # Estimate beta
    beta <- estimate_beta(fit_results$alpha)

    results[[cond]] <- list(
      fit = fit_results,
      beta = beta,
      model_comparison = model_comp
    )
  }

  # Test predictions if both conditions present
  if ("sequential" %in% names(results) && "parallel" %in% names(results)) {
    results$prediction_tests <- test_arc_predictions(
      results$sequential$fit,
      results$parallel$fit
    )
  }

  results
}


#' Print analysis summary
#'
#' @param results Output from analyze_arc_data
print_arc_summary <- function(results) {
  cat("\n", strrep("=", 60), "\n")
  cat("ARC PRINCIPLE ANALYSIS RESULTS\n")
  cat(strrep("=", 60), "\n")

  for (cond in c("sequential", "parallel")) {
    if (cond %in% names(results)) {
      r <- results[[cond]]
      cat(sprintf("\n%s:\n", toupper(cond)))
      cat(sprintf("  α = %.3f [%.3f, %.3f]\n",
                  r$fit$alpha, r$fit$alpha_ci[1], r$fit$alpha_ci[2]))
      cat(sprintf("  β = %.3f\n", r$beta))
      cat(sprintf("  R² = %.3f\n", r$fit$r_squared))
      cat(sprintf("  Best model (AIC): %s\n", r$model_comparison$model[1]))
    }
  }

  if ("prediction_tests" %in% names(results)) {
    cat("\nPREDICTION TESTS:\n")
    pt <- results$prediction_tests
    for (name in c("P1_sequential_superlinear", "P2_parallel_sublinear", "P3_sequential_greater")) {
      test <- pt[[name]]
      status <- ifelse(test$supported, "✓ SUPPORTED", "✗ NOT SUPPORTED")
      cat(sprintf("  %s: %s\n", test$prediction, status))
    }

    cat(sprintf("\nOVERALL: %d/%d predictions supported\n",
                pt$summary$predictions_supported, pt$summary$total_predictions))

    if (pt$summary$arc_supported) {
      cat("→ ARC Principle SUPPORTED by this data\n")
    } else if (pt$summary$arc_falsified) {
      cat("→ ARC Principle FALSIFIED by this data\n")
    }
  }

  cat(strrep("=", 60), "\n\n")
}


# Example usage:
# data <- read.csv("your_data.csv")
# results <- analyze_arc_data(data)
# print_arc_summary(results)
