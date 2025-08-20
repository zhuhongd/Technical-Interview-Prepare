"""

Problem: Longest Consecutive Sequence
-------
Given an *unsorted* list of integers `nums`, return the length of the *longest*
sequence of consecutive integers (numbers that increase by exactly +1 each step).
The elements do NOT need to be adjacent in the original array.
Target time: O(n).

Examples
--------
nums = [2, 20, 4, 10, 3, 4, 5]     -> 4   # sequence [2, 3, 4, 5]
nums = [0, 3, 2, 5, 4, 6, 1, 1]    -> 7   # sequence [0, 1, 2, 3, 4, 5, 6]

Constraints
----------
- 0 <= len(nums) <= 1000
- -1e9 <= nums[i] <= 1e9

Core Idea (Beginner-Friendly)
-----------------------------
Think of the numbers as points on a number line. A "consecutive sequence" is a solid
block like 2—3—4—5. We want the length of the longest block.

We can do this in O(n) using a set:
1) Put all numbers into a set S for O(1) average lookups.
2) A number x is the *start* of a sequence if (x-1) is NOT in S.
   (If x-1 exists, then x is in the *middle* of some sequence, so don't start here.)
3) For each start x, walk forward (x, x+1, x+2, ...) while those numbers exist in S.
   Track the length of this walk and record the best.

Why this is O(n):
- Each number is part of at most one forward walk (the walk that begins at its sequence start).
- Membership checks in a set are O(1) on average.

Mini Dry Run
------------
nums = [2, 20, 4, 10, 3, 4, 5]; S = {2,3,4,5,10,20}
- 2 is a start (1 not in S): walk 2,3,4,5 -> length 4
- 3,4,5 are not starts (2,3,4 are in S) -> skip
- 10 is a start: walk 10 -> length 1
- 20 is a start: walk 20 -> length 1
Answer = max(4,1,1) = 4
"""

from typing import List


# ============================================================
# ✅ Active Solution: Set + "start-only" forward expansion (O(n))
# ============================================================
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Implementation details:
        - Build a set S of all numbers for O(1) average membership checks.
        - For each x in S, if x-1 not in S, then x is the *start* of a run.
        - From x, count forward while (x+1), (x+2), ... are in S.
        - Keep track of the maximum run length.
        """
        s = set(nums)     # removes duplicates, enables O(1) membership tests
        best = 0          # best (maximum) run length seen so far

        for x in s:
            # Only begin counting if this is the smallest element of its run.
            if (x - 1) not in s:
                length = 1
                current = x
                # Keep stepping forward as long as the next integer exists.
                while (current + 1) in s:
                    current += 1
                    length += 1
                best = max(best, length)

        return best


# ============================================================
# (Optional) Alternative for Learning: Sorting approach (O(n log n))
# Uncomment to experiment; tests below target the active `Solution`.
# ============================================================
# class SortedSolution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         """
#         Easier to reason about but O(n log n) due to sorting:
#           1) Deduplicate with set(), then sort.
#           2) Scan once to count the length of each consecutive run.
#         """
#         if not nums:
#             return 0
#         uniq = sorted(set(nums))  # remove duplicates, then sort
#         best = 1
#         cur_len = 1
#         for i in range(1, len(uniq)):
#             if uniq[i] == uniq[i - 1] + 1:
#                 cur_len += 1
#             else:
#                 best = max(best, cur_len)
#                 cur_len = 1
#         return max(best, cur_len)


# -----------------------------
# Inline tests (single-solution)
# -----------------------------
def _run_tests() -> None:
    sol = Solution().longestConsecutive

    # Each case: (nums, expected_length, label)
    TEST_CASES = [
        # From prompt
        ([2, 20, 4, 10, 3, 4, 5], 4, "example-1: 2..5"),
        ([0, 3, 2, 5, 4, 6, 1, 1], 7, "example-2: 0..6 with dup 1"),

        # Edge cases
        ([], 0, "empty list -> 0"),
        ([7], 1, "single element -> 1"),
        ([5, 5, 5], 1, "all duplicates -> 1"),

        # Simple runs
        ([1, 2, 3], 3, "short run 1..3"),
        ([10, 11], 2, "two-number run"),

        # Duplicates mixed in
        ([1, 2, 2, 3], 3, "dups inside 1..3"),
        ([1, 1, 2, 2, 3, 3], 3, "heavy dups still 1..3"),

        # Classic examples
        ([100, 4, 200, 1, 3, 2], 4, "classic 1..4"),
        ([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6], 7, "long chain -1..6"),

        # Negatives & zero
        ([-2, -1, 1, 2], 2, "two small chains (-2,-1) and (1,2)"),
        ([-5, -4, -3, -1, 0, 1], 3, "either -5..-3 or -1..1 -> 3"),

        # Already consecutive
        ([1, 2, 3, 4, 5], 5, "already 1..5"),

        # Scattered with noise
        ([10, 30, 20, 21, 22, 23, 40], 4, "20..23 is longest"),

        # Multiple equal-length chains (ensure we pick the max)
        ([50, 52, 53, 100, 101, 102, 10, 11], 3, "chains 50,52..53 and 100..102 and 10..11"),

        # Larger synthetic
        (list(range(-5, 6)) + [1000, 2000, 3000], 11, "full -5..5 length 11"),
    ]

    def _p(x, limit=80):
        s = str(x)
        return s if len(s) <= limit else s[:limit-3] + "...]"

    passed = 0
    for i, (nums, expected, label) in enumerate(TEST_CASES, 1):
        got = sol(nums)
        ok = (got == expected)
        passed += ok
        print(f"[{i:02d}] {label}")
        print(f"  nums     = {_p(nums)}")
        print(f"  got      = {got}")
        print(f"  expected = {expected}  -> {'✅' if ok else '❌'}\n")

    print(f"Passed {passed}/{len(TEST_CASES)} tests.")


if __name__ == "__main__":
    _run_tests()
