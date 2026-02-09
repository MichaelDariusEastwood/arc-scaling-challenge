# Measurement Protocol: Biological Systems

**Version 1.0 | ARC Scaling Challenge**

---

## Overview

This protocol specifies how to measure the scaling exponent α in biological neural systems, with focus on recurrent processing and consciousness research.

---

## Background

The COGITATE study (Melloni et al., 2023) found that recurrent processing (feedback loops in visual cortex) is necessary for conscious perception. The ARC Principle predicts:

- **I (Base Potential):** Synaptic architecture / neural diversity
- **R (Recursive Depth):** Recurrent processing cycles
- **α (Scaling):** Should be > 1 for conscious processing

---

## System Types

### Type A: Neural Recordings (Invasive)

- Intracranial EEG
- Multi-electrode arrays
- Single-unit recordings

### Type B: Neuroimaging (Non-Invasive)

- MEG (magnetoencephalography)
- High-density EEG
- fMRI with high temporal resolution

### Type C: Computational Models

- Spiking neural networks
- Recurrent neural networks
- Predictive coding models

---

## Measurement Protocol (Neuroimaging)

### Experimental Design

**Condition 1: Recurrent Processing Allowed**
- Stimulus presented long enough for feedback (>100ms)
- Measure: Conscious perception, neural complexity

**Condition 2: Recurrent Processing Disrupted**
- Backward masking (stimulus <50ms + mask)
- TMS to disrupt feedback
- Measure: Reduced perception, reduced complexity

### Step 1: Define Recursive Depth (R)

Options for operationalising R:

| Approach | R Measure |
|----------|-----------|
| Temporal | Time since stimulus onset (feedback cycles) |
| Anatomical | Number of cortical layers traversed |
| Functional | Connectivity loops detected |
| Oscillatory | Number of alpha/gamma cycles |

### Step 2: Define Capability (U)

Options for operationalising U:

| Measure | Description |
|---------|-------------|
| Perceptual accuracy | Correct identification rate |
| Neural complexity | Perturbational complexity index (PCI) |
| Information integration | Φ (phi) from IIT |
| Decoding accuracy | Classifier performance on neural data |

### Step 3: Vary R Systematically

```
Stimulus durations: 20ms, 50ms, 100ms, 200ms, 500ms
→ Allows 0, 1, 2, 4, 10 feedback cycles (approximately)
```

---

## Analysis

### Fit Power Law

```
U(R) = U_0 × R^α

or for error formulation:
Error(R) = E_0 × R^(-α)
```

### Neural Complexity Analysis

Use Perturbational Complexity Index (PCI):
```
PCI = compressibility of TMS-evoked EEG response
Higher PCI = more integrated information processing
```

### Compare Conditions

| Comparison | Expected (if ARC holds) |
|------------|------------------------|
| Conscious vs unconscious | α_conscious > α_unconscious |
| Feedback intact vs disrupted | α_intact > α_disrupted |
| Awake vs anaesthetised | α_awake > α_anaesthetised |

---

## Data Format

```csv
condition,R_cycles,n_trials,accuracy,complexity_pci,std_error
conscious,1,100,0.55,0.25,0.03
conscious,2,100,0.68,0.35,0.04
conscious,4,100,0.82,0.48,0.04
conscious,10,100,0.95,0.62,0.03
masked,1,100,0.52,0.15,0.02
masked,2,100,0.53,0.16,0.02
masked,4,100,0.54,0.17,0.02
```

---

## Expected Results (If ARC Holds)

| Condition | Expected α |
|-----------|------------|
| Conscious processing | α > 1 |
| Masked/unconscious | α ≈ 0 |
| Recurrence disrupted | α < 1 |

---

## Falsification Conditions

The ARC Principle is **falsified** for biological systems if:

1. Conscious processing yields α ≤ 1
2. Disrupting recurrence does NOT reduce α
3. No difference between conscious and unconscious conditions
4. Capability scales without recurrent feedback

---

## Ethical Requirements

- IRB/Ethics approval required for human studies
- Informed consent
- IACUC approval for animal studies
- Follow Declaration of Helsinki guidelines

---

## Computational Validation

Before running expensive neural experiments, validate with computational models:

```python
# Test with recurrent neural network
model = RecurrentNet(layers=4, recurrence=True)
# vs
model_ff = FeedforwardNet(layers=4, recurrence=False)

# Compare α between models
```

---

## References

- Melloni, L., et al. (2023). "An adversarial collaboration to critically evaluate theories of consciousness." *Nature Human Behaviour*.
- Casali, A. G., et al. (2013). "A theoretically based index of consciousness." *Science Translational Medicine*.
- Tononi, G. (2015). "Integrated information theory." *Scholarpedia*.
