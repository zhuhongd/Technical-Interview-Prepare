# Week 3 — Sliding Window (Fixed & Variable Size)

> "Don't scan; slide your way to efficiency."  
> — Every efficient LeetCode solver

---

## 1. Why Sliding Window?

Sliding Window is an essential pattern for solving problems involving **contiguous sequences** like subarrays or substrings.

Instead of brute-forcing every possible subarray (O(n²)), sliding window techniques reduce complexity to O(n) by expanding and shrinking a window dynamically.

---

## 2. When do I use Sliding Window?

Typical clues that you should consider a sliding window:

| When the question mentions...                  | You should think...                 |
|------------------------------------------------|-------------------------------------|
| “Window of size k”                             | Fixed-size window                   |
| “Subarray/subsequence with sum ≥ target”       | Variable-size window                |
| “Longest substring without repeating chars”    | Expand/shrink window dynamically    |
| “Maximum/minimum of subarrays”                 | Maintain max/min using deque        |
| “Frequency/count of characters”                | Sliding window + hash map/counter   |

---

## 3. Types of Sliding Window

### Fixed-size Sliding Window
Used when the size of the window is **given explicitly**.

**Template:**
```python
window_sum = 0
L = 0
for R in range(len(nums)):
    window_sum += nums[R]
    if R - L + 1 > k:
        window_sum -= nums[L]
        L += 1
```

## 4 Practice Problem Line-Up & Why Each Matters

| # | Problem (LeetCode) | File | Window Type | Why it matters |
|---|--------------------|------|-------------|----------------|
| 1 | Contains Duplicate II (LC 219) | `contains_duplicate_ii.py` | **Fixed** | Core window + `set` for “duplicates within k” |
| 2 | Number of Sub-arrays of Size k & Avg ≥ Threshold (LC 1343) | `subarrays_avg_threshold.py` | **Fixed** | Rolling-sum template for O(1) updates |
| 3 | Minimum Size Subarray Sum (LC 209) | `min_size_subarray_sum.py` | **Variable** | Classic expand-shrink to minimize length |
| 4 | Longest Substring Without Repeating Chars (LC 3) | `longest_unique_substring.py` | **Variable** | Tracks unique chars with a moving set/map |
| 5 | Longest Repeating Character Replacement (LC 424) | `longest_repeating_char_replace.py` | **Variable** | Window + frequency map; “at most k changes” |
| 6 | Minimum Window Substring (LC 76) | `minimum_window_substring.py` | **Variable** | Advanced: two counters + shrink to minimum |
| 7 | Sliding Window Maximum (LC 239) | `sliding_window_maximum.py` | **Fixed** + deque | Monotonic deque for O(1) max retrieval |

> *All `.py` files include full explanations and step-by-step comments.*

---

## 5 Objectives for Week 3

- [x] **Recognize** when a sliding-window solution is appropriate.  
- [x] **Implement** both fixed-size and variable-size windows from memory.  
- [x] **Combine** windows with sets, hash maps, counters, or deques.  
- [x] **Explain** why total pointer movement ⇒ **amortized O(n)** time.

---

## 6 Skip Test 🚦

Solve **[Minimum Window Substring (LC 76)](https://leetcode.com/problems/minimum-window-substring/)** in ≤ 30 minutes using the sliding-window + hash-map approach.

Pass it? 🎉 — Proceed to **Week 4: Prefix Sum & Greedy**.

---

## 7 Further Reading & Videos

- 📘 [NeetCode — Sliding Window Patterns](https://neetcode.io/roadmap)  
- 🎥 [Tech With Tim — Sliding Window Technique](https://www.youtube.com/watch?v=MK-NZ4hN7rs)  
- 📚 [LeetCode Explore Card — Sliding Window](https://leetcode.com/explore/learn/card/sliding-window/)

---

**Next up →** **Week 4 — Prefix Sum & Greedy**: learn to preprocess arrays for constant-time range queries and to make optimal local decisions.

*Happy sliding!* 🧠🚀
