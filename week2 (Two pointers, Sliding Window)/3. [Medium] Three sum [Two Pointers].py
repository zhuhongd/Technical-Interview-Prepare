"""
3Sum (LeetCode #15) - EECS4070

Problem:
---------
Given an array `nums`, return all unique triplets [nums[i], nums[j], nums[k]] such that:
- i, j, and k are all different indices
- nums[i] + nums[j] + nums[k] == 0

You must not return duplicate triplets.

Examples:
---------
Input:  [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]

Input:  [0, 1, 1]
Output: []

Input:  [0, 0, 0]
Output: [[0, 0, 0]]

Constraints:
------------
- 3 <= nums.length <= 1000
- -10^5 <= nums[i] <= 10^5
"""

# How This Builds on Previous Problems:
# -------------------------------------
# - From **Two Sum II**, you learned how to use two pointers to find a pair that adds up to a target.
# - 3Sum fixes one element, then applies the Two Sum II logic to the remaining array.

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            # Skip duplicate fixed numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates on the left and right
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result

"""

Approach:
---------
1. Sort the array
2. Iterate through each number as a fixed element
3. Use two pointers (left, right) to find pairs that sum to -nums[i]
4. Skip duplicates at each step

Time Complexity: O(n^2)
- Outer loop runs n times, inner loop runs ~n times total

Space Complexity: O(1)
- No extra data structures used, apart from result list

This implementation is part of the EECS4070 Directed Study project by Hongda Zhu.
"""


