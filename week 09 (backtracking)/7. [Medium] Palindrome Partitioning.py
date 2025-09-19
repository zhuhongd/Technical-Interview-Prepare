"""
Palindrome Partitioning (LeetCode 131) — EECS4070 Teaching-First Version

Problem
-------
Given a string s, split s into substrings where every substring is a palindrome.
Return all possible lists of palindromic substrings.

Link
----
https://leetcode.com/problems/palindrome-partitioning/

Key Examples
------------
Input : s = "aab"
Output: [["a","a","b"], ["aa","b"]]

Input : s = "a"
Output: [["a"]]

Beginner Intuition
------------------
We want to cut the string into pieces so that every piece reads the same forward
and backward. A natural strategy is backtracking:
- At position i, try every end j >= i such that s[i:j+1] is a palindrome.
- Append it, recurse from j+1; when we reach the end, record the path.

A small optimization makes this very fast: precompute a table isPal[i][j] that
tells us in O(1) whether s[i..j] is a palindrome (expanded from short to long).

Approach Overview
-----------------
1) Backtracking + DP palindrome table (active):
   - Precompute isPal in O(n^2).
   - DFS over cut positions using O(1) pal checks.

2) Backtracking + on-the-fly palindrome check (alternative):
   - Check palindrome by two pointers when needed (simpler, a bit slower).

3) Memoized DFS (returns partitions from index i) (alternative):
   - Top-down with caching to avoid recomputing suffix results.

Complexity
----------
Let n = len(s), and let K be the number of valid partitions.
Precompute: O(n^2) time and space for isPal.
Search   : O(n * K) to collect all partitions (each substring copy costs up to O(n)).
Overall  : O(n^2 + nK) time, O(n^2 + n) extra space (plus output).

Tests
-----
Includes provided examples and a few additional cases.
"""

from typing import List


# ============================================================
# ✅ Active Solution: Backtracking + O(1) palindrome table
# ============================================================
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        # Precompute isPal[i][j]
        isPal = [[False]*n for _ in range(n)]
        for i in range(n):               # length 1
            isPal[i][i] = True
        for i in range(n-1):             # length 2
            isPal[i][i+1] = (s[i] == s[i+1])
        for length in range(3, n+1):     # length >= 3
            for i in range(0, n-length+1):
                j = i + length - 1
                isPal[i][j] = (s[i] == s[j]) and isPal[i+1][j-1]

        ans: List[List[str]] = []
        path: List[str] = []

        def dfs(i: int) -> None:
            if i == n:
                ans.append(path.copy())
                return
            for j in range(i, n):
                if isPal[i][j]:
                    path.append(s[i:j+1])
                    dfs(j+1)
                    path.pop()

        dfs(0)
        return ans


# ============================================================
# Alternative 1: Backtracking + on-the-fly palindrome check
# ============================================================
class SolutionOnTheFly:
    def partition(self, s: str) -> List[List[str]]:
        def is_pal(a: int, b: int) -> bool:
            while a < b:
                if s[a] != s[b]:
                    return False
                a += 1; b -= 1
            return True

        ans: List[List[str]] = []
        path: List[str] = []

        def dfs(i: int) -> None:
            if i == len(s):
                ans.append(path.copy()); return
            for j in range(i, len(s)):
                if is_pal(i, j):
                    path.append(s[i:j+1])
                    dfs(j+1)
                    path.pop()

        dfs(0)
        return ans


# ============================================================
# Alternative 2: Memoized DFS (returns partitions from index)
# ============================================================
class SolutionMemo:
    def partition(self, s: str) -> List[List[str]]:
        from functools import lru_cache

        def is_pal(a: int, b: int) -> bool:
            while a < b:
                if s[a] != s[b]:
                    return False
                a += 1; b -= 1
            return True

        @lru_cache(maxsize=None)
        def solve(i: int) -> List[List[str]]:
            if i == len(s):
                return [[]]
            res: List[List[str]] = []
            for j in range(i, len(s)):
                if is_pal(i, j):
                    for tail in solve(j+1):
                        res.append([s[i:j+1]] + tail)
            return res

        return solve(0)


# ============================================================
# Tests
# ============================================================
def _norm(partitions: List[List[str]]) -> tuple:
    """Normalize for order-insensitive comparison: sort by (len, tuple(parts))."""
    return tuple(sorted((tuple(p) for p in partitions), key=lambda x: (len(x), x)))

def _run_tests() -> None:
    impls = [
        ("DPBacktrack", Solution().partition),
        ("OnTheFly",    SolutionOnTheFly().partition),
        ("Memo",        SolutionMemo().partition),
    ]

    TESTS = [
        ("aab", [["a","a","b"],["aa","b"]], "ex1"),
        ("a",   [["a"]],                     "ex2"),
        ("abba", [["a","b","b","a"], ["a","bb","a"], ["abba"]], "sym"),
        ("aaa",  [["a","a","a"],["a","aa"],["aa","a"],["aaa"]], "all-same"),
        ("abc",  [["a","b","c"]],            "no-merge"),
    ]

    passed = total = 0
    for s, expected, label in TESTS:
        print(f"\n[{label}] s={s!r}")
        exp_norm = _norm(expected)
        for name, fn in impls:
            got = fn(s)
            ok = (_norm(got) == exp_norm)
            total += 1; passed += ok
            print(f"  {name:<12} -> size={len(got):<2} match={'✅' if ok else '❌'} | got={_norm(got)}")
    print(f"\nPassed {passed}/{total} checks.")

if __name__ == "__main__":
    _run_tests()
