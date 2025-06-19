# Week 4 — Binary Search

> “If your array is sorted or can be logically sorted, think binary search first.”  
> — Every efficient LeetCode solver

---

## 1 Why Binary Search?

Binary search is a highly efficient method for searching elements within **sorted arrays or ranges**. While linear search (**O(n)**) checks every element sequentially, binary search repeatedly cuts the search space in half, significantly speeding up the process to **O(log n)**.

**Real-life analogy:**  
Searching for a word in a dictionary — open the dictionary in the middle, determine if your word is before or after, and repeat until you find it.

### Common Clues in Interview Questions:

| When the question mentions...                 | You should think about...                          |
|-----------------------------------------------|----------------------------------------------------|
| “Sorted array” or “rotated sorted array”      | Binary search, possibly with modification          |
| “Find minimum/maximum” or “Optimal value”     | Binary search on answer ranges                     |
| “Logarithmic complexity O(log n)”             | Binary search or divide-and-conquer                |

---

## 2. How Binary Search Works (Step-by-Step)

**Key Idea:**  
Given a sorted array, binary search divides the array in half repeatedly, narrowing down the search space until the target is found or the space is exhausted.

### Typical Binary Search Template:
```python
L = 0
R = len(arr) - 1

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
** Note:
We use L + (R - L) // 2 instead of (L + R) // 2 to avoid potential overflow.


## 3. Two Common Variations of Binary Search

### 🔹 Variation 1: Search an Array

**Given:** A sorted array and a target  
**Goal:** Find the target’s index or return `-1` if it doesn’t exist.

**Example:**
```python
arr = [1, 2, 3, 4, 5, 6, 7, 8]
target = 5


| # | Problem                                                                                                            | File                                | Concept                    | Why it matters                  |
| - | ------------------------------------------------------------------------------------------------------------------ | ----------------------------------- | -------------------------- | ------------------------------- |
| 1 | [Binary Search (LC 704)](https://neetcode.io/problems/binary-search)                                               | `binary_search.py`                  | Basic binary search        | Essential foundation            |
| 2 | [Search a 2D Matrix (LC 74)](https://neetcode.io/problems/search-a-2d-matrix)                                      | `search_2d_matrix.py`               | Binary search in 2D        | 2D logic extension              |
| 3 | [Koko Eating Bananas (LC 875)](https://neetcode.io/problems/koko-eating-bananas)                                   | `koko_eating_bananas.py`            | Binary search on answer    | Search to minimize a result     |
| 4 | [Find Minimum in Rotated Sorted Array (LC 153)](https://neetcode.io/problems/find-minimum-in-rotated-sorted-array) | `find_min_rotated_sorted_array.py`  | Modified binary search     | Handle rotated inputs           |
| 5 | [Search in Rotated Sorted Array (LC 33)](https://neetcode.io/problems/search-in-rotated-sorted-array)              | `search_in_rotated_sorted_array.py` | Modified binary search     | Search with logical partitions  |
| 6 | [Median of Two Sorted Arrays (LC 4)](https://neetcode.io/problems/median-of-two-sorted-arrays)                     | `median_two_sorted_arrays.py`       | Binary search partitioning | Advanced usage of binary search |

## 6. Skip Test 🚦

If you can solve  
[**Search in Rotated Sorted Array (LC 33)**](https://neetcode.io/problems/search-in-rotated-sorted-array)  
in **20 minutes or less** using modified binary search and pass all test cases,  
you’re ready to move on to **Week 5**!

---

## 7. Further Reading & Resources

- [LeetCode Explore Card: Binary Search](https://leetcode.com/explore/learn/card/binary-search/)
- [Blind 75 — Binary Search Section](https://blind75.vercel.app/)
- [Google Research: Overflow-safe mid calculation](https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html)

---

## ➡️ Next Up

### **Week 5 — Stacks, Queues, and Monotonic Structures**

You’ll learn how to approach problems like:

- Stock span
- Largest rectangle in histogram
- Sliding window maximum
- Valid parentheses / bracket matching

These patterns are essential for solving tough linear scan problems and appear frequently in interviews.

