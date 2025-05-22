"""
Longest Consecutive Sequence - EECS4070 Writeup

Problem:
---------
Given an unsorted array of integers `nums`, return the length of the longest sequence of consecutive integers.

A consecutive sequence is defined as numbers increasing by exactly 1.  
The elements do not need to be consecutive in the original array.  
You must solve this in O(n) time.

Examples:
---------
Input:  nums = [2, 20, 4, 10, 3, 4, 5]
Output: 4  # [2, 3, 4, 5]

Input:  nums = [0, 3, 2, 5, 4, 6, 1, 1]
Output: 7  # [0, 1, 2, 3, 4, 5, 6]

Constraints:
------------
- 0 <= nums.length <= 1000
- -10^9 <= nums[i] <= 10^9

link: https://neetcode.io/problems/longest-consecutive-sequence
"""

from typing import List

# -----------------------------------------------
# ✅ Solution: Using Set and Forward Expansion
# -----------------------------------------------

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        final_count = 0

        for i in nums_set:
            if i - 1 not in nums_set:  # Only start counting if it's the beginning of a sequence
                temp_counter = 1
                location = i
                while location + 1 in nums_set:
                    temp_counter += 1
                    location += 1
                final_count = max(final_count, temp_counter)

        return final_count

"""
Time Complexity: O(n)
- Each number is processed at most once, since we only explore sequences starting from the smallest number.

Space Complexity: O(n)
- A set is used to store all unique numbers for O(1) lookup.

Common Mistake:
---------------
❌ Sorting the array, which gives O(n log n) and violates the time constraint.
✅ Use a set for O(1) average time lookups.

"""

# -----------------------------------------------
# 🧪 Alternate version: Hongda Zhu’s Implementation
# -----------------------------------------------

class HongdaSolution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        final_count = 0

        for i in nums_set:
            temp_counter = 1
            location = i
            if i - 1 not in nums_set:
                while location + 1 in nums_set:
                    temp_counter += 1
                    location += 1
            if temp_counter > final_count:
                final_count = temp_counter

        return final_count

"""
Difference:
- This version tracks `temp_counter` outside the `if` block for clarity.
- The update to `final_count` is done after the `while` loop — fixed to handle cases like nums = [0] properly.

"""