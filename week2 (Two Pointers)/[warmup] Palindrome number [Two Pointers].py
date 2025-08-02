"""
Palindrome Number (LeetCode #9) — EECS4070 Writeup

Warm-up goal
------------
This is a gentle warm-up to get familiar with the "two-pointer" idea:
compare from both ends and meet in the middle.

Problem
-------
Given an integer x, return True if x is a palindrome and False otherwise.
A palindrome reads the same forward and backward.

Important quick facts:
- Negative numbers are NOT palindromes (a minus sign only appears on the left).
- Numbers ending in 0 (but not 0 itself) are NOT palindromes (because there'd have to be a leading 0).
- Single-digit numbers are always palindromes.

Examples
--------
x = 121   -> True
x = -121  -> False
x = 10    -> False
x = 0     -> True

Constraints
-----------
-2^31 <= x <= 2^31 - 1

Link: https://leetcode.com/problems/palindrome-number/
"""

# ============================================================
# ✅ Active Solution: String + Two Pointers (Beginner-friendly)
# ============================================================
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         """
#         Intuition (like checking letters in a word):
#         - Turn the number into a string of digits.
#         - Compare the leftmost and rightmost characters.
#         - Move inward until they cross.

#         Why it works:
#         - A palindrome must match in mirrored positions. If any pair differs, it's not a palindrome.
#         - Negative numbers fail early (we can check before converting).
#         """
#         # Rule-out: negative numbers are not palindromes.
#         if x < 0:
#             return False

#         s = str(x)
#         left, right = 0, len(s) - 1

#         while left < right:
#             if s[left] != s[right]:
#                 return False
#             left += 1
#             right -= 1

#         return True


# ====================================================================
# (Optional) Alternative: No string conversion (reverse HALF the number)
# --------------------------------------------------------------------
# How it works:
#   We peel digits from the RIGHT of x and build a number `reverted` from those digits.
#   After each peel:
#       - x loses its last digit  (x //= 10)
#       - reverted gains that digit at its end (reverted = reverted*10 + last_digit)
#   We stop when reverted >= x, meaning we've processed half the digits.
#   Then:
#       - For even # of digits: left half == right half reversed  → x == reverted
#       - For odd  # of digits: ignore the middle digit          → x == reverted // 10
#
# Why these early exits?
#   - x < 0                        : a minus sign only appears on the left; not symmetric
#   - x % 10 == 0 and x != 0       : ends with 0 but isn't 0 itself → can't mirror to a valid leading 0
#
# Dry runs:
#   1221 -> (x,reverted): (1221,0)->(122,1)->(12,12) stop → 12==12 → True
#   12321-> (x,reverted): (12321,0)->(1232,1)->(123,12)->(12,123) stop → 12 == 123//10 → True

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted = 0
        # Build the reversed right half until it's >= the left half.
        while x > reverted:
            reverted = reverted * 10 + (x % 10)
            x //= 10

        # Even length: x == reverted
        # Odd length : x == reverted // 10 (middle digit ignored)
        return x == reverted or x == reverted // 10


# -----------------------------
# 🧪 Inline tests (comprehensive)
# -----------------------------
def _run_tests() -> None:
    sol = Solution().isPalindrome

    # (x, expected, label)
    TESTS = [
        # From prompt
        (121, True,  "example: 121"),
        (-121, False, "example: -121"),
        (10, False,  "example: 10"),
        (0, True,    "example: 0"),

        # Single and small
        (1, True, "single 1"),
        (7, True, "single 7"),
        (11, True, "two-digit palindrome"),
        (12, False, "two-digit non-palindrome"),

        # Even digit palindromes
        (1221, True, "even digits 1221"),
        (1001, True, "even digits 1001"),
        (1331, True, "even digits 1331"),

        # Odd digit palindromes
        (12321, True, "odd digits 12321"),
        (10101, True, "odd digits 10101"),

        # Clear non-palindromes
        (123, False, "123 not palindrome"),
        (100, False, "100 ends with 0"),
        (1000000000, False, "large ending zero (not zero itself)"),

        # Edge-y within 32-bit range
        (2147447412, True,  "near 32-bit palindrome"),
        (2147483647, False, "max 32-bit int not palindrome"),

        # Negatives and tricky
        (-101, False, "negative not palindrome"),
        (1000021, False, "mismatch middle"),
    ]

    passed = 0
    for i, (x, expected, label) in enumerate(TESTS, 1):
        got = sol(x)
        ok = (got == expected)
        passed += ok
        print(f"[{i:02d}] {label:>26}  x={x:<11} -> got={got} expected={expected} | {'✅' if ok else '❌'}")

    print(f"\nPassed {passed}/{len(TESTS)} tests.")


if __name__ == "__main__":
    _run_tests()
