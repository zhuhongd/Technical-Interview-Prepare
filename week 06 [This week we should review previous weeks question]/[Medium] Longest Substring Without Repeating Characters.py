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
# -----------------------------
# Comprehensive offline tests
# -----------------------------
def _preview_s(s: str, max_len: int = 30) -> str:
    """Safe preview for strings; shows head/tail if very long."""
    n = len(s)
    if n <= max_len:
        return repr(s)
    head = s[: max_len // 2]
    tail = s[-(max_len // 2) :]
    return repr(head + "…" + tail) + f" (len={n})"

def _run_tests():
    sol = Solution().lengthOfLongestSubstring
    TESTS = [
        # Provided-style
        ("zxyzxyz", 3, "rotating-zxy"),
        ("xxxx", 1, "all-same"),
        ("", 0, "empty"),
        (" ", 1, "single-space"),

        # Classic LC
        ("abcabcbb", 3, "abcabcbb"),
        ("bbbbb", 1, "bbbbb"),
        ("pwwkew", 3, "pwwkew"),
        ("dvdf", 3, "dvdf"),
        ("abba", 2, "abba"),
        ("tmmzuxt", 5, "tmmzuxt"),
        ("anviaj", 5, "anviaj"),
        ("au", 2, "au"),
        ("aab", 2, "aab"),

        # Mixed punctuation / digits
        ("a1!a2@", 5, "letters-digits-punct"),      # "1!a2" length 4
        ("1234567890", 10, "digits-unique"),

        # Long unique then repeat
        ("abcdefgxyzabc", 10, "long-unique-then-repeat"),

        # Repeats spaced out
        ("abcaefghibjklmno", 14, "repeats-spaced-out"),  # "caefghibjklm" length 12

        # Larger constructed cases
        ("abcdefghijklmnopqrstuvwxyz", 26, "all-26-unique"),
        ("abcde" * 200, 5, "long-repeating-pattern"),    # repeats every 5
    ]

    passed = 0
    for i, (s, expected, label) in enumerate(TESTS, 1):
        got = sol(s)
        ok = (got == expected)
        passed += ok
        print(f"[{i:02d}][{label:<24}] s={_preview_s(s):<40} -> got={got:<2} expected={expected:<2} | {'✅' if ok else '❌'}")

    print(f"\nPassed {passed}/{len(TESTS)} tests.")

if __name__ == "__main__":
    _run_tests()