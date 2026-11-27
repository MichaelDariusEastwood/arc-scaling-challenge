# Measurement Protocol: Quantum Systems

**Version 1.0 | ARC Scaling Challenge**

---

## Overview

This protocol specifies how to measure the scaling exponent α (or Λ) in quantum error correction systems under recursive error correction cycles.

---

## Background

Google Quantum AI report quantum error correction below the surface code threshold (the title of their paper; their preprint was public from 24 August 2024, and the paper was published in Nature on 9 December 2024; reference below). The programme reads the result in its own terms, which are not the authors': the physical error rate as base potential (I), the code distance as recursive depth (R), and the suppression exponent as α. That reading is graded convergent timing beside the author's record of 8 December 2024, never a prediction, and this protocol is a measurement design, not a registered test.

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

## Expected results

None is registered. The theory registration names no quantum system.

---

## What a result would show

No condition here refutes a registered proposition. A result from this design would be reported as a dated observation, at its true size.

---

## Alternative Test: Break Recursive Feedback

If possible, test a condition where error correction cycles do not feed back:
- Run syndrome extraction but ignore results
- Apply random corrections instead of computed corrections

**What the control asks:** whether the suppression exponent falls when the feedback loop is broken. No value is predicted.

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

- Google Quantum AI (2024). "Quantum error correction below the surface code threshold." *Nature*. https://doi.org/10.1038/s41586-024-08449-y
- Fowler, A. G., et al. (2012). "Surface codes: Towards practical large-scale quantum computation." *Physical Review A*. https://doi.org/10.1103/PhysRevA.86.032324
