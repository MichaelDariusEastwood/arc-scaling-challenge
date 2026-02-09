#!/usr/bin/env python3
"""
Beta (β) Estimator for ARC Principle
====================================

Estimate self-referential coupling β from observed α.

Relationship: α = 1/(1-β)  →  β = 1 - 1/α

Author: Michael Darius Eastwood
License: MIT
"""

import numpy as np
import argparse


def alpha_to_beta(alpha: float) -> float:
    """
    Convert α to β using α = 1/(1-β)

    Parameters
    ----------
    alpha : float
        Scaling exponent

    Returns
    -------
    float : β (self-referential coupling)
    """
    if alpha <= 0:
        raise ValueError(f"α must be > 0 (got {alpha})")

    beta = 1 - 1/alpha
    return beta


def beta_to_alpha(beta: float) -> float:
    """
    Convert β to α using α = 1/(1-β)

    Parameters
    ----------
    beta : float
        Self-referential coupling (must be < 1)

    Returns
    -------
    float : α (scaling exponent)
    """
    if beta >= 1:
        raise ValueError(f"β must be < 1 (got {beta})")

    alpha = 1 / (1 - beta)
    return alpha


def interpret_beta(beta: float) -> str:
    """Provide interpretation of β value."""

    if beta < 0:
        return "Negative coupling: Each step degrades previous work"
    elif beta == 0:
        return "No coupling: Steps are independent (α = 1, linear)"
    elif beta < 0.5:
        return "Weak coupling: Modest compounding (1 < α < 2)"
    elif beta < 0.75:
        return "Moderate coupling: Strong compounding (2 < α < 4)"
    elif beta < 0.9:
        return "Strong coupling: Very strong compounding (α > 4)"
    else:
        return "Extreme coupling: Approaching singularity (α → ∞)"


def interpret_alpha(alpha: float) -> str:
    """Provide interpretation of α value."""

    if alpha < 0:
        return "Negative scaling: Capability decreases with recursion"
    elif alpha == 0:
        return "No scaling: Recursion provides no benefit"
    elif alpha < 1:
        return "Sub-linear (diminishing returns): Parallel/independent processing"
    elif alpha == 1:
        return "Linear scaling: Each step provides constant benefit"
    elif alpha < 2:
        return "Super-linear (mild): Sequential recursion, moderate β"
    elif alpha < 4:
        return "Super-linear (strong): Sequential recursion, high β"
    else:
        return "Super-linear (extreme): Very strong self-referential coupling"


def main():
    parser = argparse.ArgumentParser(
        description='β Estimator for ARC Principle'
    )
    parser.add_argument('--alpha', type=float, default=None,
                        help='α value to convert to β')
    parser.add_argument('--beta', type=float, default=None,
                        help='β value to convert to α')

    args = parser.parse_args()

    print("\n" + "="*50)
    print("ARC PRINCIPLE: α ↔ β CONVERTER")
    print("Relationship: α = 1/(1-β)")
    print("="*50)

    if args.alpha is not None:
        try:
            beta = alpha_to_beta(args.alpha)
            print(f"\nInput: α = {args.alpha}")
            print(f"Output: β = {beta:.4f}")
            print(f"\nInterpretation:")
            print(f"  α: {interpret_alpha(args.alpha)}")
            print(f"  β: {interpret_beta(beta)}")
        except ValueError as e:
            print(f"\nError: {e}")

    elif args.beta is not None:
        try:
            alpha = beta_to_alpha(args.beta)
            print(f"\nInput: β = {args.beta}")
            print(f"Output: α = {alpha:.4f}")
            print(f"\nInterpretation:")
            print(f"  β: {interpret_beta(args.beta)}")
            print(f"  α: {interpret_alpha(alpha)}")
        except ValueError as e:
            print(f"\nError: {e}")

    else:
        # Print reference table
        print("\nREFERENCE TABLE:")
        print("-"*40)
        print(f"{'β':>8} {'α':>10} {'Interpretation':<25}")
        print("-"*40)

        for beta in [0, 0.25, 0.5, 0.75, 0.9, 0.95]:
            alpha = beta_to_alpha(beta)
            interp = "Linear" if alpha == 1 else f"Super-linear" if alpha > 1 else "Sub-linear"
            print(f"{beta:>8.2f} {alpha:>10.2f} {interp:<25}")

        print("-"*40)
        print("\nUsage:")
        print("  python beta_estimator.py --alpha 2.2")
        print("  python beta_estimator.py --beta 0.5")

    print("="*50 + "\n")


if __name__ == '__main__':
    main()
