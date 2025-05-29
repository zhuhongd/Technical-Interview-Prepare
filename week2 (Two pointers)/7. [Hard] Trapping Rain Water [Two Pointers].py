"""
Problem: Trapping Rain Water

Level: Medium
Link: https://leetcode.com/problems/trapping-rain-water/

-------------------------------------------
Purpose:
-------------------------------------------
This problem tests your ability to reason about "how much space is left" in a set of vertical bars (like a histogram).
It’s one of the best real-world style questions for:
- Thinking visually
- Using auxiliary arrays (prefix/suffix)
- Recognizing opportunities to optimize to O(1) space

**Interviewers love this problem** because it's about:
- Realizing you must check BOTH the tallest wall to the left and the tallest to the right
- Writing a clean, bug-free implementation

-------------------------------------------
Problem Statement:
-------------------------------------------
You are given an array of non-negative integers `height` where each value represents an elevation map bar of width 1.
Return the **maximum amount of water** that can be trapped after raining.

Example:
Input:  height = [0,2,0,3,1,0,1,3,2,1]
Output: 9

Visual:
|   |   |   | # |   |   |   | # |   |   |
|   | # |   | # |   |   |   | # | # |   |
|   | # |   | # |   |   |   | # | # | # |
| # | # | # | # | # | # | # | # | # | # |
-------------------------------------------
Explanation:
- Water can only be held if there is a taller (or equal) wall on both sides.
- For each position, trapped water = min(max_left, max_right) - height[i] (if positive).

Constraints:
- 1 <= height.length <= 1000
- 0 <= height[i] <= 1000

-------------------------------------------
Approach 1: Brute Force (For Loop on Each Bar)
-------------------------------------------
For each bar, scan to the left and right to find the highest wall.
Then calculate water at that bar: min(left_max, right_max) - height[i].

Time Complexity: O(n^2) -- slow for big input!
Space Complexity: O(1)
"""

class Solution:
    def trap_brute_force(self, height: list) -> int:
        n = len(height)
        total_water = 0
        for i in range(n):
            left_max = max(height[:i+1])    # Tallest to the left (inclusive)
            right_max = max(height[i:])     # Tallest to the right (inclusive)
            trapped = min(left_max, right_max) - height[i]
            if trapped > 0:
                total_water += trapped
        return total_water

"""
-------------------------------------------
Approach 2: Prefix & Suffix Arrays (Prefix/Suffix Maximums)
-------------------------------------------
We can do better by precomputing, in O(n) time, the tallest wall to the left and right for every bar.

- Build left_max[i]: max height to the left of i (inclusive)
- Build right_max[i]: max height to the right of i (inclusive)
- For each bar, water = min(left_max[i], right_max[i]) - height[i]

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def trap_prefix_suffix(self, height: list) -> int:
        n = len(height)
        if n == 0:
            return 0

        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        total_water = 0
        for i in range(n):
            trapped = min(left_max[i], right_max[i]) - height[i]
            if trapped > 0:
                total_water += trapped
        return total_water

"""
-------------------------------------------
Approach 3: Optimized Two Pointer Approach (O(1) space)
-------------------------------------------
The "aha moment" is: as you walk in from both ends, always process the LOWER wall.
If height[left] < height[right]:
    If height[left] >= left_max: update left_max
    Else: trapped = left_max - height[left]
    left += 1
Else:
    If height[right] >= right_max: update right_max
    Else: trapped = right_max - height[right]
    right -= 1

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def trap(self, height: list) -> int:
        n = len(height)
        left, right = 0, n - 1
        left_max, right_max = 0, 0
        total_water = 0

        while left < right:
            # Always move pointer at smaller wall inward
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

"""
-------------------------------------------
Step-by-Step Walkthrough for Beginners:
-------------------------------------------
Suppose height = [0,2,0,3,1,0,1,3,2,1]

- At each index, ask:
    What's the tallest wall on my left? What's the tallest on my right?
    What's the minimum of these two heights? How much higher is that than my own height?
    That's how much water sits above me.

For index 2 (height=0):
    left_max = max(0,2,0) = 2
    right_max = max(0,3,1,0,1,3,2,1) = 3
    Water = min(2,3) - 0 = 2

For index 5 (height=0):
    left_max = max(0,2,0,3,1,0) = 3
    right_max = max(0,1,3,2,1) = 3
    Water = min(3,3) - 0 = 3

Add all such positions. Answer: 9.

-------------------------------------------
Key Interview Purpose:
-------------------------------------------
- Practice thinking in "prefix/suffix" and "sliding window" ways.
- Optimize brute force with smart pre-processing or pointer tricks.
- Clear logic and avoiding fencepost/off-by-one errors is critical.
- Think visually and draw example arrays—this really helps!

-------------------------------------------
Example usage:
-------------------------------------------
"""
if __name__ == "__main__":
    sol = Solution()
    height = [0,2,0,3,1,0,1,3,2,1]
    print("Water trapped:", sol.trap(height))  # Output: 9
