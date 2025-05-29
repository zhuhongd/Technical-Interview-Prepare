"""
Problem: Remove Duplicates from Sorted Array

You are given an integer array `nums` sorted in **non-decreasing** order.  
Your task is to remove duplicates from `nums` **in-place**, so that each element appears only once.

After removing the duplicates, return the number of unique elements, denoted as `k`, such that the first `k` elements of `nums` contain the unique elements **in the same relative order** as the original.

Return `k` as the final result.

Note:
- It is **not necessary** to consider elements beyond the first `k` positions of the array.
- You **must modify the input array in-place** with O(1) extra memory.

Examples:
Input: nums = [1, 1, 2, 3, 4]  
Output: 4  # Unique elements are [1, 2, 3, 4]

Input: nums = [2, 10, 10, 30, 30, 30]  
Output: 3  # Unique elements are [2, 10, 30]

Constraints:
- 1 <= nums.length <= 30,000
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order

Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

# -----------------------------
# Brute Force (Invalid in this case):
# -----------------------------
# A naive solution would use an extra array to collect unique elements and return len(set(nums)).
# BUT this violates the problem constraint of modifying the array *in-place* with O(1) extra space.

# -----------------------------
# Optimized Two-Pointer Approach:
# -----------------------------
# Use two pointers: `slow` tracks where the next unique element should go,
# and `fast` scans through the array.
# We only write to nums[slow] when we find a new unique element at nums[fast].
#
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def remove_duplicates(self, nums: list) -> int:
        if not nums:
            return 0

        slow = 1  # Start writing from index 1
        for fast in range(1, len(nums)):
            if nums[fast] != nums[fast - 1]:  # Found a new unique element
                nums[slow] = nums[fast]
                slow += 1

        return slow

# Example usage:
nums = [2, 10, 10, 30, 30, 30]
sol = Solution()
k = sol.remove_duplicates(nums)
print("Unique count:", k)
print("Modified array:", nums[:k])
# Output:
# Unique count: 3
# Modified array: [2, 10, 30]
