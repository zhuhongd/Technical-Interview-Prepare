# Week 4 — Binary Search

> “If your array is sorted or can be logically sorted, think binary search first.”  
> — Every efficient LeetCode solver

---

### 🎯 Week Goal (and why it matters for the study)
Master two flavors of Binary Search—**on indices** and **on answers (monotonic predicates)**—and log how this pattern affects speed/accuracy vs. brute force.

---

## 1. Why Binary Search?

Binary search cuts the search space in half each step → **O(log n)** instead of O(n).  
Use it when data is **sorted** OR when you can define a **monotonic yes/no condition** over a range of answers.

**Real-life analogy:** Flip through a dictionary by halves until you land on the word.

---

## 2. Common Clues in Interview Questions

| If the prompt says…                           | You should consider…                        |
|-----------------------------------------------|---------------------------------------------|
| “Sorted array” / “Rotated sorted array”       | Classic index binary search (with tweaks)   |
| “Find min/max feasible value” / “capacity”    | Binary search on the **answer space**       |
| “Must be O(log n)”                            | Binary search or divide & conquer           |

---

## 3. How Classic Binary Search Works

**Template (index search):**

```python
L, R = 0, len(arr) - 1
while L <= R:
    mid = L + (R - L) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        L = mid + 1
    else:
        R = mid - 1
return -1
```

> **Note:** Use `L + (R - L) // 2` instead of `(L + R) // 2` to avoid integer overflow in languages with fixed-width ints (not an issue in Python, but a good habit).

---

## 4. Two Core Variations

### 🔹 Variation A: **Search an Array (index-based)**
Given a sorted array, find the index/element (or insertion point).

### 🔹 Variation B: **Binary Search on Answers (predicate-based)**
You can’t binary search an index, but you can ask:  
*“Is it possible with speed `x`?”* or *“Can we allocate with capacity `x`?”*  
Define a monotonic `ok(x)` and binary search the smallest `x` that returns `True`.

**Predicate template (first `True`):**
```python
def ok(x) -> bool:
    # check feasibility for x
    ...

L, R = lo, hi  # inclusive bounds on answer space
while L < R:
    mid = (L + R) // 2
    if ok(mid):
        R = mid
    else:
        L = mid + 1
return L
```

## 5. Practice Line-up & Why These Matter

| # | Problem                                                                                     | File name                                   | Variant | Concept / Why It Matters                                               |
|---|----------------------------------------------------------------------------------------------|---------------------------------------------|---------|-------------------------------------------------------------------------|
| 1 | [Binary Search (LC 704)]                                                                     | `1. [easy] binary search.py`                 | A       | Pure template. Make zero off-by-one errors here.                        |
| 2 | [Search a 2D Matrix (LC 74)]                                                                 | `2. [easy] search a 2D matrix.py`            | A       | Treat 2D as 1D (index mapping).                                         |
| 3 | [Koko Eating Bananas (LC 875)]                                                               | `3. [Medium] Koko Eating Bananas.py`         | B       | Binary search on **answer space** (rate). Introduces predicate `ok(x)`. |
| 4 | [Find Minimum in Rotated Sorted Array (LC 153)]                                              | `4. [Medium] Find Min Rotated Array.py`      | A (mod) | Rotation pivot logic; careful with mid comparisons.                     |
| 5 | [Search in Rotated Sorted Array (LC 33)]                                                     | `5. [Medium] Search In Rotated Sorted Arra...py` | A (mod) | Partition thinking; two sorted halves.                                  |
| 6 | [Time Based Key-Value Store (LC 981)]                                                        | `6. [Medium] Time Based Key-Value Store.py`  | A/B*    | Map of lists + binary search by timestamp; hybrid pattern.              |
| 7 | [Median of Two Sorted Arrays (LC 4)] *(Optional / Hard)*                                     | `7. [Hard][Optional] Median of Two Sorted ...py` | A (part)| Partitioning two arrays; advanced BS trick.                              |

\*Uses hash map for storage + binary search on the timestamp list — good crossover problem.

---

## 6. Skip Test 🚦

Solve **Search in Rotated Sorted Array (LC 33)** in **≤ 20 minutes** with a correct modified binary search solution.  
Pass → move to **Week 5**.

---

## 7. Common Pitfalls

- Off-by-one loops (`while L < R` vs `<=`)  
- Not updating bounds → infinite loop  
- Mixing index-BS template with answer-BS logic  
- Forgetting to prove the predicate is monotonic (for answer-BS)  
- Mis-handling mid and neighbors in rotated-array problems

---

## 8. Further Reading & Resources

- LeetCode Explore Card: Binary Search  
- Blind 75 — Binary Search section  
- Google blog: overflow-safe `mid`

---

### ➡️ Next Up

**Week 5 — Stacks, Queues & Monotonic Structures (or Linked Lists if you reorder).**

