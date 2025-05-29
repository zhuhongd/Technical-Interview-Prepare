# Week 2 — Two Pointers & Sliding Window

> “When brute force is too slow, try using two pointers.”  
> — Every successful LeetCode solver

---

## 1 Why two pointers?

Brute-force pair checks are **O(n²)**.  
With two pointers you often drop to **O(n)** while using **O(1)** space.

Typical clues:

### Real-world triggers for using two pointers:
| When the question mentions...      | You should think about...              |
|-----------------------------------|----------------------------------------|
| “Sorted array”                    | Use two ends to shrink the search space |
| “In-place modification”           | Use slow/fast pointer approach         |
| “Distance ≤ k” or “at most k”     | Use a window of size k                 |
| “Max area” / “Longest subarray”   | Shrink or expand the window            |

---

## 2. When do I use Two Pointers / Sliding Window?

Two pointers are often used when scanning a sequence from both ends or simulating a sliding window.

### Structure 1: From both ends
```python
L = 0
R = len(arr) - 1
while L < R:
    # Do something with arr[L] and arr[R]
    if some_condition:
        R -= 1
    else:
        L += 1
```
---

## 3. Practice Problem Line-Up & Why Each Matters

| # | Problem | File | Concept | Why it matters |
|---|---------|------|---------|---------------|
| 1 | [Remove Duplicates from Sorted Array (LC 26)](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | `remove_duplicates_from_sorted_array.py` | Two pointers (in-place) | Foundation for O(1) space “rewrite the array” tricks |
| 2 | [Remove Duplicates from Sorted Array II (LC 80)](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/) | `remove_duplicates_from_sorted_array_ii.py` | Two pointers (allow up to k) | Shows how to generalize the pattern, track allowed count |
| 3 | [Container With Most Water (LC 11)](https://leetcode.com/problems/container-with-most-water/) | `container_with_most_water.py` | Two pointers (maximize/minimize window) | How to shrink the search space from both sides |
| 4 | [Trapping Rain Water (LC 42)](https://leetcode.com/problems/trapping-rain-water/) | `trapping_rain_water.py` | Prefix/Suffix max, Two pointers | Combines two pointers with prefix arrays, builds on visual intuition |
| 5 | [Contains Duplicate II (LC 219)](https://leetcode.com/problems/contains-duplicate-ii/) | `contains_duplicate_ii.py` | Sliding window, set | Classic “track what’s in your window” problem |

*(All problems are in this folder. Each .py file has a full explanation and walkthrough.)*

---

## 4. Objectives for Week 2

By the end of this week, you should be able to:
- **Explain** when and why two pointers beats brute force.
- **Implement** two pointer and sliding window patterns for arrays and strings.
- **Modify code** to solve in-place problems without extra space.
- **Identify** classic interview clues (“sorted”, “find window”, “remove duplicates”) and apply these techniques on sight.

---

## 5. Skip Test 🚦

If you can solve [Container With Most Water (LC 11)](https://leetcode.com/problems/container-with-most-water/)  
using the two-pointer approach in ≤ 20 minutes and pass the tests, you’re ready to move to Week 3!

---

## 6. Further Reading & Videos

- [NeetCode — Two Pointers Playlist](https://www.youtube.com/playlist?list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATC)
- [LeetCode Explore Card: Two Pointers](https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-two-pointer-technique/)
- [Blind 75 — Two Pointer Questions](https://blind75.vercel.app/)

---

**Next up:**  
Week 3 — Sliding Window & Subarray Problems! You’ll learn how to optimize even more “subarray/substring” challenges, often with hash maps or counters.

Happy problem solving!
