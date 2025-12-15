# 1. Background and Objective

This document provides a **detailed, algorithm-oriented explanation** of solving

- **0/1 Knapsack Problem**, and
- **Multiple Knapsack Problem**

using **traditional two-dimensional dynamic programming (2D DP)**.

The explanation is tightly aligned with your actual Python implementations and is suitable for:

- Algorithm courses
- Course projects / reports
- Experimental baselines in research
- Oral or written technical explanations

The focus is on **clear state definitions, correct DP transitions, and traceback (path recovery)** rather than optimized variants.

---

# 2. Unified 2D DP Modeling Framework

## 2.1 State Definition

For both knapsack variants, we define the DP state as:

```text
dp[i][w] = the maximum total value achievable
           using the first i items
           with knapsack capacity w
```

Where:
- `i` represents the number of items considered (1 … n)
- `w` represents the remaining knapsack capacity (0 … W)

The DP table has size:

```text
(n + 1) × (W + 1)
```

Boundary conditions:
- `dp[0][w] = 0` for all `w`
- `dp[i][0] = 0` for all `i`

---

## 2.2 Core Decision Logic

At each state `(i, w)`, the algorithm decides **how many units of item i** to take:

- 0/1 Knapsack: `k ∈ {0, 1}`
- Multiple Knapsack: `k ∈ {0, 1, 2, …, c_i}`

All transitions follow the same principle:

```text
dp[i][w] = max over all feasible choices k
           ( dp[i-1][w - k·w_i] + k·v_i )
```

The difference lies only in the **range of k**.

---

# 3. 0/1 Knapsack Problem (2D DP + Traceback)

## 3.1 Mathematical Formulation

Given:
- `weights[i]`: weight of item i
- `values[i]`: value of item i
- `capacity`: maximum knapsack capacity

Objective:

```text
maximize   Σ value_i · x_i
subject to Σ weight_i · x_i ≤ capacity
           x_i ∈ {0, 1}
```

---

## 3.2 DP Transition Equation

For item `i` and capacity `w`:

```text
dp[i][w] = dp[i-1][w]                          (do not take item i)
           max(dp[i-1][w], dp[i-1][w-w_i]+v_i) (take item i, if w_i ≤ w)
```

The strict use of `dp[i-1][·]` ensures that **each item is used at most once**.

---

## 3.3 DP Table Construction

The DP table is initialized as:

```python
dp = [[0] * (capacity + 1) for _ in range(n + 1)]
```

The table is filled row by row:

- Each row corresponds to one item
- Each column corresponds to a capacity value

For each `(i, w)`:
1. Start with the value from the previous row (not taking item i)
2. Update the value if taking item i leads to a better result

---

## 3.4 Traceback (Path Recovery)

After filling the DP table, the selected items are recovered by backtracking from
`dp[n][capacity]`.

Key logic:

```text
If dp[i][w] ≠ dp[i-1][w],
then item i must have been selected.
```

Implementation idea:

- Start from the last item and full capacity
- Move upward row by row
- Reduce capacity when an item is selected

The result is a binary selection vector:

```text
[0, 1, 0, 1, ...]
```

---

# 4. Multiple Knapsack Problem (2D DP + Enumeration)

## 4.1 Mathematical Formulation

In the multiple knapsack problem, each item `i` has a limited count `c_i`:

```text
x_i ∈ {0, 1, 2, …, c_i}
```

Objective:

```text
maximize   Σ value_i · x_i
subject to Σ weight_i · x_i ≤ W
```

---

## 4.2 DP Transition Equation

For item `i` and capacity `w`:

```text
dp[i][w] = max_{k = 0 … c_i, k·w_i ≤ w}
           ( dp[i-1][w - k·w_i] + k·v_i )
```

This is the **most direct and classical formulation** of the multiple knapsack problem.

---

## 4.3 DP Table Construction (Triple Loop)

The DP table is filled using three nested loops:

1. Loop over items `i`
2. Loop over capacities `w`
3. Loop over possible counts `k`

Key properties:

- `k = 0` corresponds to not selecting item i
- All transitions use `dp[i-1][·]`, preventing reuse beyond `c_i`

This guarantees correctness but leads to higher time complexity.

---

## 4.4 Traceback Strategy

Traceback in the multiple knapsack problem is more involved than in 0/1 knapsack.

Your implementation adopts a **descending k-search strategy**:

```text
Try k from max feasible value down to 0
Find the first k that satisfies the DP equality
```

Why this works well:

- Avoids ambiguity when multiple k values yield the same optimal value
- Ensures a consistent and correct reconstruction of the solution

The final solution is a vector:

```text
[x_1, x_2, x_3, ...]
```

---

# 5. Comparison: 0/1 Knapsack vs Multiple Knapsack (2D DP)

| Aspect | 0/1 Knapsack | Multiple Knapsack |
|------|-------------|------------------|
| Decision variable | Binary (0/1) | Integer (0 … c_i) |
| Transition cost | O(1) | O(c_i) |
| Time complexity | O(nW) | O(nW·c) |
| DP dependency | dp[i-1] | dp[i-1] |
| Traceback difficulty | Easy | Moderate |
| Interpretability | Very high | Very high |

---

# 6. Summary and Research Perspective

Your current implementations:

- Follow **textbook-level 2D DP definitions**
- Provide **excellent interpretability**
- Are ideal as **baseline algorithms** for experiments

They are especially suitable when:

- Clarity is more important than speed
- The goal is explanation, teaching, or comparison

Natural next steps (if needed):

- Binary optimization for multiple knapsack
- Space optimization from 2D DP to 1D DP
- Empirical comparison of runtime and memory usage

These extensions can be built cleanly on top of your current work.

