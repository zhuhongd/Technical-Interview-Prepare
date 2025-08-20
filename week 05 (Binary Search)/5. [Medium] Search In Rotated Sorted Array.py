"""
🔍 Problem: Search in Rotated Sorted Array

You are given a rotated version of a sorted array with **distinct integers**.
Return the index of the target if it's found, otherwise return -1.

Example:
Input: nums = [3,4,5,6,1,2], target = 1 → Output: 4
Input: nums = [3,5,6,0,1,2], target = 4 → Output: -1

Constraints:
- All elements are unique
- Time complexity must be O(log n)
- 1 <= len(nums) <= 1000

🔗 Link: https://neetcode.io/problems/search-in-rotated-sorted-array
"""

# ✅ Approach:
# This is a **modified binary search** problem.
# Even though the array is rotated, at every step, **one side is guaranteed to be sorted**.

# Step-by-step:
# 1. Compute the middle index.
# 2. Check if the middle element is the target.
# 3. Decide which half is sorted:
#    - If nums[left] <= nums[mid]: the **left half** is sorted.
#    - Otherwise, the **right half** is sorted.
# 4. Determine whether the target is in the sorted half:
#    - If it is, narrow the search to that half.
#    - If not, search the other half.

# ❗️Why it works:
# Because we're eliminating half the array each time — just like in regular binary search —
# the time complexity remains O(log n), even with the rotation.

# 💡 Tip:
# Always draw out a rotated array with mid pointers to visualize sorted vs unsorted halves.

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
