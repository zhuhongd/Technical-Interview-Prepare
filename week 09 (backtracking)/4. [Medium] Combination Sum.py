"""
Combination Sum (LeetCode 39) — EECS4070 Teaching-First Version

Problem
-------
Given distinct integers nums and an integer target, return all unique combinations
of nums where the chosen numbers sum to target. You may reuse each number unlimited times.
Order of numbers inside a combination does not matter; order of the returned list
does not matter.

Link
----
https://leetcode.com/problems/combination-sum/

Beginner Intuition
------------------
This is a classic "unbounded" choice problem. At position i, we can:
- take nums[i] again (since unlimited), keeping index i
- or skip nums[i] and move to i+1
We keep a running sum (or remaining target). When remaining == 0 at any point,
we record the current path as a valid combination.

Approach Overview
-----------------
1) Backtracking with pruning (active):
   - Sort nums so we can prune early when candidate > remaining.
   - DFS(index, remaining, path). Two options: pick nums[index] (stay at index), or skip to index+1.
   - Record a copy of path when remaining hits 0.

2) Iterative DP (alternative):
   - dp[s] = list of unique combos summing to s.
   - For each candidate c, for s from c..target, extend dp[s-c] by appending c
     (ensure nondecreasing order by iterating candidates outside the sum loop).

3) BFS / Layered expansion (alternative):
   - Queue states (start_index, remaining, path). Push either "take" or "skip" branches.
   - Similar pruning as DFS.

Complexity
----------
Let n = len(nums), T = target, and K = number of valid combinations.
Backtracking explores combinations whose sums ≤ T:
Time : O(K * avg_len + search space) — practical with pruning & sorted nums.
Space: O(T) recursion depth in worst case (when repeatedly picking the smallest num),
       plus O(K * avg_len) for output.

Tests
-----
- Includes the given examples and edge cases; comparisons are order-insensitive.
"""

from typing import List, Tuple
from collections import deque


# ============================================================
# ✅ Active Solution: Backtracking with pruning
# ============================================================
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)  # sorting enables early stopping
        ans: List[List[int]] = []
        path: List[int] = []

        def dfs(i: int, remaining: int) -> None:
            if remaining == 0:
                ans.append(path.copy())
                return
            if i == len(nums) or remaining < 0:
                return

            # Option 1: pick nums[i] (unlimited times allowed)
            if nums[i] <= remaining:
                path.append(nums[i])
                dfs(i, remaining - nums[i])
                path.pop()

            # Option 2: skip nums[i]
            dfs(i + 1, remaining)

        dfs(0, target)
        return ans


# ============================================================
# Alternative 1: Iterative DP (unbounded knapsack-style)
# ============================================================
class SolutionDP:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        dp: List[List[List[int]]] = [[[]]] + [[] for _ in range(target)]
        # dp[s] is a list of combos (nondecreasing) that sum to s
        for c in nums:
            for s in range(c, target + 1):
                if dp[s - c]:
                    for comb in dp[s - c]:
                        # enforce nondecreasing order by only appending >= last chosen
                        if not comb or c >= comb[-1]:
                            dp[s].append(comb + [c])
        # Remove duplicates just in case (shouldn't be needed with nondecreasing rule)
        unique = {tuple(x) for x in dp[target]}
        return [list(t) for t in sorted(unique)]


# ============================================================
# Alternative 2: BFS-style expansion with pruning
# ============================================================
class SolutionBFS:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        ans: List[List[int]] = []
        q = deque([(0, target, [])])  # (start_index, remaining, path)
        while q:
            i, rem, path = q.popleft()
            if rem == 0:
                ans.append(path)
                continue
            if i == len(nums) or rem < 0:
                continue

            # take nums[i]
            if nums[i] <= rem:
                q.append((i, rem - nums[i], path + [nums[i]]))
            # skip nums[i]
            q.append((i + 1, rem, path))
        # De-dup (BFS may create same nondecreasing combos multiple ways)
        return [list(t) for t in sorted({tuple(x) for x in ans})]


# ============================================================
# Tests (order-insensitive)
# ============================================================
def _norm(combos: List[List[int]]) -> Tuple[Tuple[int, ...], ...]:
    """Sort each combo, then sort list of combos; return as tuple of tuples for comparison."""
    return tuple(sorted(tuple(sorted(c)) for c in combos))

def _run_tests() -> None:
    impls = [
        ("Backtrack", Solution().combinationSum),
        ("DP",        SolutionDP().combinationSum),
        ("BFS",       SolutionBFS().combinationSum),
    ]

    TESTS = [
        # (nums, target, expected_any_order, label)
        ([2,5,6,9], 9, [[2,2,5],[9]], "ex1"),
        ([3,4,5], 16, [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]], "ex2"),
        ([3], 5, [], "ex3"),

        # Additional checks
        ([2,3,7], 7, [[7],[2,2,3]], "classic"),
        ([2], 1, [], "no-solution"),
        ([2], 2, [[2]], "single-equal"),
        ([8, 3, 4], 11, [[3,4,4], [3,8]], "prune-check"),  # ← fixed
    ]

    passed = 0
    total  = 0

    for nums, target, expected, label in TESTS:
        print(f"\n[{label}] nums={nums} target={target}")
        exp_norm = _norm(expected)
        for name, fn in impls:
            got = fn(nums, target)
            ok = (_norm(got) == exp_norm)
            total += 1
            passed += ok
            print(f"  {name:<9} -> size={len(got):<2} match_expected={'✅' if ok else '❌'} | got={_norm(got)}")

        # Cross-impl agreement
        norms = {_norm(fn(nums, target)) for _, fn in impls}
        print(f"  impls-agree: {'✅' if len(norms) == 1 else '❌'}")

    print(f"\nPassed {passed}/{total} checks.")


if __name__ == "__main__":
    _run_tests()
