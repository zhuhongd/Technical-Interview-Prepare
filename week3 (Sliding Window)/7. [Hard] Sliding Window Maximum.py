"""
Sliding Window Maximum — EECS4070 (Explained, Single Active Solution)

Problem
-------
You are given an integer array `nums` and an integer `k`.
There is a sliding window of size `k` that moves from left to right.
Return a list of the **maximum element** in the window at each step.

Link
----
https://leetcode.com/problems/sliding-window-maximum/

Key Example
-----------
nums = [1, 2, 1, 0, 4, 2, 6], k = 3  ->  [2, 2, 4, 4, 6]

Sliding windows and max values:
[1  2  1] 0  4  2  6  → max = 2
 1 [2  1  0] 4  2  6  → max = 2
 1  2 [1  0  4] 2  6  → max = 4
 1  2  1 [0  4  2] 6  → max = 4
 1  2  1  0 [4  2  6] → max = 6

Thinking (Monotonic Deque, O(n))
--------------------------------
Goal: Always know the maximum of the *current* window in O(1).
We keep a **deque of indices** such that their values are in **decreasing order**.
Front of deque = index of current window’s maximum.

For each new position `right`:
1) **Pop from the back** while the new value is **≥** the value at the back’s index
   (those smaller/equal ones can never be a future max once the new, later, bigger-or-equal value arrives).
2) **Push right** into the deque.
3) **Pop from the front** if it’s **outside** the current window (index < right-k+1).
4) If we have a full window (right ≥ k-1), **record nums[deque[0]]** as the max.

Why it works:
- The deque keeps only “useful” indices in decreasing value order.
- The max is always at the front; outdated indices are removed when they leave the window.

Complexity
----------
Time:  O(n) — each index is pushed/popped at most once.
Space: O(k) — deque holds at most k indices.
"""

from collections import deque
from typing import List


# -----------------------------
# ✅ Active Solution: Monotonic Deque (O(n) time, O(k) space)
# -----------------------------
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k == 0 or n == 0:
            return []
        if k == 1:
            return nums[:]  # every single element is a window max

        dq = deque()   # will store indices; values are in decreasing order
        ans: List[int] = []

        for right in range(n):
            # 1) Remove smaller or equal values from the back
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()

            # 2) Push current index
            dq.append(right)

            # 3) Remove front if it's outside the window (window start = right - k + 1)
            window_start = right - k + 1
            if dq[0] < window_start:
                dq.popleft()

            # 4) Record max once the first full window forms
            if right >= k - 1:
                ans.append(nums[dq[0]])

        return ans


# -----------------------------
# Comprehensive offline tests
# -----------------------------
def _preview_arr(a, max_items=12):
    """Safe preview for arrays (avoids printing huge lists)."""
    n = len(a)
    if n <= max_items:
        return str(a)
    head = ", ".join(map(str, a[:max_items // 2]))
    tail = ", ".join(map(str, a[-(max_items // 2):]))
    return f"[{head}, …, {tail}] (len={n})"

def _run_tests():
    f = Solution().maxSlidingWindow
    TESTS = [
        # Provided example
        ([1, 2, 1, 0, 4, 2, 6], 3, [2, 2, 4, 4, 6], "example"),

        # Basic sanity
        ([1], 1, [1], "single"),
        ([2, 1], 1, [2, 1], "k=1-return-self"),
        ([2, 1], 2, [2], "k=len(nums)"),

        # Increasing
        ([1, 2, 3, 4, 5], 2, [2, 3, 4, 5], "increasing-k2"),
        ([1, 2, 3, 4, 5], 3, [3, 4, 5], "increasing-k3"),

        # Decreasing
        ([5, 4, 3, 2, 1], 2, [5, 4, 3, 2], "decreasing-k2"),
        ([5, 4, 3, 2, 1], 3, [5, 4, 3], "decreasing-k3"),

        # Duplicates and equals
        ([4, 4, 4, 4], 2, [4, 4, 4], "all-equal"),
        ([1, 3, 3, 3, 2], 3, [3, 3, 3], "plateau-equals"),

        # Mixed positives/negatives
        ([-1, -3, 5, 3, 6, 7], 3, [5, 5, 6, 7], "negatives-mixed"),
        ([0, -1, -1, 2, -3, 5], 2, [0, -1, 2, 2, 5], "mix-k2"),

        # Edge-ish k values
        ([9, 7, 2, 4, 6, 8, 2, 1], 4, [9, 7, 8, 8, 8], "k4"),
        ([1, 2, 3, 2, 1, 2, 3], 3, [3, 3, 3, 2, 3], "zigzag-k3"),

        # ---- Out-of-constraint but useful defensive tests ----
        ([], 0, [], "empty-nums-k0"),
        ([], 1, [], "empty-nums-k1"),
        ([1, 2, 3], 0, [], "k-zero"),
        ([1, 2, 3], 4, [], "k-greater-than-n"),
        ([], 3, [], "empty-nums-k3"),
    ]

    passed = 0
    for i, (nums, k, expected, label) in enumerate(TESTS, 1):
        got = f(nums, k)
        ok = (got == expected)
        passed += ok
        print(f"[{i:02d}][{label:<16}] nums={_preview_arr(nums):<34} k={k:<2} -> got={got!s:<18} expected={expected!s:<18} | {'✅' if ok else '❌'}")

    print(f"\nPassed {passed}/{len(TESTS)} tests.")

if __name__ == "__main__":
    _run_tests()
