"""
Minimum Window Substring — EECS4070 (Explained, Single Active Solution)

Problem
-------
Given two strings `s` and `t`, return the **smallest substring of `s`** that contains
**all characters of `t` (including duplicates)**. If no such window exists, return "".

Link
----
https://leetcode.com/problems/minimum-window-substring/

Key Examples
------------
s = "OUZODYXAZV", t = "XYZ"  ->  "YXAZ"
  (Shortest substring of s that contains X, Y, and Z.)

s = "xyz", t = "xyz"         ->  "xyz"
s = "x",   t = "xy"          ->  ""

Beginner’s Mental Model (Shopping List)
---------------------------------------
Think of `t` as a **shopping list** with quantities. For example, t = "AABC" means
you need two 'A's, one 'B', and one 'C'. You slide a window over `s` and count what
you “have” in your cart.

- **Expand right** to collect missing items.
- When your window has **all required counts**, it’s a valid cart.
- **Shrink left** to make the window as short as possible while still valid.
- Record the best (shortest) valid window you ever see.

What we track
-------------
• `required = Counter(t)`  → needed counts per character  
• `window`                 → counts inside the current window  
• `need = len(required)`   → how many distinct characters to satisfy  
• `have`                   → how many of those are currently satisfied (i.e., window[c] >= required[c])

Core loop (intuition first)
---------------------------
1) Move `r` right, add `s[r]` to `window`.
2) If this character’s count just reached the required amount → `have += 1`.
3) While `have == need` (window valid):
   - Update best answer if this window is smaller.
   - Move `l` right (pop `s[l]`) to try to **shrink**.
   - If popping makes any character’s count drop **below** required → `have -= 1` and stop shrinking.

Why it guarantees the minimum
-----------------------------
We only shrink when the window is valid, so any time we stop shrinking, the window
is the **smallest valid** window ending at `r`. By checking this at every possible `r`,
we will discover the **globally smallest** window.

Common Pitfalls
---------------
- Forgetting duplicates (t="AABC" needs 2 A’s, not 1).
- Using equality instead of ≥ when checking counts.
- Updating the best answer **outside** the shrinking loop (do it **inside**, when valid).
- Confusing case-sensitivity: ASCII means 'A' and 'a' are different.

Step-by-step Trace (small, complete)
------------------------------------
s = "OUZODYXAZV", t = "XYZ"
required = {'X':1, 'Y':1, 'Z':1}, need = 3
window={}, have=0, best_len=∞, best=(-1,-1), l=0

r=0:'O' → not required, have=0
r=1:'U' → not required, have=0
r=2:'Z' → window['Z']=1==required['Z'] → have=1
r=3:'O' → not required
r=4:'D' → not required
r=5:'Y' → window['Y']=1==required['Y'] → have=2
r=6:'X' → window['X']=1==required['X'] → have=3 (valid!)
  shrink from l:
    [0..6] "OUZODYX" → best=7
    pop 'O'(0): still valid → l=1, len=6 → best=6
    pop 'U'(1): still valid → l=2, len=5 → best=5 ("ZODYX")
    pop 'Z'(2): window['Z'] drops below need → have=2 → stop
r=7:'A' → not required, have=2
r=8:'Z' → window['Z']=1 → have=3 (valid!)
  shrink from l=3:
    [3..8] "ODYXAZ" → try pop:
    pop 'O'(3): valid → l=4, len=5  (best still 5)
    pop 'D'(4): valid → l=5, len=4  → best=4 ("YXAZ")
    pop 'Y'(5): now invalid → have=2 → stop
r=9:'V' → not required, have=2 → end. Answer = "YXAZ"

Complexity
----------
Time:  O(len(s)) — both pointers move right at most len(s) times.  
Space: O(len(t) + |alphabet|) — maps for needed/have (ASCII-bounded in practice).
"""

from collections import Counter, defaultdict
from typing import Tuple


# -----------------------------
# ✅ Active Solution: Sliding Window + Hash Maps (O(n))
# -----------------------------
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        required = Counter(t)            # counts needed from t
        window_counts = defaultdict(int) # counts inside the current window

        need = len(required)  # distinct chars to satisfy
        have = 0              # distinct chars currently satisfied

        res: Tuple[int, int] = (-1, -1)
        res_len = float("inf")

        l = 0
        for r, ch in enumerate(s):
            # expand
            window_counts[ch] += 1
            if ch in required and window_counts[ch] == required[ch]:
                have += 1

            # shrink to minimal while valid
            while have == need:
                if (r - l + 1) < res_len:
                    res = (l, r)
                    res_len = r - l + 1

                left_ch = s[l]
                window_counts[left_ch] -= 1
                if left_ch in required and window_counts[left_ch] < required[left_ch]:
                    have -= 1
                l += 1

        if res_len == float("inf"):
            return ""
        i, j = res
        return s[i:j+1]


# -----------------------------
# Comprehensive offline tests
# -----------------------------
def _preview_s(s: str, max_len: int = 60) -> str:
    """Short preview for long strings in logs."""
    n = len(s)
    if n <= max_len:
        return repr(s)
    half = max_len // 2
    return repr(s[:half] + "…" + s[-half:]) + f" (len={n})"

def _run_tests():
    f = Solution().minWindow
    TESTS = [
        # Provided-style examples
        ("OUZODYXAZV", "XYZ", "YXAZ", "example-1"),
        ("xyz", "xyz", "xyz", "example-2"),
        ("x", "xy", "", "example-3-none"),

        # Classic LC
        ("ADOBECODEBANC", "ABC", "BANC", "classic-lc"),

        # Duplicates in t
        ("ABCAAC", "AAC", "CAA", "dup-need-two-As"),
        ("AABBC", "AABC", "AABBC", "dup-needs-5-window"),
        ("AA", "AA", "AA", "exact-two-as"),
        ("AA", "AAA", "", "need-more-than-s"),

        # Case sensitivity (ASCII, not case-insensitive)
        ("aAaAaA", "AaA", "AaA", "case-sensitive"),

        # Single-char t
        ("BBBBA", "A", "A", "single-char-t"),
        ("BBBB", "A", "", "single-char-absent"),

        # T inside S early/late
        ("XYZZYABC", "ZZYA", "ZZYA", "covering-mixed-order"),  # needs Z,Z,Y,A -> "ZZYA"
        ("XYZABC", "ABC", "ABC", "suffix-window"),

        # Larger (but still concise)
        ("a"*50 + "XYZ" + "b"*50, "XYZ", "XYZ", "centered-triplet"),
    ]

    passed = 0
    for i, (s, t, expected, label) in enumerate(TESTS, 1):
        got = f(s, t)
        ok = (got == expected)
        passed += ok
        print(f"[{i:02d}][{label:<22}] s={_preview_s(s):<30} t={t!r:<10} -> got={got!r:<12} expected={expected!r:<12} | {'✅' if ok else '❌'}")

    print(f"\nPassed {passed}/{len(TESTS)} tests.")

if __name__ == "__main__":
    _run_tests()
