"""
3Sum (LeetCode #15) — EECS4070 (Explained, Single Active Solution)

Problem
-------
Given an array nums, return all UNIQUE triplets [a, b, c] such that:
  a + b + c = 0, and the three elements come from different indices.
Triplets can be returned in any order, but duplicates must be removed.

Link: https://neetcode.io/problems/three-integer-sum?list=neetcode150

Key Examples
------------
[-1, 0, 1, 2, -1, -4]  ->  [[-1,-1,2], [-1,0,1]]
[0, 1, 1]              ->  []
[0, 0, 0]              ->  [[0,0,0]]

Thinking Process (how to build from Two Sum II)
-----------------------------------------------
1) **Sort** nums first. Sorting lets us use the two-pointer trick and makes
   deduplication easier (duplicates sit next to each other).
2) **Fix one element** nums[i] as the first number of the triplet.
3) **Find two numbers** to the right (indices > i) whose sum is **-nums[i]**.
   This is exactly the Two Sum II pattern on a sorted subarray:
     - left starts at i+1, right starts at the end
     - if nums[left] + nums[right] is too small, move left++
     - if too big, move right--
     - if exactly the target, record the triplet and move both pointers
4) **Skip duplicates** at two places:
   - When advancing i: if nums[i] == nums[i-1], continue (avoid redoing same first element)
   - After finding a valid pair and moving pointers: keep skipping equal values so
     you don’t add the same triplet again.

Why skipping works:
- The array is sorted. Equal values are adjacent. If you’ve already formed
  a triplet with nums[i] (or with a given left/right value), repeating the same
  value at the same position would re-create the exact same triplet.

Complexity
----------
Time:  O(n^2)   (outer loop over i, inner two-pointer runs overall linear per i)
Space: O(1) extra (ignoring the output list)

Dry Run (small)
---------------
nums = [-1, 0, 1, 2, -1, -4] -> sort -> [-4, -1, -1, 0, 1, 2]
i=0 -> -4, need +4: no pair -> move on
i=1 -> -1, need +1:
   left=2(-1), right=5(2) -> sum=1 -> yes: [-1, -1, 2]; move both, skip dups
   left=3(0),  right=4(1) -> sum=1 -> yes: [-1, 0, 1]
i=2 -> nums[2]==nums[1] (duplicate) -> skip
Others -> no new triplets
"""

from typing import List


# ============================================================
# ✅ Active Solution: Sort + Fix-One + Two Pointers (O(n^2))
# ============================================================
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans: List[List[int]] = []

        for i in range(n):
            # 1) Skip duplicate first elements to avoid repeating the same triplet starts
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            left, right = i + 1, n - 1

            while left < right:
                s = nums[left] + nums[right]
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    # Found a valid triplet
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # 2) Skip duplicates at left and right so we don't add the same triplet again
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return ans


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
        ([-1, -1, -1, 2, 2],   [],                          "no-zero-sum"),
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
