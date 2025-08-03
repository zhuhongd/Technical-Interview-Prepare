"""
4Sum — EECS4070 (Explained, Single Active Solution)

Problem
-------
Given an integer array nums (size n) and an integer target, return **all unique quadruplets**
[a, b, c, d] from nums such that:
  - indices are distinct (use each element at most once),
  - nums[a] + nums[b] + nums[c] + nums[d] == target,
  - order within a quadruplet does not matter, and the set of quadruplets can be in any order.
Duplicates must be removed (same values in different index orders count as the same quadruplet).

Examples
--------
Input : nums = [3, 2, 3, -3, 1, 0], target = 3
Output: [[-3, 0, 3, 3], [-3, 1, 2, 3]]

Input : nums = [1, -1, 1, -1, 1, -1], target = 2
Output: [[-1, 1, 1, 1]]

Constraints
-----------
1 <= len(nums) <= 200
-1e9 <= nums[i] <= 1e9
-1e9 <= target  <= 1e9

What the grader expects
-----------------------
• Return a list of **unique** quadruplets (no duplicates).  
• You may return them in **any order**; within each quadruplet the value order doesn’t matter.  
• Use each array element at most once per quadruplet (distinct indices).

Thinking Process (build from 3Sum)
----------------------------------
1) **Sort** the array. Sorting groups equal numbers together and enables two pointers.
2) **Fix two numbers** via indices i and j (with i < j).  
   Now the problem reduces to: find **two numbers** to the right of j whose sum is
   `target - (nums[i] + nums[j])`. This is exactly the **Two Sum II** pattern.
3) For the remaining subarray (j+1 .. n-1), use **left/right pointers**:
   - If the sum is too small, move left++.
   - If the sum is too big, move right--.
   - If equal, record the quadruplet, then move both pointers and **skip duplicates**.
4) **Skip duplicates** at every level:
   - For i: if nums[i] == nums[i-1], continue (skip same first number).
   - For j: if nums[j] == nums[j-1] (with j>i+1), continue (skip same second number).
   - After finding a quadruplet, skip equal nums[left] and equal nums[right] so you don’t repeat.

Why this removes duplicates
---------------------------
Sorting guarantees equal values are adjacent. By skipping repeated i’s, j’s, and by
advancing left/right past runs of equal values after a hit, we only record each value
combination once.

Complexity
----------
Time:  O(n^3) — two nested loops (i, j) and a linear two-pointer scan inside.  
Space: O(1) extra (ignoring the output list).

Mini Dry Run (intuition)
------------------------
nums = [3, 2, 3, -3, 1, 0], target = 3
sorted = [-3, 0, 1, 2, 3, 3]

Fix i=-3 (i=0):
  Fix j=0 (nums[j]=0):
    Need two numbers sum to 3 - (-3+0) = 6 → left=2 (1), right=5 (3)
      1+3=4 < 6 → left++
      2+3=5 < 6 → left++
      3+3=6 == 6 → record [-3,0,3,3], move left/right and skip dups
  Fix j=1 (nums[j]=1):
    Need sum to 5 → (2,3) works → record [-3,1,2,3]
Further i values yield no new unique combinations.

"""

from typing import List


# ============================================================
# ✅ Active Solution: Sort + (i,j) + Two Pointers (O(n^3))
# ============================================================
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res: List[List[int]] = []

        # Early return if fewer than 4 elements
        if n < 4:
            return res

        for i in range(n - 3):
            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # Skip duplicate second elements
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                # Two-pointer search on the remaining subarray
                left, right = j + 1, n - 1
                # Target for the two-pointer pair
                need = target - nums[i] - nums[j]

                while left < right:
                    s = nums[left] + nums[right]
                    if s < need:
                        left += 1
                    elif s > need:
                        right -= 1
                    else:
                        # Found a quadruplet
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        # Skip duplicates at left and right to avoid repeating same quadruplet
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

        return res


