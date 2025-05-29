"""
Problem: Trapping Rain Water

You are given an array of non-negative integers `height` where each value represents an elevation map bar of width 1.
Return the **maximum amount of water** that can be trapped between the bars after raining.

Example 1:
Input:  height = [0,2,0,3,1,0,1,3,2,1]
Output: 9

Constraints:
- 1 <= height.length <= 1000
- 0 <= height[i] <= 1000

Link: https://leetcode.com/problems/trapping-rain-water/
"""

# -----------------------------
# Brute Force Approach:
# -----------------------------
# For every index, scan left and right to find the highest bar on each side.
# The trapped water at index i is min(left_max, right_max) - height[i] (if positive).
# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution:
    def trap_brute_force(self, height: list) -> int:
        n = len(height)
        if n == 0:
            return 0
        total_water = 0
        for i in range(n):
            left_max = max(height[:i+1])  # max to the left (inclusive)
            right_max = max(height[i:])   # max to the right (inclusive)
            water = min(left_max, right_max) - height[i]
            if water > 0:
                total_water += water
        return total_water

# -----------------------------
# Optimized Two-Pointer / Prefix-Suffix Approach:
# -----------------------------
# Precompute prefix max and suffix max arrays, then calculate trapped water in one pass.
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def trap_prefix_suffix(self, height: list) -> int:
        n = len(height)
        if n == 0:
            return 0

        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])

        right_max[-1] = height[-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])

        total_water = 0
        for i in range(n):
            water = min(left_max[i], right_max[i]) - height[i]
            if water > 0:
                total_water += water
        return total_water

# -----------------------------
# Further Optimized: Two Pointers (O(1) extra space)
# -----------------------------
# Use left and right pointers, and keep track of left_max and right_max as you go.
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def trap(self, height: list) -> int:
        n = len(height)
        if n == 0:
            return 0

        left, right = 0, n - 1
        left_max, right_max = 0, 0
        total_water = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total_water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total_water += right_max - height[right]
                right -= 1
        return total_water

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    height = [0,2,0,3,1,0,1,3,2,1]
    print("Water trapped:", sol.trap(height))  # Output: 9
