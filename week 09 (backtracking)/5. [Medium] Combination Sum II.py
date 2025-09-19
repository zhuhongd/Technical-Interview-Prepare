"""
Combination Sum II (LeetCode 40) — EECS4070 Teaching-First Version

Problem
-------
Given integers candidates (may contain duplicates) and an integer target, return all
unique combinations where the chosen numbers sum to target. Each number may be used
**at most once**. The result must not contain duplicate combinations. Order does not matter.

Link
----
https://leetcode.com/problems/combination-sum-ii/

Beginner Intuition
------------------
Compared to Combination Sum I (unlimited usage), here each element can be picked once.
Because candidates may contain duplicates, we must avoid generating the same combination
multiple times. The classic technique:
  1) Sort the array.
  2) In each DFS level, when looping j from i.., if candidates[j] == candidates[j-1] and j > i,
     skip this j (duplicate at the same depth).
  3) Prune early if candidates[j] > remaining.

Approach Overview
-----------------
1) Backtracking with sorted input & duplicate-skip (active):
   - Sort candidates.
   - DFS(i, remaining, path):
       for j in [i..n):
         if j>i and cand[j]==cand[j-1]: continue   # skip duplicates at same depth
         if cand[j] > remaining: break              # pruning
         path.append(cand[j]); DFS(j+1, remaining - cand[j]); path.pop()

2) Count-based DFS (alternative):
   - Compress candidates into (value, count) pairs.
   - Try taking k = 0..count times for each value (bounded by remaining).

3) DP (alternative, set-based):
   - Iterate values; at each step, extend previous sums but ensure each item used at most once
     by processing value once per stage and using nondecreasing sequences to avoid dupes.

Complexity
----------
Let n = len(candidates).
Time : O(#solutions * avg_len + branching) — practical with sorting & pruning.
Space: O(n) recursion depth (excluding output). DP/set approach may use extra memory.

Tests
-----
- Includes the given examples and extra edge cases; comparisons are order-insensitive.
"""

from typing import List, Tuple
from collections import Counter


# ============================================================
# ✅ Active Solution: Backtracking (sorted + skip duplicates)
# ============================================================
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans: List[List[int]] = []
        path: List[int] = []
        n = len(candidates)

        def dfs(i: int, remaining: int) -> None:
            if remaining == 0:
                ans.append(path.copy())
                return
            if i == n or remaining < 0:
                return

            prev = None
            for j in range(i, n):
                x = candidates[j]
                # Skip duplicates at the same depth
                if prev is not None and x == prev:
                    continue
                if x > remaining:
                    break
                prev = x
                path.append(x)
                dfs(j + 1, remaining - x)  # j+1 because each item can be used at most once
                path.pop()

        dfs(0, target)
        return ans


# ============================================================
# Alternative 1: Count-based DFS (value → frequency)
# ============================================================
class SolutionCountDFS:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        freq = sorted(Counter(candidates).items())  # [(val, count), ...]
        ans: List[List[int]] = []
        path: List[int] = []

        def dfs(idx: int, remaining: int) -> None:
            if remaining == 0:
                ans.append(path.copy())
                return
            if idx == len(freq) or remaining < 0:
                return

            val, cnt = freq[idx]
            # Try taking k copies of val (0..cnt), bounded by remaining
            kmax = min(cnt, remaining // val)
            # Case k = 0 (skip this value)
            dfs(idx + 1, remaining)
            # Cases k >= 1
            for k in range(1, kmax + 1):
                path.extend([val] * k)
                dfs(idx + 1, remaining - k * val)
                del path[-k:]

        dfs(0, target)
        return ans


# ============================================================
# Alternative 2: Stage-wise DP (each value used once per stage)
# ============================================================
class SolutionDP:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort and process values one by one; at each stage, we add the current value once
        candidates.sort()
        sets_by_sum = {0: {()}}  # sum -> set of tuples (sorted nondecreasing)
        for x in candidates:
            # Iterate sums descending to avoid reusing x in the same stage
            new_entries = {}
            for s, combs in list(sets_by_sum.items()):
                ns = s + x
                if ns > target:
                    continue
                new_sets = {c + (x,) for c in combs}
                if ns in new_entries:
                    new_entries[ns] |= new_sets
                else:
                    new_entries[ns] = new_sets
            for ns, new_sets in new_entries.items():
                sets_by_sum[ns] = (sets_by_sum.get(ns, set())) | new_sets
        return [list(t) for t in sorted(sets_by_sum.get(target, set()))]


# ============================================================
# Tests (order-insensitive)
# ============================================================
def _norm(combos: List[List[int]]) -> Tuple[Tuple[int, ...], ...]:
    """Sort each combo, then sort list of combos; return as tuple of tuples for comparison."""
    return tuple(sorted(tuple(sorted(c)) for c in combos))

def _run_tests() -> None:
    impls = [
        ("Backtrack", Solution().combinationSum2),
        ("CountDFS",  SolutionCountDFS().combinationSum2),
        ("DP",        SolutionDP().combinationSum2),
    ]

    TESTS = [
        # Given examples
        ([9,2,2,4,6,1,5], 8, [[1,2,5],[2,2,4],[2,6]], "ex1"),
        ([1,2,3,4,5], 7, [[1,2,4],[2,5],[3,4]], "ex2"),

        # Edge / additional
        ([], 5, [], "empty-cands"),
        ([1,1,1], 2, [[1,1]], "dups-simple"),
        ([2,5,2,1,2], 5, [[1,2,2],[5]], "lc40-classic"),
        ([10,1,2,7,6,1,5], 8, [[1,1,6],[1,2,5],[1,7],[2,6]], "lc40-sample"),
        ([3,3,3,3], 6, [[3,3]], "all-same"),
        ([4,5,11], 3, [], "no-solution"),
    ]

    passed = 0
    total  = 0

    for cands, target, expected, label in TESTS:
        print(f"\n[{label}] candidates={cands} target={target}")
        exp_norm = _norm(expected)
        for name, fn in impls:
            got = fn(cands, target)
            ok = (_norm(got) == exp_norm)
            total += 1
            passed += ok
            print(f"  {name:<9} -> size={len(got):<2} match_expected={'✅' if ok else '❌'} | got={_norm(got)}")

        # Cross-impl agreement
        norms = {_norm(fn(cands, target)) for _, fn in impls}
        print(f"  impls-agree: {'✅' if len(norms) == 1 else '❌'}")

    print(f"\nPassed {passed}/{total} checks.")


if __name__ == "__main__":
    _run_tests()