# -----------------------------
# 🧪 Offline tests (order-insensitive, with robust validation)
# -----------------------------
from typing import List, Tuple
from collections import Counter

def _normalize(quads: List[List[int]]) -> List[Tuple[int, int, int, int]]:
    """
    Canonical, order-insensitive representation:
      - sort each quadruplet internally
      - convert to tuple
      - sort the outer list of tuples
    """
    return sorted(tuple(sorted(q)) for q in quads)

def _valid_four_sum_answer(nums: List[int], target: int, quads: List[List[int]]) -> bool:
    """
    Property-based validator for 4Sum outputs:
      1) Each quadruplet has length 4 and sums to target
      2) No duplicate quadruplets (value-wise)
      3) Multiplicity check: each quadruplet's values are available from nums
         with enough counts (prevents fabricated values).
    """
    # 1) shape + sum
    for q in quads:
        if not isinstance(q, (list, tuple)) or len(q) != 4:
            return False
        if sum(q) != target:
            return False

    # 2) deduplicate (value-wise)
    norm = _normalize(quads)
    if len(norm) != len(set(norm)):
        return False

    # 3) multiplicity check against nums
    nums_count = Counter(nums)
    for q in norm:
        need = Counter(q)
        for v, cnt in need.items():
            if nums_count[v] < cnt:
                return False
    return True

def _run_tests() -> None:
    sol = Solution().fourSum

    # Set STRICT=True to compare exactly with curated expected triples.
    # Set STRICT=False to accept any correct answer via property-based validation.
    STRICT = True

    TESTS = [
        # —— Examples from the prompt ——
        ([3, 2, 3, -3, 1, 0], 3,
         [[-3, 0, 3, 3], [-3, 1, 2, 3]], "example-1"),

        ([1, -1, 1, -1, 1, -1], 2,
         [[-1, 1, 1, 1]], "example-2"),

        # —— Basic/edge coverage ——
        ([], 0, [], "empty"),
        ([1, 2, 3], 6, [], "less-than-four-elements"),
        ([0, 0, 0, 0], 0, [[0, 0, 0, 0]], "all-zeros"),
        ([0, 0, 0, 0, 0], 0, [[0, 0, 0, 0]], "many-zeros-one-quad"),

        # —— Duplicates / multiple answers ——
        ([1, 0, -1, 0, -2, 2], 0,
         [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]], "classic-lc"),

        ([2, 2, 2, 2, 2], 8,
         [[2, 2, 2, 2]], "all-twos"),

        # —— Mixed signs (carefully curated, no placeholders) ——
        ([5, -2, -1, 0, 1, 2, -1], 2,
         [[-2, -1, 0, 5], [-1, 0, 1, 2]], "mix-1"),

        ([-3, -1, 0, 2, 4, 5], 2,
         [[-3, -1, 2, 4]], "unique-one-quad"),
    ]

    passed = 0
    for i, (nums, target, expected, label) in enumerate(TESTS, 1):
        got = sol(nums, target)
        got_norm = _normalize(got)
        exp_norm = _normalize(expected)

        # Two checks:
        #  - strict equality to curated expected (when STRICT=True)
        #  - property-based validity (always computed for insight)
        ok_strict = (got_norm == exp_norm)
        ok_valid  = _valid_four_sum_answer(nums, target, got)

        ok = ok_strict if STRICT else ok_valid
        passed += ok

        def _p(x, lim=72):
            s = str(x)
            return s if len(s) <= lim else s[:lim-3] + "…]"

        print(f"[{i:02d}][{label:<18}] nums={_p(nums)} target={target}")
        print(f"  got (norm) = {got_norm}")
        print(f"  exp (norm) = {exp_norm}")
        print(f"  checks     = strict:{ok_strict} valid:{ok_valid}  -> {'✅' if ok else '❌'}\n")

    print(f"Passed {passed}/{len(TESTS)} tests (STRICT={STRICT}).")

if __name__ == "__main__":
    _run_tests()

