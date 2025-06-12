"""
Problem: Longest Substring Without Repeating Characters

Given a string `s`, return the length of the **longest substring** without repeating characters.

A substring is a contiguous sequence of characters within the string.

Examples:
Input: s = "zxyzxyz"
Output: 3
Explanation: The longest substrings without duplicates are "zxy", "xyz", etc. Length = 3.

Input: s = "xxxx"
Output: 1
Explanation: The longest substring without duplicates is "x".

Constraints:
- 0 <= s.length <= 1000
- s may consist of printable ASCII characters

Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

# -----------------------------
# Brute Force Approach:
# -----------------------------
# Try every possible substring and check if it has all unique characters.
# Time complexity: O(n^3) — generate all substrings (O(n^2)) and check for uniqueness (O(n))
# Space complexity: O(n) — for the substring set

class Solution:
    def lengthOfLongestSubstring_brute(self, s: str) -> int:
        n = len(s)
        max_len = 0

        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break
                seen.add(s[j])
                max_len = max(max_len, j - i + 1)

        return max_len


# -----------------------------
# Optimized Sliding Window Approach:
# -----------------------------
# Use a hash set to track characters in the current window.
# Expand the right pointer to grow the window.
# Shrink the left pointer when we hit a duplicate.
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len

"""
Sliding Window Summary:

- Type: Dynamic window size (grow/shrink based on character repetition)
- Goal: Maintain a window where all characters are unique
- Shrink: If duplicate found, move left pointer and remove from set until the duplicate is gone
- Expand: Always move right pointer and add to set

This is a classic problem that introduces the **"grow and shrink" sliding window pattern**, often used in string and substring problems.
"""
