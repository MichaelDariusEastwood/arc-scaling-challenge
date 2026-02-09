# Measurement Protocol: AI Language Models

**Version 1.0 | ARC Scaling Challenge**

---

## Overview

This protocol specifies how to measure the scaling exponent α in large language models under sequential vs parallel recursive conditions.

---

## Requirements

### Model Requirements
- Access to model with visible reasoning tokens (e.g., DeepSeek R1, o1-style models)
- OR ability to implement chain-of-thought prompting
- API access or local deployment

### Data Requirements
- Minimum 5 different recursive depths (R values)
- Minimum 10 problems per condition
- Problems with verifiable correct answers

---

## Experimental Design

### Condition 1: Sequential Recursion

Sequential recursion = each reasoning step builds on previous output.

```
Prompt structure:
"Solve this step by step. Show your reasoning at each step.
After each step, review and refine your answer.
Problem: [PROBLEM]"
```

**Measure:** Token count at each reasoning depth

**Vary R by:** Controlling reasoning steps (e.g., "Think for 1 step", "Think for 3 steps", etc.) or natural variation in chain-of-thought length

### Condition 2: Parallel Recursion

Parallel recursion = independent samples aggregated.

```
Method:
1. Generate N independent responses (no shared context)
2. Aggregate by majority vote
3. Vary N: 1, 2, 4, 8, 16 samples
```

**Measure:** Number of parallel samples (N)

---

## Measurement Procedure

### Step 1: Select Problem Set

Requirements:
- Problems with single correct answer
- Difficulty appropriate for model
- Diverse problem types recommended

Suggested sources:
- AIME (mathematics)
- GSM8K (grade school math)
- MMLU subsets
- Custom domain-specific problems

### Step 2: Run Sequential Condition

```python
for depth in [1, 2, 4, 8, 16]:  # or natural variation
    for problem in problems:
        response = model.generate(
            prompt=sequential_prompt(problem, depth),
            temperature=0  # deterministic
        )
        record(depth, response, is_correct)
```

### Step 3: Run Parallel Condition

```python
for n_samples in [1, 2, 4, 8, 16]:
    for problem in problems:
        responses = [model.generate(prompt, temp=1.0)
                     for _ in range(n_samples)]
        final_answer = majority_vote(responses)
        record(n_samples, final_answer, is_correct)
```

### Step 4: Calculate Error Rates

```
E(R) = (incorrect responses) / (total responses) at depth R
```

---

## Analysis

### Fit Power Law

```
E(R) = E_0 × R^(-α)

Log-transform:
log(E) = log(E_0) - α × log(R)
```

Use provided tools:
```bash
python tools/alpha_estimator.py --data results.csv --condition sequential
python tools/alpha_estimator.py --data results.csv --condition parallel
```

### Model Comparison

Compare power-law fit against alternatives:
- Logarithmic: E(R) = a - b×log(R)
- Exponential: E(R) = a×exp(-b×R)
- Linear: E(R) = a - b×R

Use AIC/BIC calculator:
```bash
python tools/aic_bic_calculator.py --data results.csv
```

---

## Data Format

Save results as CSV:

```csv
condition,R,n_problems,n_correct,n_incorrect,error_rate
sequential,1,50,25,25,0.50
sequential,2,50,35,15,0.30
sequential,4,50,42,8,0.16
sequential,8,50,46,4,0.08
parallel,1,50,30,20,0.40
parallel,2,50,32,18,0.36
parallel,4,50,33,17,0.34
parallel,8,50,34,16,0.32
```

---

## Expected Results (If ARC Holds)

| Condition | Expected α | 95% CI |
|-----------|------------|--------|
| Sequential | α > 1 (super-linear) | [1.0, 3.0] |
| Parallel | α ≈ 0 (sub-linear) | [-0.5, 0.5] |

---

## Falsification Conditions

The ARC Principle is **falsified** for AI systems if:

1. Sequential recursion yields α ≤ 1 consistently
2. Parallel recursion yields α ≥ 1 consistently
3. No significant difference between conditions

---

## Submission Checklist

- [ ] Raw data (CSV)
- [ ] Model identification (name, version, API endpoint)
- [ ] Problem set description
- [ ] α estimates with 95% CI for both conditions
- [ ] AIC/BIC model comparison results
- [ ] Analysis code (reproducible)

---

## Example Submission

See `submissions/results/example_ai_submission/` for a complete worked example.
