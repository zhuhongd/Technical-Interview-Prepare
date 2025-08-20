"""
Problem: Longest Substring Without Repeating Characters (week 04)

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

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # solution here

        return

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