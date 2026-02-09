# Contributing to the ARC Scaling Challenge

Thank you for your interest in testing Eastwood's ARC Principle!

## How to Contribute

### 1. Test the Principle

Choose a domain and follow the appropriate protocol:
- `protocols/ai-language-models.md`
- `protocols/quantum-systems.md`
- `protocols/physical-systems.md`
- `protocols/biological-systems.md`

### 2. Prepare Your Submission

1. Fork this repository
2. Create a new folder: `submissions/results/[your-name]-[domain]-[date]/`
3. Include:
   - `data.csv` - Raw data
   - `analysis.py` or `analysis.R` - Your analysis code
   - `results.json` - Full results
   - `SUBMISSION.md` - Completed template from `submissions/TEMPLATE.md`
   - `figures/` - Any generated figures

### 3. Submit

1. Create a Pull Request
2. Title: `[Domain] Submission: [Brief Description]`
3. Include summary in PR description

---

## Data Standards

### CSV Format

```csv
condition,R,n_trials,n_correct,n_incorrect,error_rate
sequential,1,100,55,45,0.45
sequential,2,100,70,30,0.30
...
```

### Required Columns

| Column | Description | Type |
|--------|-------------|------|
| condition | "sequential" or "parallel" | string |
| R | Recursive depth | numeric |
| n_trials | Total trials | integer |
| error_rate | Failures / total | float [0,1] |

---

## Analysis Requirements

All submissions must include:

- [ ] α estimate with 95% confidence interval
- [ ] R² value for power-law fit
- [ ] AIC/BIC model comparison
- [ ] Sample size (n ≥ 5 R values recommended)
- [ ] Reproducible code

---

## Code of Conduct

1. **Report honestly** - Include negative results
2. **Share data** - Raw data must be included
3. **Be reproducible** - Code must run and reproduce results
4. **Respect others** - Constructive criticism only

---

## What Counts as Falsification?

The ARC Principle is **falsified** if:

1. Sequential recursion consistently yields α ≤ 1
2. Parallel recursion consistently yields α ≥ 1
3. No systematic difference between conditions

**We welcome falsifications.** Disproving the principle is just as valuable as confirming it.

---

## Questions?

Open an issue or contact:
- Email: michael@michaeldariuseastwood.com
- GitHub Issues: Preferred for public questions

---

*Science advances through rigorous testing. Thank you for contributing.*
