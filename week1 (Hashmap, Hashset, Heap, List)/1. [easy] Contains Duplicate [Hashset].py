"""
Problem: Contains Duplicate

Given an integer array `nums`, return `true` if any value appears more than once in the array, and return `false` if every element is distinct.

Examples:
Input: nums = [1, 2, 3, 3]
Output: True

Input: nums = [1, 2, 3, 4]
Output: False

link: https://neetcode.io/problems/duplicate-integer
"""

# Brute-force approach:
# Use a nested loop to compare each pair of elements.
# If two elements have the same value but different indices, return True.
# Time Complexity: O(n^2) — inefficient for large arrays.

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] == nums[j]:
                    return True
        return False

# This approach works, but it's slow due to repeated comparisons.
# Can you even imagine if this list is longer, and each element would need to manually compare with the entire list?

# Optimized approach is using a set (hash set) [Knowledge 1.]:
# As we iterate through the array, we add each number to a set.
# If we encounter a number that is already in the set, we return True.
# Time Complexity: O(n)
# Space Complexity: O(n)

# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         hash_set = set()
#         for num in nums:
#             if num in hash_set:
#                 return True
#             hash_set.add(num)
#         return False

def _run_tests() -> None:
    sol = Solution().hasDuplicate

    # Each item: (input_list, expected_output, short_label)
    TEST_CASES = [
        # From examples
        ([1, 2, 3, 3], True,  "example-dup"),
        ([1, 2, 3, 4], False, "example-uniq"),

        # Tiny / edge
        ([], False,           "empty"),
        ([1], False,          "single"),
        ([1, 1], True,        "pair-dup"),

        # Duplicates in different positions
        ([1, 2, 3, 1], True,  "dup-first-last"),
        ([1, 1, 2, 3], True,  "dup-start"),
        ([1, 2, 3, 3], True,  "dup-end"),
        ([1, 2, 1, 3, 2], True, "multiple-dups"),  # multiple values repeated
        ([2, 1, 3, 4, 5, 2], True, "dup-middle"),

        # No duplicates / unordered
        ([4, 1, 5, 2, 6, 3], False, "uniq-shuffled"),

        # Negatives and zero
        ([0, -1, -2, -3, -4], False, "neg-uniq"),
        ([0, -1, -2, -3, -1], True,  "neg-dup"),
        ([0, 0], True,               "zero-dup"),

        # Mixed magnitudes
        ([10**9, -10**9, 123456, -123456], False, "large-uniq"),
        ([10**9, -10**9, 123456, -123456, 10**9], True, "large-dup"),

        # Repeated many times (small but clear)
        ([5, 5, 5, 5], True,  "all-same"),
        ([1, 2, 3, 4, 5, 6, 7, 8], False, "range-uniq"),

        # A bit longer, still quick to run
        (list(range(50)), False, "long-uniq"),
        ([*range(40), 7], True,  "long-with-dup-end"),
    ]

    passed = 0
    for i, (nums, expected, label) in enumerate(TEST_CASES, 1):
        got = sol(nums)
        ok = (got == expected)
        passed += ok
        # Truncate long input display for readability
        preview = str(nums)
        if len(preview) > 70:
            preview = preview[:67] + "...]"
        print(f"[{i:02d}][{label:<16}] input={preview:<72} -> got={got} expected={expected} | {'✅' if ok else '❌'}")

    total = len(TEST_CASES)
    print(f"\nPassed {passed}/{total} tests.")


if __name__ == "__main__":
    _run_tests()