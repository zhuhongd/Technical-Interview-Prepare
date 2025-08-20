"""
Problem: 3Sum (week 03)

-------
Given an array nums, return all UNIQUE triplets [a, b, c] such that:
  a + b + c = 0, and the three elements come from different indices.
Triplets can be returned in any order, but duplicates must be removed.

Link: https://neetcode.io/problems/three-integer-sum?list=neetcode150
"""

from typing import List


# ============================================================
# ✅ Active Solution: Sort + Fix-One + Two Pointers (O(n^2))
# ============================================================
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # your solution here

        return


# ============================================================
# (Optional) Notes for learners
# ------------------------------------------------------------
# • Don’t try to use a set of lists directly for dedup — lists are unhashable.
#   Sorting + skip-duplicates is cleaner and O(1) space.
# • Always move BOTH pointers after recording a valid triplet (and then skip dups),
#   otherwise you may loop forever or add duplicates.
# • You can short-circuit on some bounds (e.g., if nums[i] > 0 break) for micro-optimizations,
#   but the above is clear and passes the constraints comfortably.
# ============================================================


# -----------------------------
# 🧪 Inline tests (order-insensitive)
# -----------------------------
def _normalize(groups: List[List[int]]) -> List[tuple]:
    """
    Convert to an order-insensitive canonical form:
      - each triplet sorted (they already are, but normalize anyway)
      - outer list sorted as tuples
    """
    return sorted(tuple(sorted(g)) for g in groups)

def _run_tests() -> None:
    sol = Solution().threeSum

    # (nums, expected_triplets, label)
    TESTS = [
        # From prompt
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]], "example-1"),
        ([0, 1, 1],            [],                          "example-2"),
        ([0, 0, 0],            [[0, 0, 0]],                 "example-3"),

        # More coverage
        ([3, -2, 1, 0],        [],                          "no-solution"),
        ([0, 0, 0, 0],         [[0, 0, 0]],                 "many-zeros"),
        ([-2, 0, 1, 1, 2],     [[-2, 0, 2], [-2, 1, 1]],    "classic-mix"),
        ([-4, -1, -1, 0, 1, 2], [[-1, -1, 2], [-1, 0, 1]],  "lc-common"),
        ([-2, -2, 0, 0, 2, 2], [[-2, 0, 2]],                "dup-pairs"),
        ([-1, -1, -1, 3], [] , "no-zero-sum"),      # -1 -1 + 3 = 1; no zero triplet
        ([1, 2, 3], [] , "no-zero-sum-positives"),  # all positive -> can’t sum to 0
        ([-5, 2, 3, 0, 0],     [[-5, 2, 3]],                "neg-big-plus-pair"),
    ]

    passed = 0
    for i, (nums, expected, label) in enumerate(TESTS, 1):
        got = sol(nums)
        ok = _normalize(got) == _normalize(expected)
        passed += ok

        def _p(x, lim=72):
            s = str(x)
            return s if len(s) <= lim else s[:lim-3] + "...]"

        print(f"[{i:02d}][{label:<16}] nums={_p(nums)}")
        print(f"  got      = {_normalize(got)}")
        print(f"  expected = {_normalize(expected)}  -> {'✅' if ok else '❌'}\n")

    print(f"Passed {passed}/{len(TESTS)} tests.")


if __name__ == "__main__":
    _run_tests()
