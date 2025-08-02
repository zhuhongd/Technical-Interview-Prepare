"""
Product of Array Except Self

Problem
-------
Given an integer array `nums`, return an array `output` such that:
    output[i] = product of all elements of nums *except* nums[i].

You must solve it in O(n) time without using division.

Examples
--------
Input : nums = [1, 2, 4, 6]
Output: [48, 24, 12, 8]

Input : nums = [-1, 0, 1, 2, 3]
Output: [0, -6, 0, 0, 0]

Constraints
----------
- 2 <= len(nums) <= 1000
- -20 <= nums[i] <= 20
- Result fits in 32-bit integer

Link: https://neetcode.io/problems/products-of-array-discluding-self?list=neetcode150
-----------------------------------------------------------
Approach: Prefix and Suffix Multiplication (O(n), no division)
-----------------------------------------------------------
Key idea:
For each position i,
  result[i] = (product of everything LEFT of i) * (product of everything RIGHT of i)

We build those two “sides” in two passes using only two running variables:
1) Left-to-right pass  : put the product of all elements to the *left* into result[i]
2) Right-to-left pass  : multiply result[i] by the product of all elements to the *right*

Why this works:
- When you stand on index i, everything left was already multiplied in pass #1,
  everything right is multiplied in pass #2.
- We never multiply nums[i] itself into result[i], because we write first, then update.

Small dry run (nums = [1, 2, 4, 6])
-----------------------------------
Pass 1 (prefix):
  prefix = 1
  i=0: result[0] = 1         ; prefix *= 1  -> 1
  i=1: result[1] = 1         ; prefix *= 2  -> 2
  i=2: result[2] = 2         ; prefix *= 4  -> 8
  i=3: result[3] = 8         ; prefix *= 6  -> 48
Now result holds left products: [1, 1, 2, 8]

Pass 2 (suffix):
  suffix = 1
  i=3: result[3] *= 1 -> 8   ; suffix *= 6  -> 6
  i=2: result[2] *= 6 -> 12  ; suffix *= 4  -> 24
  i=1: result[1] *= 24 -> 24 ; suffix *= 2  -> 48
  i=0: result[0] *= 48 -> 48 ; suffix *= 1  -> 48
Final: [48, 24, 12, 8]
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # Pass 1: prefix products (everything to the LEFT of i)
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]   # update AFTER writing, so nums[i] not included in result[i]

        # Pass 2: suffix products (everything to the RIGHT of i)
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]   # update AFTER multiplying, so nums[i] not included in result[i]

        return result


# -----------------------------
# Inline tests (easy to read & run)
# -----------------------------

def _run_tests() -> None:
    sol = Solution().productExceptSelf

    # Each case: (nums, expected, label)
    TEST_CASES = [
        # From prompt
        ([1, 2, 4, 6],            [48, 24, 12, 8],          "example-1"),
        ([-1, 0, 1, 2, 3],        [0, -6, 0, 0, 0],         "example-2-one-zero"),

        # Basic shapes
        ([1, 2],                  [2, 1],                   "two-elements"),
        ([1, 1, 1, 1],            [1, 1, 1, 1],             "all-ones"),
        ([-2, -3, -4],            [12, 8, 6],               "all-negatives"),

        # Zeros behavior
        ([2, 3, 0, 4],            [0, 0, 24, 0],            "single-zero-center"),
        ([0, 0, 5],               [0, 0, 0],                "two-zeros"),

        # Mixed signs / variety
        ([2, -3, 4],              [-12, 8, -6],             "mixed-signs"),
        ([0, 1, 2, 3, 4],         [24, 0, 0, 0, 0],         "zero-at-start"),
        ([1, 2, 3, 0],            [0, 0, 0, 6],             "zero-at-end"),
    ]

    passed = 0
    for i, (nums, expected, label) in enumerate(TEST_CASES, 1):
        got = sol(nums)
        ok = (got == expected)
        passed += ok
        print(f"[{i:02d}][{label:<20}] nums={nums} -> got={got} expected={expected} | {'✅' if ok else '❌'}")


    total = len(TEST_CASES)
    print(f"\nPassed {passed}/{total} tests.")


if __name__ == "__main__":
    _run_tests()
