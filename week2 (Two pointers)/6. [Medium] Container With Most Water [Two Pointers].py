# Create Python file content for the problem "Container With Most Water"

"""
Problem: Container With Most Water

You are given an integer array `height` where `height[i]` represents the height of the i-th vertical line.
Choose any two lines to form a container, such that it holds the most water between them.

Return the maximum amount of water a container can store.

Examples:
Input: height = [1,7,2,5,4,7,3,6]
Output: 36

Input: height = [2,2,2]
Output: 4

Constraints:
- 2 <= height.length <= 1000
- 0 <= height[i] <= 1000

Link: https://leetcode.com/problems/container-with-most-water/
"""

# -----------------------------
# Brute Force Approach:
# -----------------------------
# Check the area formed between every pair of lines.
# Area = min(height[i], height[j]) * (j - i)
# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution:
    def maxArea_brute_force(self, height: list) -> int:
        max_area = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                area = min(height[i], height[j]) * (j - i)
                max_area = max(max_area, area)
        return max_area


# -----------------------------
# Optimized Two-Pointer Approach:
# -----------------------------
# Start with two pointers at the ends and move the shorter line inward.
# This guarantees we consider the widest container first, and only move inwards.
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def maxArea(self, height: list) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            area = h * w
            max_area = max(max_area, area)

            # Move the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# Example usage:
if __name__ == "__main__":
    sol = Solution()
    height1 = [1, 7, 2, 5, 4, 7, 3, 6]
    print("Max area (Example 1):", sol.maxArea(height1))  # Output: 36

    height2 = [2, 2, 2]
    print("Max area (Example 2):", sol.maxArea(height2))  # Output: 4


# Save the file
path = "/mnt/data/container_with_most_water.py"
with open(path, "w") as f:
    f.write(container_water_py)

path
