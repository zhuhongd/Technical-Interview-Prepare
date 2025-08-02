"""
Problem: Two Sum

Given an array of integers `nums` and an integer `target`, return the indices `i` and `j` such that:

    nums[i] + nums[j] == target and i != j

You must return the indices with the **smaller index first**.

You may assume that every input has exactly one solution.

Examples:
Input: nums = [3, 4, 5, 6], target = 7
Output: [0, 1]   # 3 + 4 = 7

Input: nums = [4, 5, 6], target = 10
Output: [0, 2]   # 4 + 6 = 10

Input: nums = [5, 5], target = 10
Output: [0, 1]

Constraints:
- 2 <= nums.length <= 1000
- -10^7 <= nums[i], target <= 10^7

Link: https://neetcode.io/problems/two-integer-sum
"""

# -----------------------------
# Brute Force Approach:
# -----------------------------
# Compare each pair of numbers to see if they sum to the target.
# Time complexity: O(n^2)
# Space complexity: O(1)

from typing import List
# you can just use "list", then you don't need to import library anymore.

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    return [min(i, j), max(i, j)]


# -----------------------------
# Optimized Hash Map Approach:
# -----------------------------
# As we iterate, we calculate the "complement" needed to reach the target.
# If it's already in the hash map, we return the indices.
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}  # Stores num -> index
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[nums[i]] = i

# Note: The idea is to remember what number we're looking for (target - current) as we scan through the list, instead of scanning again.

# -----------------------------
# Inline tests (no frameworks needed)
# -----------------------------

def _run_tests() -> None:
    sol = Solution().two_sum

    # Each case: (nums, target, expected_indices, label)
    TEST_CASES = [
        # From prompt
        ([3, 4, 5, 6], 7,  [0, 1], "example-1"),
        ([4, 5, 6],    10, [0, 2], "example-2"),
        ([5, 5],       10, [0, 1], "example-3"),

        # Standard basics
        ([2, 7, 11, 15], 9,  [0, 1], "classic"),
        ([3, 2, 4],      6,  [1, 2], "unsorted"),
        ([0, 4, 3, 0],   0,  [0, 3], "zeros-with-dup"),
        ([-3, 4, 1, 90], 1,  [0, 1], "negative-plus-positive"),
        ([2, -2, 9],     0,  [0, 1], "sum-to-zero"),

        # Duplicates / multiple same values
        ([1, 3, 3],      6,  [1, 2], "duplicate-3s"),
        ([1, 1, 2, 3],   2,  [0, 1], "duplicate-1s-early"),
        ([1, 2, 1, 3],   2,  [0, 2], "duplicate-1s-later"),

        # Large-ish but quick
        (list(range(1000)), 1997, [998, 999], "long-range"),
    ]

    passed = 0
    for i, (nums, target, expected, label) in enumerate(TEST_CASES, 1):
        got = sol(nums, target)

        # verify correctness and "smaller index first" contract
        ok = (
            got == expected and
            0 <= got[0] < got[1] < len(nums) and
            nums[got[0]] + nums[got[1]] == target
        )
        passed += ok

        def _preview(arr, limit=60):
            s = str(arr)
            return s if len(s) <= limit else s[:limit] + "...]"

        print(f"[{i:02d}][{label:<18}] nums={_preview(nums):<64} "
              f"target={target:<7} -> got={got} expected={expected} | {'✅' if ok else '❌'}")

    total = len(TEST_CASES)
    print(f"\nPassed {passed}/{total} tests.")


if __name__ == "__main__":
    _run_tests()