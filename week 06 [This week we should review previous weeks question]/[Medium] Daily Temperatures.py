"""
Problem: Daily Temperatures (week 06)

Given a list of daily temperatures, return a list where each element represents
the number of days to wait until a warmer temperature.

If there is no future day with a warmer temperature, use 0 for that day.

Example:
    Input:  [30, 38, 30, 36, 35, 40, 28]
    Output: [1, 4, 1, 2, 1, 0, 0]
    Explanation:
        Day 0 → wait 1 day (38)
        Day 1 → wait 4 days (40)
        Day 2 → wait 1 day (36)
        Day 3 → wait 2 days (40)
        Day 4 → wait 1 day (40)
        Day 5 → no warmer day
        Day 6 → no warmer day
"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # your solution here
        return


# Test the example
if __name__ == "__main__":
    temps = [30, 38, 30, 36, 35, 40, 28]
    expected = [1, 4, 1, 2, 1, 0, 0]

    output = Solution().dailyTemperatures(temps)
    print(f"Input: {temps}")
    print(f"Output: {output}")
    print(f"Expected: {expected}")
    print("✅ Pass" if output == expected else "❌ Fail")

"""
🔍 How the Monotonic Stack Works:

The stack stores indices (and values) of unresolved temperatures.
We iterate from left to right, and for each temperature:
- If it's higher than what’s on top of the stack, it resolves that prior index.
- Otherwise, we push it onto the stack and wait for a warmer day in the future.

Example Walkthrough:
Input: [30, 38, 30, 36, 35, 40, 28]
Stack Evolves:
[(0,30)]
→ [1] is 38 > 30 → pop (0), result[0] = 1
→ push (1,38)
→ (2,30) pushed
→ 36 > 30 → pop (2), result[2] = 1
→ and so on...

📦 Time Complexity: O(n)
Each index is pushed and popped at most once from the stack.

📦 Space Complexity: O(n)
Stack may grow to hold all elements if no warmer temps appear.
"""
