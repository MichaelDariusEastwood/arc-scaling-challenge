# ARC Scaling Challenge

**A Global Research Initiative to Test Eastwood's Principle of Recursive Amplification**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DOI](https://img.shields.io/badge/DOI-10.17605%2FOSF.IO%2F6C5XB-blue)](https://doi.org/10.17605/OSF.IO/6C5XB)

---

## Citation & Prior Art

This repository ships a machine-readable [`CITATION.cff`](CITATION.cff). On GitHub, use the **"Cite this repository"** button in the sidebar (top right of the repository page) to export the citation in APA or BibTeX directly from that file.

**Cite this work as:**

> Eastwood, M.D. (2026). *ARC Scaling Challenge: An Open Falsification Toolkit for Recursive-Amplification Scaling Laws.* OSF. https://doi.org/10.17605/OSF.IO/6C5XB

```bibtex
@misc{eastwood2026challenge,
  author       = {Eastwood, Michael Darius},
  title        = {ARC Scaling Challenge: An Open Falsification Toolkit for
                  Recursive-Amplification Scaling Laws},
  year         = {2026},
  publisher    = {OSF},
  doi          = {10.17605/OSF.IO/6C5XB},
  url          = {https://doi.org/10.17605/OSF.IO/6C5XB}
}
```

### Independent corroboration (sequential > parallel)

The central prediction tested by this toolkit (sequential recursion gives α > 1, parallel gives α < 1) is independently corroborated by:

> Sharma, A. & Chopra, P. (2025). *The Sequential Edge: Inverse-Entropy Voting Beats Parallel Self-Consistency at Matched Compute.* arXiv:2511.02309 (4 November 2025). https://arxiv.org/abs/2511.02309

Their work reports, on independent systems and at matched compute, that sequential reasoning outperforms parallel self-consistency. **No priority is claimed for that result here** — it is cited as corroborating prior/parallel art, and the credit for that specific finding belongs to its authors.

### Acknowledged prior art (the geometric exponent)

The geometric scaling exponent `α = d/(d+1)` is **acknowledged prior art**. It follows the dimensional-scaling tradition of West, Brown & Enquist (allometric quarter-power scaling) and related derivations across physics and biology; this programme does not claim to have originated `d/(d+1)`. The contribution claimed here is the **Cauchy unification** — deriving the family of admissible scaling laws from the Cauchy functional equations rather than the `d/(d+1)` exponent itself.

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
├── requirements.txt             # Python dependencies
├── Makefile                     # Easy setup commands
│
├── protocols/                   # Measurement templates
│   ├── ai-language-models.md
│   ├── quantum-systems.md
│   ├── physical-systems.md
│   └── biological-systems.md
│
├── analysis/                    # Statistical analysis code
│   ├── python/
│   │   ├── __init__.py
│   │   └── arc_analysis.py      # Main analysis toolkit
│   └── r/
│       ├── arc_analysis.R       # R equivalent
│       └── install_packages.R   # R dependency installer
│
├── tools/                       # Standalone tools
│   ├── aic_bic_calculator.py    # Model comparison
│   ├── alpha_estimator.py       # α estimation methods
│   └── beta_estimator.py        # α ↔ β conversion
│
├── examples/                    # Example data and outputs
│   ├── data/
│   │   └── example_ai_sequential_parallel.csv
│   └── expected_output/
│       └── example_results.json
│
├── tests/                       # Unit tests
│   └── test_arc_analysis.py
│
├── figures/                     # Figure generation
│   ├── generate_scaling_plot.py
│   └── style_config.py
│
└── submissions/                 # Community results
    ├── TEMPLATE.md
    └── results/
```

---

## Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/michaeldariuseastwood/arc-scaling-challenge.git
cd arc-scaling-challenge

# Install Python dependencies
pip install -r requirements.txt

# Or use make
make install
```

### Python

```bash
# Run analysis on your data
python analysis/python/arc_analysis.py --data your_data.csv

# Or run on example data
python analysis/python/arc_analysis.py --data examples/data/example_ai_sequential_parallel.csv
```

### R

```r
# Install packages first
source("analysis/r/install_packages.R")

# Run analysis
source("analysis/r/arc_analysis.R")
results <- fit_arc_model(your_data)
```

---

## Quick Verification

Verify the toolkit works correctly:

```bash
# Full verification (Python + tests)
make verify

# Or run individual checks:

# 1. Test imports
python -c "from analysis.python.arc_analysis import fit_power_law; print('OK')"

# 2. Run beta estimator
python tools/beta_estimator.py --alpha 2.2

# 3. Run example analysis
python analysis/python/arc_analysis.py --data examples/data/example_ai_sequential_parallel.csv

# 4. Run unit tests
python -m pytest tests/ -v
```

**Expected output for example data:**
- Sequential α ≈ 2.2 (super-linear)
- Parallel α ≈ 0.08 (near-zero)
- All 3 ARC predictions SUPPORTED

See `examples/expected_output/example_results.json` for full expected results.

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

### Papers

| Paper | Title | DOI | Status |
|-------|-------|-----|--------|
| **I** | Preliminary Evidence | [10.17605/OSF.IO/6C5XB](https://doi.org/10.17605/OSF.IO/6C5XB) | Published |
| **II** | Experimental Validation | [10.17605/OSF.IO/8FJMA](https://doi.org/10.17605/OSF.IO/8FJMA) | Published |
| **III** | Cross-Domain Unification | [10.17605/OSF.IO/HQCGF](https://doi.org/10.17605/OSF.IO/HQCGF) | Published |

### Other Resources

- **GitHub Repository:** [arc-principle-validation](https://github.com/michaeldariuseastwood/arc-principle-validation)
- **Book:** *Infinite Architects: Intelligence, Recursion, and the Creation of Everything* (Eastwood, 2026)

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
