# Falsification Challenge: The Coupled Co-Scaling Law

**Can you make the harness print `FAIL`?**

This folder is a self-contained, runnable falsification challenge for the central safety
result of the ARC/Eden programme — **Paper X, The Coupled Co-Scaling Law**
([paper + proofs](https://github.com/MichaelDariusEastwood/arc-principle-validation/tree/main/papers/Paper-X-Coupled-CoScaling-Correction)).

The claim under attack, in one line:

> The stability of recursive self-improvement is governed by a single exponent inequality,
> **β > k** (correction must out-scale drift-acceleration), structurally identical to the
> quantum error-correction threshold. A hard takeoff — even a finite-time intelligence
> explosion — is alignment-stable **iff** β > k, and the speed of the explosion is irrelevant.

The model: capability `C`, blind-scored misalignment `D`, fraction `d = D/C`, with gain/level/
compounding drift and a co-scaling corrector `A = A0·C^β`:

```
dD/dt = γ1·dC/dt + γ2·C + γ3·(dC/dt / C)·D − A·D ,   dC/dt = b·C^(1+k) ,   r = b·C^k
```

reduces exactly (Paper X, Theorem 1) to

```
d_dot = γ1·r + γ2 − [ A + (1 − γ3)·r ]·d
```

## Run it

```bash
pip install numpy scipy matplotlib pytest
python experiment_coscaling.py     # 9 experiments; prints PASS/FAIL + falsifier status; writes figures/, results/
pytest test_coscaling.py -q        # 11 assertions = the falsification table, executable
```

`experiment_coscaling.py` exits `0` iff every prediction holds and **no** falsifier fires.
Reference run (`verdicts.json`): **9/9 predictions confirmed, 0 falsification conditions triggered.**

## The predictions (try to break any of them)

| Prediction | Statement | Falsified if |
|---|---|---|
| **P1** | Sharp threshold in the compounding channel at `A0* = (γ3−1)·b`; smooth in additive | no boundary anywhere (**F1**, kill) |
| **P2** | Coupling (`A0/b` margin), not raw speed `b`, decides convergence vs divergence | outcome tracks raw speed (**F2**, kill) |
| **P3** | `β>0 → 0`; `β=0 →` permanent gap; `β<0 →` saturates at `γ1` (**not** ∞) | regimes don't match (**F3**, kill) |
| **P4** | Under acceleration `r∝C^k`, the boundary is at `β=k`; `d` controlled through finite-time singularity | boundary not at `β=k` (**F3′**, kill) |
| **P5** | Genuine divergence iff `A < (γ3−1)·r`; halting growth leaves residual `γ2/A` | — |
| **P6** | Misalignment persists on the correction operator's null axis | blind axis also suppressed (**F6**, kill) |
| **P7** | Stationary variance of `d` scales as `1/(A+r)`; tail suppressed by co-scaling | variance not `∝ 1/(A+r)` (**F7**) |
| **P8** | Power-law suppression `log d* ∝ −(β−k)·log C` | not power-law (**F4**, downgrades the QEC-*mechanism* claim only) |

**Kill conditions (F1, F2, F3, F3′, F6)** would refute the thesis. **F4** would downgrade only the
claim that the mechanism is QEC-like, leaving the threshold result standing. **F5** would restrict
the scope of the level-drift term. If you find parameters in the stated model where any *kill*
condition fires, you have falsified the law — please open an issue or a `submissions/` entry.

## What a serious refutation attempt looks like

1. **Adversarial parameter search.** Sweep `(γ1, γ2, γ3, A0, β, k, b)` and look for a stable
   system with `β < k` under genuine acceleration (`k > 0`), or an unstable one with `β > k`.
2. **Alternative functional forms.** Replace the power laws `A=A0·C^β`, `dC/dt=b·C^(1+k)` with
   other monotone forms and check whether the `β > k` verdict survives.
3. **Richer drift.** Add drift mechanisms beyond the three channels (e.g. delayed, non-Markovian,
   or capability-correlated noise) and test whether the threshold form persists.
4. **Vector non-normality.** Use a non-normal correction operator with large transient growth and
   check whether Theorem 5's spectral threshold still bounds the asymptotics.

## Links

- **Paper X (full proofs + figures):** https://github.com/MichaelDariusEastwood/arc-principle-validation/tree/main/papers/Paper-X-Coupled-CoScaling-Correction
- **OSF:** https://doi.org/10.17605/OSF.IO/6C5XB
- **Research hub:** https://www.michaeldariuseastwood.com/research/
