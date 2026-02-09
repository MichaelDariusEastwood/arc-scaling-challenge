# ARC Scaling Challenge

**A Global Research Initiative to Test Eastwood's Principle of Recursive Amplification**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://img.shields.io/badge/DOI-10.17605%2FOSF.IO%2F6C5XB-blue)](https://doi.org/10.17605/OSF.IO/6C5XB)

---

## The Challenge

**Can you falsify the ARC Principle?**

The ARC Principle proposes that recursive self-correction on structured asymmetry produces super-linear capability gains:

```
U = I × R^α

where α = 1/(1-β)
```

This repository provides standardised tools for researchers to:
1. **Measure** α in their own systems
2. **Compare** results across domains
3. **Falsify** the framework if it fails

---

## The Predictions

| Prediction | Condition | Falsified If |
|------------|-----------|--------------|
| **P1** | Sequential recursion | α ≤ 1 |
| **P2** | Parallel recursion | α ≥ 1 |
| **P3** | No frozen disorder | α > 1 observed |
| **P4** | Cross-domain | α values diverge significantly |
| **P5** | Theoretical bound | α > 2 consistently observed |

---

## Repository Structure

```
arc-scaling-challenge/
├── README.md                    # You are here
├── CONTRIBUTING.md              # How to submit results
├── LICENSE                      # MIT License
│
├── protocols/                   # Measurement templates
│   ├── ai-language-models.md
│   ├── quantum-systems.md
│   ├── physical-systems.md
│   └── biological-systems.md
│
├── analysis/                    # Statistical analysis code
│   ├── python/
│   │   ├── arc_analysis.py
│   │   ├── power_law_fit.py
│   │   └── requirements.txt
│   └── r/
│       ├── arc_analysis.R
│       └── power_law_fit.R
│
├── tools/                       # Model comparison tools
│   ├── aic_bic_calculator.py
│   ├── alpha_estimator.py
│   └── beta_estimator.py
│
├── figures/                     # Figure generation
│   ├── generate_scaling_plot.py
│   ├── generate_comparison_plot.py
│   └── style_config.py
│
└── submissions/                 # Community results
    ├── TEMPLATE.md
    └── results/
```

---

## Quick Start

### Python

```bash
cd analysis/python
pip install -r requirements.txt
python arc_analysis.py --data your_data.csv
```

### R

```r
source("analysis/r/arc_analysis.R")
results <- fit_arc_model(your_data)
```

---

## How to Participate

### 1. Choose Your Domain

| Domain | Protocol | Contact |
|--------|----------|---------|
| AI/ML | `protocols/ai-language-models.md` | Open |
| Quantum | `protocols/quantum-systems.md` | Open |
| Physics | `protocols/physical-systems.md` | Open |
| Biology | `protocols/biological-systems.md` | Open |

### 2. Run the Measurement

Follow the protocol for your domain. Key requirements:
- Minimum 5 data points across recursive depth R
- Report both sequential AND parallel conditions (if applicable)
- Include raw data and analysis code

### 3. Submit Results

1. Fork this repository
2. Add your results to `submissions/results/`
3. Use the template: `submissions/TEMPLATE.md`
4. Submit a Pull Request

---

## The Ten Falsification Criteria

From Paper III (Eastwood, 2026):

| # | Criterion | How to Test |
|---|-----------|-------------|
| F1 | Sequential yields α > 1 | Measure α in sequential condition |
| F2 | Parallel yields α < 1 | Measure α in parallel condition |
| F3 | Frozen disorder required | Remove asymmetry, check if α drops |
| F4 | α converges across domains | Compare α values between systems |
| F5 | α ≤ 2 (theoretical bound) | Check if α exceeds 2 consistently |
| F6 | β predicts α | Measure β independently, verify α = 1/(1-β) |
| F7 | Crossover depth R* exists | Find R where sequential overtakes parallel |
| F8 | Output-to-input feedback required | Break feedback loop, check α |
| F9 | Time crystal shows α > 1 | Measure scaling in acoustic time crystal |
| F10 | Power-law is correct form | Compare AIC/BIC vs alternative models |

---

## Statistical Standards

All submissions must include:

- [ ] Raw data (CSV or JSON)
- [ ] Sample size (n ≥ 5 data points)
- [ ] α estimate with 95% confidence interval
- [ ] Model comparison (AIC/BIC vs alternatives)
- [ ] Reproducible analysis code

---

## Current Results

| Submitter | Domain | System | α (Sequential) | α (Parallel) | Status |
|-----------|--------|--------|----------------|--------------|--------|
| Eastwood (2026) | AI | DeepSeek R1 | 2.2 [1.5, 3.0] | 0.0 | Paper II |
| — | — | — | — | — | Awaiting submissions |

---

## Citation

If you use these tools, please cite:

```bibtex
@article{eastwood2026arc,
  title={Eastwood's ARC Principle: Cross-Domain Unification of
         Recursive Amplification Across AI, Quantum Computing,
         and Physics},
  author={Eastwood, Michael Darius},
  year={2026},
  publisher={OSF Preprints},
  doi={10.17605/OSF.IO/6C5XB}
}
```

---

## Related Resources

- **Paper I:** [Preliminary Evidence](https://doi.org/10.17605/OSF.IO/6C5XB)
- **Paper II:** [Experimental Validation](https://doi.org/10.17605/OSF.IO/8FJMA)
- **Paper III:** [Cross-Domain Unification](https://github.com/MichaelDariusEastwood/arc-principle-validation)
- **Book:** *Infinite Architects* (Eastwood, 2026)

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

## Contact

- **Author:** Michael Darius Eastwood
- **Email:** michael@michaeldariuseastwood.com
- **ORCID:** 0009-0003-8483-8512

---

*We welcome falsification. Either outcome advances science.*
