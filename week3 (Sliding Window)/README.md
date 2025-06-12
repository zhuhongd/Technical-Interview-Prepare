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

4. Practice Problem Line-Up & Why Each Matters
| # | Problem                                                                                                                                                            | File                                | Window Type   | Why it matters                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- | ------------- | ----------------------------------------------------- |
| 1 | [Contains Duplicate II (LC 219)](https://leetcode.com/problems/contains-duplicate-ii/)                                                                             | `contains_duplicate_ii.py`          | Fixed-size    | Core sliding window logic with set for duplicates     |
| 2 | [Number of Subarrays with Avg ≥ Threshold (LC 1343)](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/) | `subarrays_avg_threshold.py`        | Fixed-size    | Maintains a rolling sum for efficient updates         |
| 3 | [Minimum Size Subarray Sum (LC 209)](https://leetcode.com/problems/minimum-size-subarray-sum/)                                                                     | `min_size_subarray_sum.py`          | Variable-size | Expand and shrink window to minimize length           |
| 4 | [Longest Substring Without Repeating Chars (LC 3)](https://leetcode.com/problems/longest-substring-without-repeating-characters/)                                  | `longest_unique_substring.py`       | Variable-size | Tracks unique characters dynamically                  |
| 5 | [Longest Repeating Character Replacement (LC 424)](https://leetcode.com/problems/longest-repeating-character-replacement/)                                         | `longest_repeating_char_replace.py` | Variable-size | Combines sliding window with frequency counting       |
| 6 | [Minimum Window Substring (LC 76)](https://leetcode.com/problems/minimum-window-substring/)                                                                        | `minimum_window_substring.py`       | Variable-size | Advanced hash-map based window resizing               |
| 7 | [Sliding Window Maximum (LC 239)](https://leetcode.com/problems/sliding-window-maximum/)                                                                           | `sliding_window_maximum.py`         | Fixed-size    | Deque to efficiently track the max in a moving window |



(All .py files contain detailed explanations and step-by-step solutions.)

5. Objectives for Week 3
By the end of this week, you should be able to:

✅ Recognize when a sliding window solution is appropriate

✅ Implement fixed and variable-sized windows efficiently

✅ Combine sliding window logic with sets, maps, or frequency counters

✅ Clearly explain sliding window time complexity (amortized O(n))

6. Skip Test 🚦
Solve Minimum Window Substring (LC 76) using sliding window and hash maps within 30 minutes.

If you pass, you're ready for Week 4 (Prefix Sum & Greedy)!

7. Further Reading & Videos
📘 NeetCode Sliding Window Patterns

🎥 Sliding Window Technique — Tech With Tim (YouTube)

📚 LeetCode Sliding Window Explore Card

Next up:
Week 4 — Prefix Sum & Greedy! Master techniques to efficiently preprocess arrays and make optimal local choices.