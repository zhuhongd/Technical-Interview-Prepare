"""
Palindrome Number (LeetCode #9)

This is a warm up for you to get familar with two pointer.
I dont think such easy questions will come up during interview, so I put it as warm up.

Problem:
---------
Given an integer x, return True if x is a palindrome, and False otherwise.

A palindrome reads the same forward and backward.  
Negative numbers and numbers ending in 0 (but not 0 itself) cannot be palindromes.

Examples:
---------
Input: 121
Output: True

Input: -121
Output: False

Input: 10
Output: False

Constraints:
------------
- -2^31 <= x <= 2^31 - 1

link: https://leetcode.com/problems/palindrome-number/
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False

        # Convert the number to a string and use two pointers
        s = str(x)
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

"""
Approach:
---------
- Convert the integer to a string
- Use two pointers to compare digits from both ends
- Return False if any pair doesn't match

Time Complexity: O(n)
- n is the number of digits in x

Space Complexity: O(n)
- String conversion creates a copy of the digits

Alternative:
------------
You can also solve this without converting to a string, by reversing half the number and comparing it.

This implementation is part of the EECS4070 Directed Study project by Hongda Zhu.
"""

# 🧪 Test Cases
if __name__ == "__main__":
    sol = Solution()

    print(sol.isPalindrome(121))    # True
    print(sol.isPalindrome(-121))   # False
    print(sol.isPalindrome(10))     # False
    print(sol.isPalindrome(0))      # True
    print(sol.isPalindrome(1221))   # True
