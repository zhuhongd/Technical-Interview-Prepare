"""
Problem: Valid Anagram

Given two strings s and t, return True if t is an anagram of s, and False otherwise.

Definition:
An anagram is a word or phrase formed by rearranging the letters of another — 
using all the original letters exactly once.

Examples:
Input: s = "racecar", t = "carrace"
Output: True

Input: s = "jar", t = "jam"
Output: False

Constraints:
- s and t consist of lowercase English letters only.

Link: https://neetcode.io/problems/is-anagram
"""

# Approach:
# Step 1: Check if the strings have the same length.
#         If not, they can't be anagrams, so we return False immediately.
#
# Step 2: Create two dictionaries to count the frequency of each character
#         in both strings.
#
# Step 3: Compare the two dictionaries.
#         If they are identical, the strings are anagrams.

# Why use dictionaries?
# Dictionary operations (like get and assignment) are O(1) on average.
# So even though we're looping through both strings, the total time complexity is O(n).

# [Knowledge 2.] Using a.get(key, 0) is a common Python trick to simplify frequency counting:
# Instead of writing:
#     if char not in d:
#         d[char] = 1
#     else:
#         d[char] += 1
# You can write:
#     d[char] = d.get(char, 0) + 1

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Step 1: Check if lengths are different — early return
        if len(s) != len(t):
            return False

        # Step 2: Count character frequencies for both strings
        freq_s = {}
        freq_t = {}

        for char in s:
            freq_s[char] = freq_s.get(char, 0) + 1   # [Knowledge 2.]

        for char in t:
            freq_t[char] = freq_t.get(char, 0) + 1

        # Step 3: Compare dictionaries
        return freq_s == freq_t
