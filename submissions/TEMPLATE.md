# Submission Template

## Submission Information

**Submitter:** [Your Name]
**Affiliation:** [Institution or "Independent"]
**Email:** [Contact email]
**Date:** [YYYY-MM-DD]

---

## Domain

Select one:
- [ ] AI/Machine Learning
- [ ] Quantum Computing
- [ ] Physical Systems
- [ ] Biological/Neural Systems
- [ ] Other: _______________

---

## System Description

**System Name:** [e.g., GPT-4, IBM Eagle, etc.]

**System Type:** [e.g., Language Model, Quantum Processor, Time Crystal, etc.]

**Key Parameters:**
- Parameter 1: value
- Parameter 2: value

---

## Experimental Setup

### Base Potential (I)
Describe the "frozen disorder" or structured asymmetry in your system:


### Recursive Depth (R)
How was R operationalised?
- [ ] Token count
- [ ] Error correction cycles
- [ ] Time steps
- [ ] Other: _______________

**R values tested:** [e.g., 1, 2, 4, 8, 16]

### Conditions

**Sequential condition:**
[Describe how sequential recursion was implemented]

**Parallel condition:**
[Describe how parallel/independent sampling was implemented]

---

## Results

### Raw Data

| Condition | R | n | Success | Failure | Error Rate |
|-----------|---|---|---------|---------|------------|
| sequential | 1 | | | | |
| sequential | 2 | | | | |
| sequential | 4 | | | | |
| parallel | 1 | | | | |
| parallel | 2 | | | | |
| parallel | 4 | | | | |

### Alpha Estimates

| Condition | α | 95% CI | R² | Method |
|-----------|---|--------|----|---------|
| Sequential | | | | |
| Parallel | | | | |

### Model Comparison

| Model | AIC | ΔAIC | Weight |
|-------|-----|------|--------|
| Power-law | | | |
| Logarithmic | | | |
| Exponential | | | |
| Linear | | | |

---

## Prediction Tests

| Prediction | Expected | Observed | Supported? |
|------------|----------|----------|------------|
| P1: α_seq > 1 | Yes | | |
| P2: α_par < 1 | Yes | | |
| P3: α_seq > α_par | Yes | | |

---

## Interpretation

**Does this data support the ARC Principle?**
- [ ] Yes - All predictions supported
- [ ] Partially - Some predictions supported
- [ ] No - Predictions falsified

**Key findings:**


**Limitations:**


---

## Files Included

- [ ] `data.csv` - Raw experimental data
- [ ] `analysis.py` or `analysis.R` - Analysis code
- [ ] `results.json` - Full analysis output
- [ ] `figures/` - Generated figures

---

## Reproducibility Statement

I confirm that:
- [ ] All data is original and accurately reported
- [ ] Analysis code reproduces the reported results
- [ ] Methodology follows the specified protocol

**Signature:** [Your Name]
**Date:** [YYYY-MM-DD]

---

## Additional Notes

[Any additional context, caveats, or observations]
