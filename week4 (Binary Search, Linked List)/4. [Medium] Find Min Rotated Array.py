"""
Problem: Find Minimum in Rotated Sorted Array

You are given a rotated sorted array `nums` that was originally sorted in ascending order.
It was rotated between 1 and n times. Your task is to find the **minimum element**.

All elements are unique. Your solution must run in O(log n) time.

Examples:
Input: nums = [3,4,5,6,1,2] → Output: 1
Input: nums = [4,5,0,1,2,3] → Output: 0
Input: nums = [4,5,6,7] → Output: 4

Constraints:
- 1 <= nums.length <= 1000
- -1000 <= nums[i] <= 1000

Link: https://neetcode.io/problems/find-minimum-in-rotated-sorted-array
"""

# Approach: Binary Search (O(log n))
#
# Imagine a sorted array like [1, 2, 3, 4, 5, 6]
# If we rotate it 2 times, it becomes: [5, 6, 1, 2, 3, 4]
# The smallest value — the one we want — is 1.
#
# The trick is that although the array is rotated, at least one half is still sorted.
# We can use that fact to eliminate half of the array each time.
#
# Goal: Find the point where the order breaks — that's the minimum.
#
# Key Observations:
# - If nums[mid] > nums[r], the smallest value must be to the right of mid.
#   Example: [4,5,6,1,2,3] → nums[mid]=6, nums[r]=3 → go right
# - If nums[mid] < nums[r], the smallest is at mid or to the left.
#   Example: [6,1,2,3,4,5] → nums[mid]=2, nums[r]=5 → go left
#
# We repeat this until l == r, which will point to the minimum.

class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]

"""
Dry-run Example:

nums = [4,5,6,1,2,3]

Step 1: l=0, r=5 → mid=2 → nums[mid]=6, nums[r]=3 → 6 > 3 → l = mid + 1 = 3
Step 2: l=3, r=5 → mid=4 → nums[mid]=2, nums[r]=3 → 2 < 3 → r = mid = 4
Step 3: l=3, r=4 → mid=3 → nums[mid]=1, nums[r]=2 → 1 < 2 → r = mid = 3
End: l=3, r=3 → return nums[3] = 1

This shows how the loop eliminates half of the array at each step.
We never scan the entire array — this is why the solution runs in O(log n).
"""
