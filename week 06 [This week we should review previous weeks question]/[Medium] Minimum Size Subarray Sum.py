"""
Problem: Minimum Size Subarray Sum

You are given an array of positive integers `nums` and a positive integer `target`. Return the **minimal length** of a contiguous subarray 
such that the sum is greater than or equal to `target`. If there is no such subarray, return 0.

Examples:
Input: target = 10, nums = [2,1,5,1,5,3]
Output: 3
Explanation: The subarray [5,1,5] has sum = 11 and is the shortest such subarray.

Input: target = 5, nums = [1,2,1]
Output: 0
Explanation: No subarray's sum is greater than or equal to 5.

Constraints:
- 1 <= nums.length <= 100,000
- 1 <= nums[i] <= 10,000
- 1 <= target <= 1,000,000,000

Follow-up:
Try to find a solution with time complexity O(n log n) or better.

Link: https://leetcode.com/problems/minimum-size-subarray-sum/
"""

# -----------------------------
# Brute Force Approach:
# -----------------------------
# Check all subarrays and track the shortest one with sum >= target.
# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution:
    def minSubArrayLen_brute(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        min_len = float('inf')

        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                if total >= target:
                    min_len = min(min_len, j - i + 1)
                    break

        return min_len if min_len != float('inf') else 0

# -----------------------------
# Optimized Sliding Window Approach:
# -----------------------------
# Use two pointers to dynamically expand and shrink the window.
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        total = 0
        min_len = float('inf')

        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1

        return min_len if min_len != float('inf') else 0

"""
Sliding Window Summary:

- Type: Shrinking window
- Expand: Move right pointer and add to the total
- Shrink: While total >= target, try to shrink the window from the left to minimize length
- Update: Track the minimum length whenever total is valid

This is a classic "minimum length" + "sum constraint" sliding window problem where the window grows and shrinks based on a dynamic condition.
"""
# -----------------------------
# Comprehensive offline tests
# -----------------------------
def _preview_arr(a, max_items=10):
    """Safe preview to avoid flooding output with very large arrays."""
    n = len(a)
    if n <= max_items:
        return str(a)
    head = ", ".join(map(str, a[:max_items // 2]))
    tail = ", ".join(map(str, a[-(max_items // 2):]))
    return f"[{head}, …, {tail}] (len={n})"

def _run_tests():
    sol = Solution().minSubArrayLen
    TESTS = [
        # Provided-style examples
        (10, [2, 1, 5, 1, 5, 3], 3, "example-1"),
        (5,  [1, 2, 1],          0, "example-2"),

        # Classic LC case
        (7,  [2, 3, 1, 2, 4, 3], 2, "classic-7→2"),

        # Small direct hits / misses
        (4,  [1, 4, 4],          1, "single-elem-hit"),
        (6,  [5],                0, "single-elem-miss"),
        (5,  [6, 1, 1],          1, "large-first-element"),
        (9,  [1, 1, 1, 6],       1, "large-at-end"),

        # Increasing sequence
        (11, [1, 2, 3, 4, 5],    3, "inc-11→[3,4,5]"),
        (15, [1, 2, 3, 4, 5],    5, "inc-15→all"),
        (16, [1, 2, 3, 4, 5],    0, "inc-16→none"),

        # Many small then a big
        (8,  [1, 1, 1, 1, 7],    2, "many-small-then-big"),
        (7,  [1, 1, 1, 1, 7],    1, "big-alone-reaches"),

        # All ones
        (10, [1]*9,              0, "all-ones-no-solution"),
        (9,  [1]*9,              9, "all-ones-exact"),
        (50, [1]*100,           50, "all-ones-large"),

        # Near-end optimal
        (9,  [1, 1, 1, 1, 1, 1, 3, 6], 2, "near-end-best"),

        # Random-ish sanity
        (5,  [2, 3],             2, "two-elem-exact"),
        (5,  [3, 3],             2, "two-elem-over"),
    ]

    passed = 0
    for i, (target, nums, expected, label) in enumerate(TESTS, 1):
        got = sol(target, nums)
        ok = (got == expected)
        passed += ok
        print(f"[{i:02d}][{label:<20}] target={target:<5} nums={_preview_arr(nums):<40} -> got={got:<2} expected={expected:<2} | {'✅' if ok else '❌'}")

    print(f"\nPassed {passed}/{len(TESTS)} tests.")

if __name__ == "__main__":
    _run_tests()