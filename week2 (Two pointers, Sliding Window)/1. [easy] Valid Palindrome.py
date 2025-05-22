"""
Valid Palindrome 

Problem:
--------
Given a string `s`, return `True` if it is a palindrome, `False` otherwise.

A palindrome is a string that reads the same forward and backward.
This version of the problem requires:
- Case insensitivity
- Ignoring all non-alphanumeric characters

Examples:
---------
Input:  "Was it a car or a cat I saw?"
Output: True

Explanation:
Alphanumeric version: "wasitacaroracatisaw"

Input:  "tab a cat"
Output: False

Explanation:
Alphanumeric version: "tabacat" is not the same reversed

Constraints:
------------
- 1 <= s.length <= 1000
- s consists only of printable ASCII characters

link: https://neetcode.io/problems/is-palindrome

"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Use two pointers to compare characters from both ends,
        skipping non-alphanumerics and treating letters as lowercase.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            # Skip non-alphanumeric characters
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare lowercase characters
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

"""
Approach:
---------
- Clean up while comparing: only consider alphanumeric characters
- Move left and right pointers inward
- Compare characters in lowercase for case insensitivity

Time Complexity: O(n)
- Each character is visited at most once

Space Complexity: O(1)
- Constant space used (no extra storage)

Common Mistakes:
----------------
❌ Forgetting to convert characters to lowercase
❌ Not skipping non-alphanumeric characters (like spaces and punctuation)
✅ This method avoids creating a new string — it's efficient and scalable

This implementation is part of the EECS4070 Directed Study project by Hongda Zhu.
"""