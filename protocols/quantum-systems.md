# Measurement Protocol: Quantum Systems

**Version 1.0 | ARC Scaling Challenge**

---

## Overview

This protocol specifies how to measure the scaling exponent α (or Λ) in quantum error correction systems under recursive error correction cycles.

---

## Background

Google's Willow processor demonstrated exponential error suppression with increasing code distance, achieving Λ ≈ 2.14. The ARC Principle predicts this is an instance of recursive amplification where:

- **I (Base Potential):** Qubit quality / physical error rate
- **R (Recursive Depth):** Error correction cycles / code distance
- **α (Scaling):** Error suppression exponent

---

## Requirements

### Hardware Requirements
- Quantum processor with error correction capability
- Surface code or similar error-correcting code implementation
- Minimum 3 different code distances testable

### Measurement Requirements
- Logical error rate at each code distance
- Physical qubit error rates
- Minimum 1000 shots per measurement

---

## Experimental Design

### Variable: Code Distance (d)

The code distance determines how many physical errors can be corrected. Higher d = more recursive error correction.

```
Measure logical error rate ε_L at:
d = 3, 5, 7, 9, 11 (or available distances)
```

### Fixed Parameters

- Same physical qubit quality across measurements
- Same gate fidelities
- Same measurement protocol

---

## Measurement Procedure

### Step 1: Characterise Physical Error Rate

```
Measure physical error rate ε_phys:
- Single-qubit gate errors
- Two-qubit gate errors
- Measurement errors
- Idle errors
```

### Step 2: Prepare Logical Qubit

```
For each code distance d:
1. Initialise logical |0⟩ state
2. Apply d rounds of error correction
3. Measure logical state
4. Record success/failure
5. Repeat N ≥ 1000 times
```

### Step 3: Calculate Logical Error Rate

```
ε_L(d) = (failed measurements) / (total measurements)
```

---

## Analysis

### Fit Exponential Suppression

The standard model for surface codes:

```
ε_L = A × (ε_phys / ε_threshold)^((d+1)/2)
```

Equivalently, in ARC notation:

```
E(R) = E_0 × R^(-α)

where R ~ (d+1)/2 (effective recursive depth)
```

### Extract Λ (Lambda)

Google's notation:
```
ε_L(d) / ε_L(d-2) = 1/Λ

Λ = error suppression factor per code distance increment
```

Relationship to α:
```
Λ ≈ 2^α (approximately)
```

---

## Data Format

Save results as CSV:

```csv
code_distance,n_shots,n_success,n_failure,logical_error_rate,physical_error_rate
3,1000,850,150,0.150,0.005
5,1000,920,80,0.080,0.005
7,1000,965,35,0.035,0.005
9,1000,988,12,0.012,0.005
```

---

## Expected Results (If ARC Holds)

| Metric | Expected Value |
|--------|----------------|
| Λ | > 2 (super-linear suppression) |
| α equivalent | > 1 |
| Error suppression | Exponential with code distance |

---

## Falsification Conditions

The ARC Principle is **falsified** for quantum systems if:

1. Λ < 1 consistently (errors grow with code distance)
2. Λ = 1 exactly (no suppression benefit)
3. Error suppression is sub-exponential

---

## Alternative Test: Break Recursive Feedback

If possible, test a condition where error correction cycles do not feed back:
- Run syndrome extraction but ignore results
- Apply random corrections instead of computed corrections

**Prediction:** α drops to ≤ 1 when feedback loop is broken

---

## Submission Checklist

- [ ] Raw measurement data (CSV)
- [ ] Hardware specification (processor, qubit count, topology)
- [ ] Physical error rates
- [ ] Λ estimate with uncertainty
- [ ] α estimate with 95% CI
- [ ] Code distance range tested
- [ ] Analysis code (reproducible)

---

## References

- Google Quantum AI (2024). "Quantum error correction below the surface code threshold." *Nature*.
- Fowler, A. G., et al. (2012). "Surface codes: Towards practical large-scale quantum computation." *Physical Review A*.
