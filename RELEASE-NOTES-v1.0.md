# ARC Scaling Challenge — Release v1.0 (first public release)

**Author:** Michael Darius Eastwood (Independent researcher, London) · **Licence:** MIT · **OSF:** 10.17605/OSF.IO/6C5XB

An open toolkit to test — and attempt to falsify — claims about sequential versus parallel recursion scaling (the ARC Principle).

## What's included
- α / β estimators, AIC/BIC model selection, and falsification criteria (`analysis/`, `tools/`).
- Reproducible protocols and synthetic example data (`protocols/`, `examples/`).
- `CITATION.cff` (gives the "Cite this repository" prompt) and `.zenodo.json`.

## Honest claims summary
- **Robust, replicated:** the *form* of recursion governs the scaling exponent — parallel recursion is flat (α ≈ 0); sequential recursion is super-linear within an architecture.
- **Corrected:** the early single-model estimate (DeepSeek R1, α ≈ 2.24) **did not replicate** cross-architecturally; the cross-architecture fit is ≈ 0.49. Do not quote 2.24 as an established constant.
- **No priority claimed** on "sequential beats parallel": independently reported by **Sharma & Chopra, *The Sequential Edge*, arXiv:2511.02309 (4 Nov 2025)**. Cite them.
- **Prior art:** the bare geometric exponent α = d/(d+1) was derived independently by several groups (West–Brown–Enquist and others); this programme's contribution is the **Cauchy cross-domain unification**, not the bare exponent.

## How to cite
See `CITATION.cff`. Companion repository: `arc-principle-validation` (papers, results, harness).

## Limitations
Synthetic example data only; real results live in the companion repo and on OSF. The programme does not claim to have solved AI alignment and invites replication or falsification.
