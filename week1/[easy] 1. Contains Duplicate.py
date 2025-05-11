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

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)
        return False
