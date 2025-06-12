"""
Problem: Minimum Window Substring

Given two strings `s` and `t`, return the **smallest window (substring)** in `s` that contains **all the characters from `t`**, including duplicates.

If there is no valid window, return an empty string "".

Examples:
Input: s = "OUZODYXAZV", t = "XYZ"
Output: "YXAZ"
Explanation: This is the shortest substring of `s` that contains all characters of `t`.

Input: s = "xyz", t = "xyz"
Output: "xyz"

Input: s = "x", t = "xy"
Output: ""

Constraints:
- 1 <= s.length, t.length <= 10^5
- `s` and `t` consist of ASCII characters
- The output is guaranteed to be unique

Link: https://leetcode.com/problems/minimum-window-substring/
"""

# -----------------------------
# Sliding Window + Hash Map Approach:
# -----------------------------
# Use two hash maps:
# - one for the required characters in `t` (with frequency)
# - one for the current window in `s`
# Expand the right pointer to include characters
# Shrink from the left when the window contains all characters in `t`
# Time complexity: O(n)
# Space complexity: O(m + n) where m is len(t), n is len(s)

from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Step 1: Count characters needed from t
        required = Counter(t)   # e.g., t = "XYZ" → {'X':1, 'Y':1, 'Z':1}
        window_counts = defaultdict(int)

        # Step 2: Initialize sliding window pointers
        l = 0  # left pointer
        have = 0  # how many characters we have that meet required frequency
        need = len(required)  # how many unique characters we need to satisfy
        res = [-1, -1]  # placeholder for start and end of best window
        res_len = float("inf")

        # Step 3: Expand the window with the right pointer
        for r in range(len(s)):
            char = s[r]
            window_counts[char] += 1

            # Only count as 'have' when the character matches required frequency
            if char in required and window_counts[char] == required[char]:
                have += 1

            # Step 4: Try to shrink window from left when valid
            while have == need:
                # Update best result if current window is smaller
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                # Shrink from the left
                window_counts[s[l]] -= 1
                if s[l] in required and window_counts[s[l]] < required[s[l]]:
                    have -= 1
                l += 1  # move left pointer forward

        # Step 5: Return result
        start, end = res
        return s[start:end+1] if res_len != float("inf") else ""

"""
Sliding Window Summary:

- Type: Shrinking + Expanding Window
- Goal: Track all required characters and their frequencies from t
- Strategy:
    - Expand right pointer to include more characters
    - Once all required characters are satisfied → try to shrink from left
    - Track the minimum window length that is valid
- Hash maps are used to track what we need vs what we have

Example Walkthrough:
Input: s = "OUZODYXAZV", t = "XYZ"
- Required: {'X':1, 'Y':1, 'Z':1}
- As we slide the window, we track character counts
- When we hit a window like "YXAZ", we check:
    - Does it contain all required characters?
    - Is it smaller than our previous best window?
    - If yes, we update the result

This is one of the most fundamental "sliding window with character count" patterns used in interview questions.
"""
