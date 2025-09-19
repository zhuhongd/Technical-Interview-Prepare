"""
Subsets (LeetCode 78) — EECS4070 Teaching-First Version

Problem
-------
Given an array nums of unique integers, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Order of subsets does not matter.

Link
----
https://leetcode.com/problems/subsets/

Key Examples
------------
Input : nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]  (order may vary)

Input : nums = [7]
Output: [[],[7]]

Beginner Intuition
------------------
A subset is just a choice of “pick or skip” for each element. With n elements,
there are 2^n ways. Backtracking is a natural fit: at index i, either include
nums[i] or don’t, and recurse until we’ve considered all items.

Approach Overview
-----------------
1) Backtracking (active):
   - Maintain a 'path' for the current subset and a results list.
   - At each index i: recurse without nums[i], then with nums[i].
   - Append a copy of 'path' when we’ve processed all indices.

2) Bitmask (alternative):
   - For mask in [0 .. 2^n - 1], include nums[j] iff j-th bit of mask is 1.

3) Cascading (alternative):
   - Start with [[]]; for each x in nums, duplicate all current subsets and add x.

Complexity
----------
Let n = len(nums) (≤ 10).
Time : O(n * 2^n) — each subset copy costs up to O(n) and there are 2^n subsets.
Space: O(n) recursion depth for backtracking (excluding output), and O(2^n) for results.

Tests
-----
- Covers given examples and some extra cases (including negatives and different orders).
- Uses order-insensitive comparison by normalizing to tuples inside a set.
"""

from typing import List


# ============================================================
# ✅ Active Solution: Backtracking (pick/skip)
# ============================================================
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans: List[List[int]] = []
        path: List[int] = []

        def dfs(i: int) -> None:
            if i == len(nums):
                ans.append(path.copy())
                return
            # 1) Skip nums[i]
            dfs(i + 1)
            # 2) Pick nums[i]
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

        dfs(0)
        return ans


# ============================================================
# Alternative 1: Bitmask enumeration
# ============================================================
class SolutionBitmask:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        out: List[List[int]] = []
        for mask in range(1 << n):
            cur: List[int] = []
            for j in range(n):
                if mask & (1 << j):
                    cur.append(nums[j])
            out.append(cur)
        return out


# ============================================================
# Alternative 2: Iterative "cascading"
# ============================================================
class SolutionCascade:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out: List[List[int]] = [[]]
        for x in nums:
            out += [subset + [x] for subset in out]
        return out


# ============================================================
# Tests (order-insensitive)
# ============================================================
def _norm(subsets: List[List[int]]) -> frozenset:
    """Normalize a list of lists into an order-insensitive frozenset of tuples."""
    return frozenset(tuple(sorted(s)) for s in subsets)

def _run_tests() -> None:
    impls = [
        ("Backtrack", Solution().subsets),
        ("Bitmask",   SolutionBitmask().subsets),
        ("Cascade",   SolutionCascade().subsets),
    ]

    TESTS = [
        # (nums, expected_subsets_any_order, label)
        ([1,2,3],
         [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]],
         "example-123"),
        ([7],
         [[],[7]],
         "example-7"),
        ([],  # edge: empty input -> only the empty subset
         [[]],
         "empty"),
        ([0, -1],
         [[], [0], [-1], [0, -1]],
         "zero-negative"),
        ([2,5,9,11],  # sanity: length 4 -> 16 subsets
         None,        # we'll just check count when expected is None
         "length-4-count"),
    ]

    passed = 0
    total  = 0

    for nums, expected, label in TESTS:
        print(f"\n[{label}] nums={nums}")
        results = []
        for name, fn in impls:
            got = fn(nums)
            results.append((name, got))

        if expected is not None:
            exp_norm = _norm(expected)
            for name, got in results:
                ok = (_norm(got) == exp_norm)
                total += 1
                passed += ok
                print(f"  {name:<9} -> size={len(got):<2} match_expected={'✅' if ok else '❌'}")
        else:
            # Only check size (e.g., 2^n)
            exp_size = 1 << len(nums)
            for name, got in results:
                ok = (len(got) == exp_size)
                total += 1
                passed += ok
                print(f"  {name:<9} -> size={len(got):<2} expected={exp_size:<2} | {'✅' if ok else '❌'}")

        # Cross-agreement across implementations
        norms = { _norm(got) for _, got in results }
        agree = (len(norms) == 1)
        print(f"  impls-agree: {'✅' if agree else '❌'}")

    print(f"\nPassed {passed}/{total} checks.")


if __name__ == "__main__":
    _run_tests()
