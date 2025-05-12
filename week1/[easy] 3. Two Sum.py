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

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
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
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}  # Stores num -> index
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_map:
                return [hash_map[complement], i]
            hash_map[nums[i]] = i

# Note: The idea is to remember what number we're looking for (target - current) as we scan through the list, instead of scanning again.