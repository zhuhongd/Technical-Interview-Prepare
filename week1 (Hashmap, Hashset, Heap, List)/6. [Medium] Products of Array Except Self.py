"""
Product of Array Except Self - EECS4070 Writeup

Problem:
---------
Given an integer array `nums`, return an array `output` such that:
    output[i] = product of all elements of nums except nums[i].

You must solve it in O(n) time **without using division**.

Examples:
---------
Input:  nums = [1, 2, 4, 6]
Output: [48, 24, 12, 8]

Input:  nums = [-1, 0, 1, 2, 3]
Output: [0, -6, 0, 0, 0]

Constraints:
------------
- 2 <= nums.length <= 1000
- -20 <= nums[i] <= 20
- Result will fit in a 32-bit integer

-----------------------------------------------------------
Approach: Prefix and Suffix Multiplication (O(n), no division) 
-----------------------------------------------------------
Key Idea:
- For each index i, the result is:
    result[i] = product of all elements to the **left** of i
                × product of all elements to the **right** of i

We use two passes:
1. First pass (left to right): fill in prefix products
2. Second pass (right to left): multiply with suffix products
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        # Step 1: prefix products
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # Step 2: suffix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result

"""
Time Complexity: O(n)
 - Two linear passes: one for prefix, one for suffix

Space Complexity: O(1) extra (excluding output array)
 - We only use two variables (prefix, suffix), and reuse output list

Common Mistakes:
----------------
❌ Using division (not allowed in follow-up)
❌ Incorrect prefix/suffix updates: be sure to update AFTER assigning to result[i]

Interview Tip:
--------------
This problem is a great example of space/time tradeoffs, and shows mastery of linear-time array transformations.

This explanation is part of the EECS4070 Directed Study project by Hongda Zhu.
"""