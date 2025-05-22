"""
Palindrome Practice

The point of this warm up is to get familar with Two Pointers. [Knowledge 1.]

is file contains two versions of the palindrome problem to help practice the two-pointer technique.

1. Basic Palindrome Checker (warm-up)
2. Valid Palindrome (LeetCode #125 - real-world version with cleanup)

These problems help solidify the fundamentals of moving pointers inward, character comparison,
and transitioning from basic to more realistic inputs.
"""

from typing import List

# -------------------------------------------------------
# ✅ Warm-Up Question: Basic Palindrome Check (Two Pointers)
# -------------------------------------------------------

def is_simple_palindrome(s: str) -> bool:
    """
    Given a lowercase string with no punctuation or spaces,
    return True if it is a palindrome.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

"""
Example:
- Input: "abcba" → True
- Input: "abddba" → False

Time Complexity: O(n)
Space Complexity: O(1)

This warm-up helped me understand:
- How to use two pointers (left/right)
- When to stop: left < right
- How to compare characters efficiently
"""