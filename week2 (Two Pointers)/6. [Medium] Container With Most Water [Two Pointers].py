"""
Problem: Container With Most Water

You are given an integer array `height` where `height[i]` represents the height of the i-th vertical line.
Choose any two lines to form a container, such that it holds the most water between them.

Return the maximum amount of water a container can store.

Link: https://leetcode.com/problems/container-with-most-water/

Examples:

Input: height = [1, 7, 2, 5, 4, 7, 3, 6]
Output: 36

Explanation:
- Try picking the left wall at i=1 (height 7) and right wall at i=6 (height 6):
  Area = min(7,6) * (7-1) = 6 * 6 = 36

Input: height = [2,2,2]
Output: 4
Explanation: pick the ends, area = min(2,2) * (2-0) = 2*2 = 4

Constraints:
- 2 <= height.length <= 1000
- 0 <= height[i] <= 1000
"""

# -----------------------------
# Brute Force Approach (O(n^2)):
# -----------------------------
# For every pair of walls (i, j) where i < j, calculate the area:
#   area = min(height[i], height[j]) * (j - i)
# Track and return the maximum area found.
#
# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution:
    def maxArea_brute_force(self, heights: list) -> int:
        max_area = 0
        n = len(heights)
        for i in range(n):
            for j in range(i+1, n):
                height = min(heights[i], heights[j])
                width = j - i
                area = height * width
                max_area = max(max_area, area)
        return max_area

# Walkthrough for Example 1:
# Input: heights = [1, 7, 2, 5, 4, 7, 3, 6]
# Try all pairs:
# - (i=0, j=7): min(1,6)*7=7
# - (i=1, j=5): min(7,7)*4=28
# - (i=1, j=7): min(7,6)*6=36  <-- best
# - (i=3, j=5): min(5,7)*2=10, etc.
# This approach guarantees the maximum, but is slow.

# -----------------------------
# Optimized Two-Pointer Approach (O(n)):
# -----------------------------
# Start with two pointers, left at 0, right at n-1 (the ends).
# At each step, compute area = min(heights[left], heights[right]) * (right-left).
# Move the pointer pointing to the shorter wall inward, hoping to find a taller wall and potentially more area.
# Repeat until pointers meet.
#
# Why does this work? Moving the shorter wall is the only way to possibly increase the minimum height.
# We never need to check pairs where the width is less but height is not more than before.
#
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxArea(self, heights: list) -> int:
        left = 0
        right = len(heights) - 1
        max_area = 0

        # Walkthrough example on first loop:
        # left=0 (height 1), right=7 (height 6), area=min(1,6)*(7-0)=7
        # height[left]=1 < height[right]=6, so move left += 1
        # left=1 (height 7), right=7 (height 6), area=min(7,6)*6=36 (best so far)
        # Now move right -= 1 (since height[1]=7 > height[7]=6)
        # Continue moving pointers inward until they meet.

        while left < right:
            h = min(heights[left], heights[right])
            w = right - left
            area = h * w
            if area > max_area:
                max_area = area

            # Move the shorter wall
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area

# -----------------------------
# Step-by-step Example
# -----------------------------
# Let's step through the optimized approach on [1, 7, 2, 5, 4, 7, 3, 6]:
#
# 1. left=0 (1), right=7 (6): area = min(1,6)*7 = 7
#    move left (1<6)
# 2. left=1 (7), right=7 (6): area = min(7,6)*6 = 36 <-- max so far!
#    move right (7>6)
# 3. left=1 (7), right=6 (3): area = min(7,3)*5 = 15
#    move right (7>3)
# 4. left=1 (7), right=5 (7): area = min(7,7)*4 = 28
#    move right (still equal so move right)
# ...
# Continue until left meets right.
# Maximum area found: 36.

# -----------------------------
# Example usage
# -----------------------------
if __name__ == "__main__":
    sol = Solution()
    height1 = [1, 7, 2, 5, 4, 7, 3, 6]
    print("Max area (Example 1):", sol.maxArea(height1))  # Output: 36

    height2 = [2, 2, 2]
    print("Max area (Example 2):", sol.maxArea(height2))  # Output: 4

# -----------------------------
# Takeaway
# -----------------------------
# The two-pointer pattern here is about "shrinking the window" between pointers and always moving the smaller wall.
# This is a classic approach for problems involving maximizing/minimizing something between two ends (often sorted or spatial data).
