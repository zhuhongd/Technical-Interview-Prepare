"""
Valid Palindrome — EECS4070 (Explained, Single Active Solution)

Goal
----
Return True if a string `s` is a palindrome **after**:
  • Ignoring all non-alphanumeric characters (spaces, commas, punctuation, …)
  • Treating letters case-insensitively (A == a)

Key Examples
------------
"Was it a car or a cat I saw?" -> True   (filtered: "wasitacaroracatisaw")
"tab a cat"                    -> False  (filtered: "tabacat" != reverse)

Why Two Pointers?
-----------------
We compare characters from both ends and move toward the middle.
But we must *skip* any character that is not a letter or digit. So:

  left -> moves forward until it lands on an alphanumeric character
  right <- moves backward until it lands on an alphanumeric character
  compare lowercase(left) vs lowercase(right). If they differ -> not a palindrome.
  otherwise move inward (left += 1, right -= 1) and continue.

This avoids building a filtered copy of the string (saves memory).

Complexity
----------
Time:  O(n)   — each character is looked at at most once by either pointer.
Space: O(1)   — we don’t build a filtered string; we only keep a few indices.

Common Pitfalls We Avoid
------------------------
• Forgetting to lowercase before comparison
• Not skipping punctuation/whitespace
• Building a new filtered string when the in-place two-pointer scan is enough

Teaching Analogy (Quick Visual)
-------------------------------
Imagine the string printed on a banner. You stand with a friend:
- you at the left edge, friend at the right edge.
- You each step inward, but you **step over** any non-letter/digit glyphs you see.
- When you both land on letters/digits, you read them out (lowercased).
- If your reads ever disagree, it’s not a palindrome.
- If you pass each other without a disagreement, it *is* a palindrome.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Two-pointer palindrome check with in-place skipping.

        Step-by-step logic:
          1) Initialize two indices: left at start, right at end.
          2) Move `left` forward until s[left] is alphanumeric (or left >= right).
          3) Move `right` backward until s[right] is alphanumeric (or left >= right).
          4) Compare lowercased characters. If different -> False.
          5) Otherwise move inward and repeat.
          6) If pointers cross without mismatch -> True.
        """
        left, right = 0, len(s) - 1

        while left < right:
            # 2) Advance left to next alphanumeric
            while left < right and not s[left].isalnum():
                left += 1
            # 3) Retreat right to previous alphanumeric
            while left < right and not s[right].isalnum():
                right -= 1

            # 4) Compare case-insensitively
            if s[left].lower() != s[right].lower():
                return False

            # 5) Move both pointers inward
            left += 1
            right -= 1

        # 6) No mismatches found
        return True


# ============================================================
# (Optional) Pointer Trace — for classroom/demo (toggle flag)
# ============================================================
TRACE_ENABLED = False  # set to True to see how pointers move on a sample

def _trace_example(sample: str):
    if not TRACE_ENABLED:
        return
    sol = Solution()
    left, right = 0, len(sample) - 1
    print("\n[Pointer Trace]")
    print(f"Input: {repr(sample)}")
    while left < right:
        while left < right and not sample[left].isalnum():
            print(f" skip L {left}:{repr(sample[left])}")
            left += 1
        while left < right and not sample[right].isalnum():
            print(f" skip R {right}:{repr(sample[right])}")
            right -= 1
        print(f" cmp  L {left}:{repr(sample[left]).lower()}  vs  R {right}:{repr(sample[right]).lower()}")
        if sample[left].lower() != sample[right].lower():
            print("  -> mismatch -> False")
            return
        left += 1
        right -= 1
    print("  -> pointers crossed -> True")


# -----------------------------
# 🧪 Inline tests (single solution)
# -----------------------------
def _run_tests() -> None:
    sol = Solution().isPalindrome

    # Each test: (input_string, expected_bool, label)
    TESTS = [
        # Prompt examples
        ("Was it a car or a cat I saw?", True,  "example-true"),
        ("tab a cat",                    False, "example-false"),

        # Classic & common
        ("A man, a plan, a canal: Panama", True,  "classic-true"),
        ("race a car",                      False, "classic-false"),
        ("No 'x' in Nixon",                 True,  "mixed-case-punct"),

        # Numbers and mixes
        ("12321", True,  "numeric-palindrome"),
        ("1231",  False, "numeric-non-pal"),
        ("0P",    False, "zero-vs-letter"),

        # Only punctuation/spaces -> True (filters to empty string)
        ("!!!", True, "only-punct"),
        ("   ,,,  ", True, "only-spaces-and-commas"),

        # Simple exact cases
        ("abba",  True,  "even-length-pal"),
        ("abcba", True,  "odd-length-pal"),
        ("abca",  False, "one-off-middle"),

        # Edge-ish within constraints
        ("Z", True, "single-char"),
        ("Z!", True, "single-char-with-punct"),

        # Long-ish with lots of noise
        ("___Madam...I’m Adam___", True, "long-noisy-true"),
        ("This is not a palindrome!!", False, "long-noisy-false"),
    ]

    def _p(x: str, limit=76) -> str:
        s = repr(x)  # repr shows quotes and escapes, helpful for spaces/punct
        return s if len(s) <= limit else s[:limit-3] + "…'"

    passed = 0
    for i, (inp, expected, label) in enumerate(TESTS, 1):
        got = sol(inp)
        ok = (got == expected)
        passed += ok
        print(f"[{i:02d}][{label:<24}] s={_p(inp)} -> got={got} expected={expected} | {'✅' if ok else '❌'}")

    print(f"\nPassed {passed}/{len(TESTS)} tests.")

    # Show a pointer trace for one illustrative sample if enabled
    _trace_example("Was it a car or a cat I saw?")


if __name__ == "__main__":
    _run_tests()
