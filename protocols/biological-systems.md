# Measurement Protocol: Biological Systems

**Version 1.0 | ARC Scaling Challenge**

---

## Overview

This protocol specifies how to measure the scaling exponent α in biological neural systems, with focus on recurrent processing and consciousness research.

---

## Background

This design draws on research into recurrent processing and conscious perception (references below) and attributes no finding to it. The theory registration's proposition on consciousness is conditional and is not registered, because the estimator it needs is contested in its own field. So this protocol is a measurement design, not a registered test, and no result from it would decide a registered proposition. In the programme's reading, which is unchecked: synaptic architecture as base potential (I), recurrent processing cycles as recursive depth (R), and the fitted exponent as α.

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

| Comparison | Contrast this design reads (no value predicted) |
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

## Expected results

None is registered (see the Background).

---

## What a result would show

No condition here refutes a registered proposition. A result from this design would be reported as a dated observation, at its true size.

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

- Cogitate Consortium, Ferrante, O., Gorska-Klimowska, U., et al. (2023). "An adversarial collaboration to critically evaluate theories of consciousness." *bioRxiv*. https://doi.org/10.1101/2023.06.23.546249. Published as "Adversarial testing of global neuronal workspace and integrated information theories of consciousness." *Nature* (2025). https://doi.org/10.1038/s41586-025-08888-1
- Casali, A. G., et al. (2013). "A theoretically based index of consciousness." *Science Translational Medicine*.
- Tononi, G. (2015). "Integrated information theory." *Scholarpedia*.
