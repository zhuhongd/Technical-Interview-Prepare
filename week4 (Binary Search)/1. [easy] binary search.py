"""
Problem: Binary Search

You are given an array of distinct integers `nums`, sorted in ascending order, and an integer `target`.

Implement a function to search for `target` within `nums`. 
If it exists, return its index. Otherwise, return -1.

Your solution must run in O(log n) time.

Examples:
Input: nums = [-1, 0, 2, 4, 6, 8], target = 4
Output: 3

Input: nums = [-1, 0, 2, 4, 6, 8], target = 3
Output: -1

Constraints:
- 1 <= nums.length <= 10,000
- -10,000 < nums[i], target < 10,000
- All the integers in nums are unique

Link: https://neetcode.io/problems/binary-search
"""

# Approach:
# Step 1: Set two pointers: `left` at 0 and `right` at the last index.
#
# Step 2: While left <= right, calculate the middle index `mid`.
#         If nums[mid] == target, return mid.
#         If nums[mid] < target, search in the right half (left = mid + 1).
#         If nums[mid] > target, search in the left half (right = mid - 1).
#
# Step 3: If the loop ends without finding the target, return -1.
#
# Why it works:
# Because the input is sorted, we can eliminate half the search space
# each time — this makes the time complexity O(log n).

# [Knowledge] Midpoint calculation:
# Use mid = (left + right) // 2 to avoid floating point.
# If worried about integer overflow (not an issue in Python), use:
# mid = left + (right - left) // 2

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1  # target not found
