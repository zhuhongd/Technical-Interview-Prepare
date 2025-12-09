# Week 4 — Sliding Window (Fixed & Variable Size)

> “Don’t scan; slide.”  
> — Every efficient LeetCode solver

---

### 🎯 Week Goal (and study tie‑in)
Master fixed-size, variable-size, and deque-backed sliding windows so you can turn O(n²) scans into O(n) passes.  
**Research hook:** Log how recognizing this pattern changes your solve time and confidence vs. brute force.

---

## 1. Why Sliding Window?

When a problem asks about **contiguous** subarrays/substrings, sliding window often replaces brute-force enumeration.  
We build on Week 2’s two-pointer intuition—now we **expand** and **shrink** a window to maintain constraints.

---

## 2. When to Use It

| If the prompt mentions…                          | Think…                            |
|--------------------------------------------------|-----------------------------------|
| “Window of size `k`”                             | **Fixed-size** window             |
| “Smallest/longest subarray with sum ≥ / ≤ X”     | **Variable-size** expand–shrink   |
| “Longest substring without repeating characters” | Variable window + set/map         |
| “Max/min in each window”                         | Fixed window + **monotonic deque**|
| “Frequency/count of chars in substring”          | Window + hashmap/counter          |

---

## 3. Types & Templates

### 🔹 Fixed-size Window
Size is given (e.g., `k`):

```python
L = 0
curr = 0
for R in range(len(nums)):
    curr += nums[R]
    if R - L + 1 > k:
        curr -= nums[L]
        L += 1
    # process window when size == k
```

### 🔹 Variable-Size Window (expand–shrink)

We grow `R`, then shrink `L` until the window satisfies a condition:

```python
L = 0
for R in range(len(s)):
    # include s[R] in the window
    ...
    while condition_is_violated():
        # exclude s[L] from the window
        L += 1
    # window [L..R] now satisfies the condition
```

### 🔹 Monotonic Deque Window (max/min in O(1))

Maintain indices in a deque in decreasing (for max) or increasing (for min) order so the **front is always the answer**.  
- Pop from the **back** while the new value breaks monotonicity.  
- Pop from the **front** if it falls out of the current window.

---

## 4. Practice Line-up & Why These Matter

| # | Problem (LeetCode)                                                      | File name                                      | Window Type              | Why it matters                                           |
|---|-------------------------------------------------------------------------|------------------------------------------------|--------------------------|----------------------------------------------------------|
| 1 | Contains Duplicate II (LC 219)                                          | `1. [easy] Contains Duplicate II.py`           | **Fixed** (`k` distance) | Set + fixed-window skeleton                              |
| 2 | Number of Sub-arrays of Size k & Avg ≥ Threshold (LC 1343)              | `2. [Medium] Number of Sub-arrays of Size ...py`| **Fixed**                | Rolling-sum template for O(1) updates                    |
| 3 | Minimum Size Subarray Sum (LC 209)                                      | `3. [Medium] Minimum Size Subarray Sum.py`     | **Variable (≥ target)**  | Classic expand–shrink                                    |
| 4 | Longest Substring Without Repeating Chars (LC 3)                        | `4. [Medium] Longest Substring Without Repeating Chars.py` | **Variable + set/map**   | “No duplicates” template                                 |
| 5 | Longest Repeating Character Replacement (LC 424)                        | `5. [Medium] Longest Repeating Character Replace...py`     | **Variable + freq map**  | “At most k changes” trick                                |
| 6 | Minimum Window Substring (LC 76)                                        | `6. [Hard] Minimum Window Substring.py`        | **Variable + 2 maps**    | Advanced: cover/need counters, shrink to minimum         |
| 7 | Sliding Window Maximum (LC 239)                                         | `7. [Hard] Sliding Window Maximum.py`          | **Fixed + deque**        | Monotonic deque = O(1) per-window max                    |

> Your `.py` files already have explanations—link them here for quick navigation.

---

## 5. Objectives

- **Recognize** sliding-window clues quickly.  
- **Implement** fixed and variable windows from memory.  
- **Combine** windows with sets/maps/counters/deques.  
- **Explain** why total pointer movement ⇒ amortized `O(n)` time.

---

## 6. Skip Test 🚦

Solve **[Minimum Window Substring (LC 76)](https://leetcode.com/problems/minimum-window-substring/)** in ≤ 30 minutes using a correct sliding-window + hashmap approach.  
Pass → proceed to **Week 4: Binary Search**.

---

## 7. (Optional) Data to Log for the Study

- Time to first accepted solution  
- Number of wrong submissions  
- Confidence before/after (1–5): “I can spot a sliding-window problem instantly.”

---

## 8. Further Reading & Videos

- NeetCode — Sliding Window patterns  
- Tech With Tim — Sliding Window Technique (YouTube)  
- LeetCode Explore Card — Sliding Window

---

**Next up → Week 5: Binary Search**  
Then we’ll hit Stacks/Queues/Monotonic structures in Week 5.

_Happy sliding!_ 🧠🚀
