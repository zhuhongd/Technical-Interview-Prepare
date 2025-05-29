"""
Problem: Remove Duplicates from Sorted Array II

You are given an integer array `nums` sorted in non-decreasing order.  
Modify the array **in-place** so that **each unique element appears at most twice**.  
The relative order of the elements should remain the same.

Return the number of elements (`k`) in the final result, and ensure the first `k` elements of `nums` contain the answer.

Note:
- You **must not** use extra space for another array (O(1) space only).
- It does not matter what values remain in the array beyond index `k`.

Examples:

Input: nums = [1,1,1,2,2,3]  
Output: 5  
Explanation: nums becomes [1,1,2,2,3,_]

Input: nums = [0,0,1,1,1,1,2,3,3]  
Output: 7  
Explanation: nums becomes [0,0,1,1,2,3,3,_,_]

Constraints:
- 1 <= nums.length <= 30,000
- -10⁴ <= nums[i] <= 10⁴
- nums is sorted in non-decreasing order

Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
"""

# -----------------------------
# Optimized Two-Pointer Approach:
# -----------------------------
# Instead of comparing to just the previous number (as in the basic version),
# compare current number with the element at position (slow - 2).
# If they're different, it's safe to allow another occurrence.
#
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def remove_duplicates(self, nums: list) -> int:
        if len(nums) <= 2:
            return len(nums)

        slow = 2  # Start from index 2, first two elements are always allowed

        for fast in range(2, len(nums)):
            # Only write nums[fast] if it's not equal to nums[slow - 2]
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1

        return slow

# Example usage:
nums = [0,0,1,1,1,1,2,3,3]
sol = Solution()
k = sol.remove_duplicates(nums)
print("Unique count (allowing at most 2 duplicates):", k)
print("Modified array:", nums[:k])
# Output:
# Unique count: 7
# Modified array: [0, 0, 1, 1, 2, 3, 3]
