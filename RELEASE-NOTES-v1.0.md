# ARC Scaling Challenge — Release v1.0 (first public release)

**Author:** Michael Darius Eastwood (Independent researcher, London) · **Licence:** MIT · **OSF:** 10.17605/OSF.IO/6C5XB

An open toolkit to test — and attempt to falsify — claims about sequential versus parallel recursion scaling (the ARC Principle).

## What's included
- α / β estimators, AIC/BIC model selection, and falsification criteria (`analysis/`, `tools/`).
- Reproducible protocols and synthetic example data (`protocols/`, `examples/`).
- `CITATION.cff` (gives the "Cite this repository" prompt) and `.zenodo.json`.

## Honest claims summary
- **Observed in the programme's own runs:** in Paper II, the error-decay exponent, which describes how error falls as recursive depth grows, stayed near zero for parallel recursion in DeepSeek R1 and GPT-5.4 (0.31 in Gemini 3 Flash and 0.22 in Groq Qwen3), and sequential exceeded parallel (descriptive; no interval). For sequential recursion, the one model whose data scaled smoothly, Gemini 3 Flash, gave about 0.49 by regression and 0.59 by endpoint estimation, and the endpoint estimate's bootstrap interval reaches 2.9: one model's fit, and inconclusive. These are not measurements of the capability exponent of Law I, the ARC Principle, and super-linear scaling has not been observed. No repetition outside the programme is recorded yet.
- **Retracted:** the early single-model estimate of about 2.24 (DeepSeek R1, twelve problems) is retracted. It did not replicate across architectures, and Paper II reads it as an artefact of compressed dynamic range and small sample size. Do not quote it.
- **No priority claimed** on "sequential beats parallel": independently reported by **Sharma & Chopra, *The Sequential Edge*, arXiv:2511.02309 (4 Nov 2025)**. Cite them.
- **Prior art:** the bare geometric exponent α = d/(d+1) has earlier derivations, each its own work in its own domain and terms, West, Brown and Enquist's among them; this programme's contribution is the **Cauchy cross-domain unification**, not the bare exponent.

## How to cite
See `CITATION.cff`. Companion repository: `arc-principle-validation` (papers, results, harness).

## Limitations
Synthetic example data only; real results live in the companion repo and on OSF. The programme does not claim to have solved AI alignment and invites replication or falsification.
