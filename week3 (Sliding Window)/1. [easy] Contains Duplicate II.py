"""
Problem: Contains Duplicate II

You are given an integer array `nums` and an integer `k`. Return `True` if there are two distinct indices `i` and `j` in the array such that:

    nums[i] == nums[j] and abs(i - j) <= k

Otherwise, return `False`.

Examples:
Input: nums = [1, 2, 3, 1], k = 3
Output: True       # because nums[0] == nums[3] and |0 - 3| = 3 <= k

Input: nums = [2, 1, 2], k = 1
Output: False      # because the repeated 2s are at index 0 and 2, and |0 - 2| = 2 > k

Constraints:
- 1 <= nums.length <= 100,000
- -10^9 <= nums[i] <= 10^9
- 0 <= k <= 100,000

Link: https://leetcode.com/problems/contains-duplicate-ii/
"""

# -----------------------------
# Brute Force Approach:
# -----------------------------
# Compare every pair of elements (i, j) and check:
#   - nums[i] == nums[j]
#   - abs(i - j) <= k
# This approach is not suitable for large inputs due to O(n^2) time.

class Solution:
    def containsNearbyDuplicate_brute(self, nums: list[int], k: int) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and abs(i - j) <= k:
                    return True
        return False

# Time complexity: O(n^2)
# Space complexity: O(1)


# -----------------------------
# Sliding Window Approach:
# -----------------------------
# Use a set to maintain a window of size <= k.
# As we iterate, we:
#   - Check if current value is already in the window → return True
#   - Add current value to the window
#   - If window size > k, remove the oldest element (nums[L])
# This ensures only values within the k-distance are checked.

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()
        L = 0  # Left boundary of the window

        for R in range(len(nums)):  # R is the current element (right side of window)
            if R - L > k:
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return False

# Time complexity: O(n)
# Space complexity: O(k)

"""
Sliding Window Summary:

- Type: Fixed-size window (at most k elements)
- Condition to check: Is nums[R] already in the window?
- If yes → found duplicate within distance k
- If no → add it, and slide the window when necessary

This problem is often the first step to understanding how a sliding window can **track a condition over a constrained range** (distance, time, size, etc.).
"""
