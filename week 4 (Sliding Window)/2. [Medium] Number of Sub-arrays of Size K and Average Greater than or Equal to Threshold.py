"""
Number of Sub-arrays of Size K and Average ≥ Threshold — EECS4070 (Explained, Single Active Solution)

Problem
-------
Given an integer array `arr`, and integers `k` and `threshold`, return the number of
contiguous subarrays of length `k` whose **average** is ≥ `threshold`.

Link
----
https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

Key Examples
------------
Example 1
arr = [2, 2, 2, 2, 5, 5, 5, 8], k = 3, threshold = 4  →  3

Subarray     Sum   Avg  Pass?
-----------------------------
[2,2,2]       6     2     ✘
[2,2,5]       9     3     ✘
[2,5,5]      12     4     ✅
[5,5,5]      15     5     ✅
[5,5,8]      18     6     ✅
Total: 3 subarrays with avg ≥ 4.

Example 2
arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5  →  6
(The first 6 windows of size 3 meet or exceed the threshold.)

Constraints
-----------
- 1 <= arr.length <= 10^5
- 1 <= arr[i] <= 10^4
- 1 <= k <= arr.length
- 0 <= threshold <= 10^4
"""

# -----------------------------
# Optimized Sliding Window (O(n), O(1) space)
# -----------------------------
# Maintain the sum of the current window of size k.
# Compare window_sum directly with (k * threshold) to avoid floats.
#
# Window update per step:
#   window_sum += arr[i]      # add new right element
#   window_sum -= arr[i - k]  # remove old left element
#
# If window_sum >= k * threshold → count += 1

class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        required_sum = k * threshold
        window_sum = sum(arr[:k])
        count = 1 if window_sum >= required_sum else 0

        for i in range(k, len(arr)):
            window_sum += arr[i] - arr[i - k]
            if window_sum >= required_sum:
                count += 1
        return count


# -----------------------------
# (Optional) Brute Force for study (commented)
# -----------------------------
# class Solution:
#     def numOfSubarrays_brute(self, arr: list[int], k: int, threshold: int) -> int:
#         count = 0
#         for i in range(len(arr) - k + 1):
#             if sum(arr[i:i+k]) >= k * threshold:
#                 count += 1
#         return count


# -----------------------------
# Comprehensive offline tests
# -----------------------------
def _preview_arr(a, max_items=8):
    """Safe preview for potentially huge arrays."""
    n = len(a)
    if n <= max_items:
        return str(a)
    head = ", ".join(map(str, a[:max_items//2]))
    tail = ", ".join(map(str, a[-(max_items//2):]))
    return f"[{head}, …, {tail}] (len={n})"

def _run_tests():
    sol = Solution().numOfSubarrays
    TESTS = [
        # Provided examples
        ([2, 2, 2, 2, 5, 5, 5, 8], 3, 4, 3, "example-1"),
        ([11,13,17,23,29,31,7,5,2,3], 3, 5, 6, "example-2"),

        # Edge cases
        ([1], 1, 1, 1, "single-element-pass"),
        ([1], 1, 2, 0, "single-element-fail"),

        # Threshold extremes
        ([5,5,5,5], 2, 0, 3, "zero-threshold-all-pass"),
        ([5,5,5,5], 2, 5, 3, "exact-threshold-all-pass"),
        ([5,5,5,5], 2, 6, 0, "above-threshold-all-fail"),

        # Various k sizes
        ([4,4,4,4,4], 1, 4, 5, "k-one-all-equal"),
        ([4,4,4,4,4], 5, 4, 1, "k-equals-length-pass"),
        ([4,4,4,4,3], 5, 4, 0, "k-equals-length-fail"),

        # Mixed values
        ([1,2,3,4,5,6,7,8,9], 3, 5, 4, "ascending-mixed"),
        ([9,8,7,6,5,4,3,2,1], 3, 5, 4, "descending-mixed"),

        # Repeated patterns
        ([1,2,1,2,1,2], 2, 1, 5, "repeated-pattern-low-threshold"),
        ([1,2,1,2,1,2], 2, 2, 0, "repeated-pattern-high-threshold"),

        # Alternating pass/fail
        ([3,6,3,6,3,6], 2, 4, 5, "alternating-pass-fail"),

        # Large-n sanity (kept small enough for terminal)
        ([10**4]*1000, 1000, 10**4, 1, "large-same-pass"),
        ([1]*1000, 1000, 2, 0, "large-same-fail"),
    ]

    passed = 0
    for i, (arr, k, threshold, expected, label) in enumerate(TESTS, 1):
        got = sol(arr, k, threshold)
        ok = (got == expected)
        passed += ok
        print(f"[{i:02d}][{label:<32}] arr={_preview_arr(arr):<40} k={k:<5} thr={threshold:<5} -> got={got:<3} expected={expected:<3} | {'✅' if ok else '❌'}")

    print(f"\nPassed {passed}/{len(TESTS)} tests.")

if __name__ == "__main__":
    _run_tests()
