# Measurement Protocol: Physical Systems

**Version 1.0 | ARC Scaling Challenge**

---

## Overview

This protocol specifies how to measure the scaling exponent α in classical physical systems exhibiting recursive dynamics, with particular focus on time crystals and similar non-equilibrium systems.

---

## Background

Morrell, Elliott and Grier (2026) report a classical time crystal powered by nonreciprocal wave-mediated interactions (the title of their paper; reference below). Whether the ARC Principle applies to such a system has not been checked, and the programme presents no physical system as a test of it, a result or a priority until that check is made. This protocol records a measurement design only, with no registered prediction. In the programme's reading, which is unchecked and is not the authors', frozen disorder would play the part of structured asymmetry (I) and the nonreciprocal coupling the part of recursive feedback (R).

---

## System Types

### Type A: Acoustic Time Crystals

Following the NYU protocol:
- Foam/plastic beads levitated in sound field
- Size variation creates "frozen disorder"
- Non-reciprocal acoustic coupling

### Type B: Driven Oscillator Networks

- Coupled oscillators with asymmetric coupling
- Parametric driving
- Measure synchronisation vs coupling depth

### Type C: Active Matter Systems

- Self-propelled particles with asymmetric interactions
- Measure collective order vs interaction cycles

---

## Measurement Protocol (Acoustic Time Crystal)

### Requirements

- Acoustic levitation apparatus
- Beads with controlled size distribution (variance = I)
- High-speed camera for position tracking
- Acoustic transducer array

### Step 1: Control Frozen Disorder (I)

Vary the "frozen disorder" by changing bead size distribution:

| Condition | Size Distribution | I Value |
|-----------|-------------------|---------|
| Low I | Uniform sizes | I_low |
| Medium I | Moderate variance | I_med |
| High I | High variance | I_high |

### Step 2: Vary Recursive Depth (R)

R = number of acoustic feedback cycles before measurement

Options:
1. Vary observation time (more cycles = higher R)
2. Vary acoustic coupling strength
3. Vary system size (more beads = more interaction cycles)

### Step 3: Measure Order Parameter

**Temporal Order Parameter (Ψ):**
```
Ψ = |⟨exp(i × 2π × t / T)⟩|

where T = oscillation period
```

High Ψ = strong temporal order (capability U)
Low Ψ = disorder

---

## Analysis

### Fit Power Law

```
Ψ(R) = Ψ_0 × R^α

or equivalently (for error formulation):
Disorder(R) = D_0 × R^(-α)
```

### Extract α

```python
# Log-linear regression
log(Ψ) = log(Ψ_0) + α × log(R)
```

### Control Experiments

**Remove frozen disorder:**
- Use uniform bead sizes
- If the unchecked reading above held: α drops, and no spontaneous order forms

**Remove feedback:**
- Break acoustic coupling
- If the unchecked reading above held: α falls towards zero, with no amplification

---

## Data Format

```csv
I_condition,R_value,psi_order_parameter,n_measurements,std_error
low,1,0.05,100,0.01
low,2,0.08,100,0.01
low,4,0.12,100,0.02
high,1,0.10,100,0.02
high,2,0.25,100,0.03
high,4,0.55,100,0.05
```

---

## Expected results

None is predicted. The theory registration names no physical system, and the check named in the Background comes first.

---

## What a result would show

No condition here refutes a registered proposition. A result from this design would be reported as a dated observation, at its true size.

---

## Safety Notes

- Acoustic levitation uses high-intensity sound
- Use appropriate hearing protection
- Ensure proper ventilation for foam particles

---

## References

- Morrell, M., Elliott, L., & Grier, D.G. (2026). "Nonreciprocal wave-mediated interactions power a classical time crystal." *Physical Review Letters*, 136, 057201. https://doi.org/10.1103/zjzk-t81n
