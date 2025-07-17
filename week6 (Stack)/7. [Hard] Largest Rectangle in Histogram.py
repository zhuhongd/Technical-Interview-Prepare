"""
Problem: Largest Rectangle in Histogram

You are given a list of integers `heights` representing the height of bars in a histogram.
Each bar has a width of 1.

Return the **maximum area** of a rectangle that can be formed using contiguous bars.

Examples:
Input: heights = [7, 1, 7, 2, 2, 4]
Output: 8
    → Bars [3:5] (2, 2, 4) → min height 2 × width 4 = 8

Input: heights = [1, 3, 7]
Output: 7
    → Just the last bar of height 7 and width 1

Approach:
- Use a **monotonic increasing stack**.
- For each bar, keep track of the last bar that was **taller**.
- Whenever the current bar is **shorter** than the stack top, it means we've found the right boundary for the rectangle using that bar.

Key trick: add a trailing `0` to ensure all bars are processed.

https://neetcode.io/problems/largest-rectangle-in-histogram?list=neetcode150
"""

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Append a sentinel value to flush the stack at the end
        heights.append(0)
        stack = []  # stores indices
        max_area = 0

        for i, h in enumerate(heights):
            # Maintain increasing stack
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                # Width is from the previous index in stack to i
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area


# Test case
if __name__ == "__main__":
    heights = [7, 1, 7, 2, 2, 4]
    expected = 8

    output = Solution().largestRectangleArea(heights)
    print(f"Input: {heights}")
    print(f"Output: {output}")
    print(f"Expected: {expected}")
    print("✅ Pass" if output == expected else "❌ Fail")

"""
🧠 Stack Walkthrough (for [7, 1, 7, 2, 2, 4]):

- At each index, we maintain a stack of increasing heights.
- If a lower bar is found, we compute the area of rectangles ending at that point.

Step-by-step:
Input: [7, 1, 7, 2, 2, 4, 0]  ← extra 0 helps flush the stack

0: 7  → push
1: 1  → 1 < 7 → pop 7 → area = 7 * 1 = 7 → push 1
2: 7  → push
3: 2  → 2 < 7 → pop 7 → area = 7 * 1 = 7 → push 2
4: 2  → push
5: 4  → push
6: 0  → flush: pop 4, 2, 2, 1 → max area found = 8

📦 Time Complexity: O(n)
Each bar is pushed and popped at most once.

📦 Space Complexity: O(n)
The stack holds at most n indices.
"""
