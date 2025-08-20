"""
Problem: Longest Repeating Character Replacement

You are given a string `s` consisting of only uppercase English letters and an integer `k`. 
You can choose at most `k` characters in the string to replace with any other uppercase letter.

Return the length of the **longest substring** that can be obtained such that all characters in the substring are the **same** after at most `k` replacements.

Examples:
Input: s = "XYYX", k = 2
Output: 4
Explanation: Replace both 'X's with 'Y's or both 'Y's with 'X's → "YYYY" or "XXXX"

Input: s = "AAABABB", k = 1
Output: 5
Explanation: Replace one 'B' with 'A' → "AAAABB" or "AAAAAB"

Constraints:
- 1 <= s.length <= 1000
- 0 <= k <= s.length

Link: https://leetcode.com/problems/longest-repeating-character-replacement/
"""

# -----------------------------
# Optimized Sliding Window Approach:
# -----------------------------
# Goal: Maintain a window where at most k characters need to be changed to make all characters the same.
# Strategy:
#   - Use a sliding window to track the count of each character.
#   - At every step, we only care about the most frequent character in the window.
#   - If the remaining characters (window size - max_freq) > k, shrink the window.
# Time complexity: O(n)
# Space complexity: O(1) since there are only 26 uppercase letters.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict

        # Frequency map to count characters in current window
        count = defaultdict(int)
        
        left = 0  # Left pointer of the sliding window
        max_freq = 0  # Track the max frequency of any single character in the window
        max_len = 0   # Result variable

        # Expand the window with the right pointer
        for right in range(len(s)):
            count[s[right]] += 1  # Add current character to the count map

            # Update max_freq with the most frequent character count so far
            max_freq = max(max_freq, count[s[right]])

            # If the number of characters to change exceeds k, shrink window
            # Total chars to change = window size - max_freq
            while (right - left + 1) - max_freq > k:
                # Before shrinking, reduce the count of the character at the left
                count[s[left]] -= 1
                left += 1  # Move window start to the right

            # Update the max length of valid window found so far
            max_len = max(max_len, right - left + 1)

        return max_len

"""
Sliding Window Summary:

- Type: Expand/Shrink (dynamic-sized window)
- Purpose: Find longest substring where all characters are the same after at most k replacements
- Key Insight: The optimal choice is always to make all characters match the one that appears most frequently in the window.
- Condition: If (window length - max_freq) > k → shrink the window from the left
- Final Answer: Max valid window size during the process

Detailed Example:

Input: "AAABABB", k = 1
Steps:
- Initial window: "AAABA" → counts: {'A': 4, 'B': 1}, max_freq = 4 → window valid (5 - 4 <= 1)
- Add 'B': "AAABAB" → counts: {'A': 3, 'B': 2}, max_freq = 4 → window valid (6 - 4 <= 1)
- Add 'B': "AAABABB" → counts: {'A': 3, 'B': 3}, max_freq = 4 → (7 - 4 = 3 > k) → shrink
→ Slide window to "AABABB" → window size = 5 → valid again

This problem teaches how to combine frequency tracking and window resizing to meet a tolerance constraint (at most k changes).
"""
# -----------------------------
# Comprehensive offline tests
# -----------------------------
def _preview_s(s: str, max_len: int = 40) -> str:
    """Safe preview for long strings in test logs."""
    n = len(s)
    if n <= max_len:
        return repr(s)
    head = s[: max_len // 2]
    tail = s[-(max_len // 2):]
    return repr(head + "…" + tail) + f" (len={n})"

def _run_tests():
    f = Solution().characterReplacement
    TESTS = [
        # Prompt-style examples
        ("XYYX", 2, 4, "flip-both-ends"),
        ("AAABABB", 1, 5, "one-change-length-5"),

        # Classic LC samples
        ("ABAB", 2, 4, "all-into-A"),
        ("AABABBA", 1, 4, "lc-classic-1"),
        ("AAAA", 2, 4, "already-uniform"),
        ("ABCDE", 1, 2, "strictly-increasing"),

        # Edge & small
        ("A", 0, 1, "single-char"),
        ("A", 1, 1, "single-char-with-k"),
        ("", 0, 0, "empty-string"),
        ("B", 0, 1, "one-letter-k0"),

        # Alternating patterns
        ("XYXYXY", 0, 1, "alternating-k0"),
        ("XYXYXY", 1, 3, "alternating-k1"),
        ("XYXYXY", 2, 5, "alternating-k2"),
        ("XYXYXY", 3, 6, "alternating-k3"),

        # Runs with a strong majority
        ("AAAABBBBBAA", 1, 6, "majority-1"),
        ("BAAAB", 2, 5, "make-all-A"),

        # Repeats with multiple options
        ("QWERTY", 2, 3, "distinct-letters-small-k"),
        ("QQWWEERRTT", 2, 4, "pairs-with-k2"),
        ("QQWWEERRTT", 4, 6, "pairs-with-k4"),

        # Long repeating blocks
        ("ABBB", 2, 4, "expand-to-all"),
        ("AABBBCC", 1, 4, "limited-one-change"),
        ("AABBBCC", 2, 5, "two-changes-better"),

        # Stress-like (not too long in console)
        ("ABCDE" * 50, 5, 7, "long-pattern-small-k"),
    ]

    passed = 0
    for i, (s, k, expected, label) in enumerate(TESTS, 1):
        got = f(s, k)
        ok = (got == expected)
        passed += ok
        print(f"[{i:02d}][{label:<22}] s={_preview_s(s):<42} k={k:<2} -> got={got:<2} expected={expected:<2} | {'✅' if ok else '❌'}")

    print(f"\nPassed {passed}/{len(TESTS)} tests.")

if __name__ == "__main__":
    _run_tests()
