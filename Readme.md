# Constraint Satisfaction Problems (CSP) — Python Assignments

## Overview

A **Constraint Satisfaction Problem (CSP)** involves:

* A set of **variables** (e.g., regions, cells, letters)
* A **domain** of possible values for each variable
* A set of **constraints** that restrict valid assignments

The objective is to assign values to all variables such that **all constraints are satisfied**.

CSPs are commonly solved using **Backtracking**, a systematic trial-and-error method.

### Backtracking Steps

1. Select an unassigned variable
2. Assign a value from its domain
3. Check constraints
4. If violated, backtrack and try another value
5. Repeat until a solution is found

---

## Repository Contents

| File                        | Problem                     | Method             |
| --------------------------- | --------------------------- | ------------------ |
| `Australia_map_coloring.py` | Map coloring (7 regions)    | Backtracking       |
| `Telangana_map_coloring.py` | Map coloring (33 districts) | Backtracking       |
| `Sudoku_solver.py`          | 9×9 Sudoku solver           | Backtracking       |
| `cryptarithmetic.py`        | TWO + TWO = FOUR            | Permutation search |

---

## 1. Australia Map Coloring

### Problem

Color the seven regions of Australia — WA, NT, SA, Q, NSW, V, T — using three colors such that no adjacent regions share the same color.

### Adjacency List

```
WA   → NT, SA
NT   → WA, SA, Q
SA   → WA, NT, Q, NSW, V
Q    → NT, SA, NSW
NSW  → SA, Q, V
V    → SA, NSW
T    → (no neighbors)
```

### Approach

* Assign colors recursively
* Check neighbor constraints before assigning
* Backtrack when conflicts occur

### Sample Output

```
Australia Map Coloring (CSP)

Solution found!

WA   → Red
NT   → Green
SA   → Blue
Q    → Red
NSW  → Green
V    → Red
T    → Red
```

---

## 2. Telangana Map Coloring

### Problem

Color all 33 districts of Telangana such that no neighboring districts share the same color.

### Approach

* Use real adjacency data
* Apply backtracking similar to the Australia problem
* Use multiple colors to ensure feasibility

### Sample Output

```
Telangana Districts Map Coloring (CSP)

Solution found!

District                  Color
----------------------------------------
Adilabad                  Red
Komaram Bheem             Green
Mancherial                Blue
...
Hanamkonda                Green
```

---

## 3. Sudoku Solver

### Problem

Solve a 9×9 Sudoku puzzle with the following rules:

* Each row must contain digits 1–9 without repetition
* Each column must contain digits 1–9 without repetition
* Each 3×3 subgrid must contain digits 1–9 without repetition

### Input Puzzle

```
+-------+-------+-------+
| 5 3 . | . 7 . | . . . |
| 6 . . | 1 9 5 | . . . |
| . 9 8 | . . . | . 6 . |
+-------+-------+-------+
| 8 . . | . 6 . | . . 3 |
| 4 . . | 8 . 3 | . . 1 |
| 7 . . | . 2 . | . . 6 |
+-------+-------+-------+
| . 6 . | . . . | 2 8 . |
| . . . | 4 1 9 | . . 5 |
| . . . | . 8 . | . 7 9 |
+-------+-------+-------+
```

### Approach

* Find empty cells (0)
* Try digits 1–9
* Validate row, column, and subgrid constraints
* Backtrack when necessary

### Sample Output

```
Solution:

+-------+-------+-------+
| 5 3 4 | 6 7 8 | 9 1 2 |
| 6 7 2 | 1 9 5 | 3 4 8 |
| 1 9 8 | 3 4 2 | 5 6 7 |
+-------+-------+-------+
| 8 5 9 | 7 6 1 | 4 2 3 |
| 4 2 6 | 8 5 3 | 7 9 1 |
| 7 1 3 | 9 2 4 | 8 5 6 |
+-------+-------+-------+
| 9 6 1 | 5 3 7 | 2 8 4 |
| 2 8 7 | 4 1 9 | 6 3 5 |
| 3 4 5 | 2 8 6 | 1 7 9 |
+-------+-------+-------+
```

---

## 4. Cryptarithmetic Problem

### Problem

Solve the puzzle:

```
   T W O
 + T W O
 --------
   F O U R
```

Each letter represents a unique digit (0–9). Leading digits cannot be zero.

### Approach

* Generate permutations of digits
* Assign digits to letters
* Construct numerical values
* Check if the equation holds

### Sample Output

```
Cryptarithmetic: TWO + TWO = FOUR

Solution found!

T = 7
W = 3
O = 4
F = 1
U = 6
R = 8

Verification:
734 + 734 = 1468
```

---

## How to Run

Ensure Python 3 is installed. Run the files using:

```
python Australia_map_coloring.py
python Telangana_map_coloring.py
python Sudoku_solver.py
python cryptarithmetic.py
```

---

## Key Concepts

| Term         | Description                                      |
| ------------ | ------------------------------------------------ |
| Variable     | Element to assign a value (region, cell, letter) |
| Domain       | Possible values a variable can take              |
| Constraint   | Rule restricting valid assignments               |
| Backtracking | Recursive trial-and-error method                 |
| Permutation  | Arrangement of elements in different orders      |

---

## Conclusion

These implementations demonstrate how CSP techniques such as backtracking and permutation search can be applied to real-world and classic problems, including map coloring, Sudoku solving, and cryptarithmetic puzzles.
