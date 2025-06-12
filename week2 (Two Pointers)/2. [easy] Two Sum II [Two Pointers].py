"""
Two Sum II – Input Array Is Sorted (LeetCode #167) - EECS4070

Problem:
---------
Given a sorted array of integers `numbers`, return the 1-indexed positions [index1, index2] 
of two numbers such that they add up to a given `target`.

Constraints:
- The input array is sorted in non-decreasing order
- Exactly one solution exists
- Must use O(1) additional space
- Cannot use the same element twice (index1 < index2)

Examples:
---------
Input: numbers = [1, 2, 3, 4], target = 3
Output: [1, 2]

Explanation:
1 + 2 = 3, and since it's 1-indexed, return [1, 2]

Link: https://neetcode.io/problems/two-integer-sum-ii
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]  # 1-indexed
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        # According to the problem, there will always be one valid answer
        return []

"""
Approach:
---------
- Initialize two pointers: left at the start, right at the end
- If the sum is less than target, move left forward
- If the sum is more than target, move right backward
- If the sum equals target, return the 1-indexed positions

Time Complexity: O(n)
- Each element is visited at most once

Space Complexity: O(1)
- No extra space is used aside from two pointers

Why This Problem Matters:
-------------------------
This is a classic use case for the two-pointer technique on a sorted array.
It reinforces the pattern of narrowing down the range from both ends to find a match.

This implementation is part of the EECS4070 Directed Study project by Hongda Zhu.
"""
