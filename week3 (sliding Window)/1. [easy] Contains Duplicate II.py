"""
Problem: Contains Duplicate II

You are given an integer array nums and an integer k.
Return True if there are two distinct indices i and j in the array such that:
    nums[i] == nums[j] and abs(i - j) <= k,
otherwise return False.

Examples:
Input: nums = [1,2,3,1], k = 3
Output: True

Input: nums = [2,1,2], k = 1
Output: False

Constraints:
- 1 <= nums.length <= 100,000
- -1,000,000,000 <= nums[i] <= 1,000,000,000
- 0 <= k <= 100,000

Link: https://leetcode.com/problems/contains-duplicate-ii/
"""

# -----------------------------
# Brute Force Approach:
# -----------------------------
# Compare every pair (i, j) with i != j and abs(i - j) <= k.
# Time complexity: O(n * k)
# Space complexity: O(1)

class Solution:
    def containsNearbyDuplicate_brute_force(self, nums: list, k: int) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, min(i + k + 1, n)):
                if nums[i] == nums[j]:
                    return True
        return False

# -----------------------------
# Optimized Sliding Window Approach (Set):
# -----------------------------
# Maintain a sliding window of at most k previous elements using a set.
# For each new element, check if it is already in the set (window).
# Time complexity: O(n)
# Space complexity: O(k)

class Solution:
    def containsNearbyDuplicate(self, nums: list, k: int) -> bool:
        window = set()
        for i in range(len(nums)):
            if nums[i] in window:
                return True
            window.add(nums[i])
            if len(window) > k:
                window.remove(nums[i - k])
        return False

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.containsNearbyDuplicate([1,2,3,1], 3))  # Output: True
    print(sol.containsNearbyDuplicate([2,1,2], 1))    # Output: False
