"""
Trapping Rain Water — EECS4070 (Explained, Single Active Solution)

Problem
-------
Given a non-negative integer array `height` (bar heights, width=1 each), compute how much
water is trapped after raining.

Link
----
https://leetcode.com/problems/trapping-rain-water/

Key Examples

Example 1
height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1] -> 9

  level
    3 |          █  ≈  ≈  ≈  █  
    2 |    █  ≈  █  ≈  ≈  ≈  █  █  
    1 |    █  ≈  █  █  ≈  █  █  █  █
      +---------------------------------
 index  0  1  2  3  4  5  6  7  8  9

Explanation:
Water sits above indices 2, 4, 5, 6 with depths 2, 2, 3, 2 respectively → 2+2+3+2 = 9.

--------------------------------------------------------------------

Example 2
height = [2, 0, 2] -> 2

  2 | █  ≈  █
  1 | █  ≈  █
    +----------
      0  1  2


Thinking Process (two ways; we will code the O(1) space one)
------------------------------------------------------------
1) Prefix/Suffix maxima (O(n) time, O(n) space):
   - For each index i, water[i] = min(max_left[i], max_right[i]) - height[i], if positive.
   - Build max_left and max_right arrays in two passes.

2) Two Pointers (O(n) time, O(1) space)  ← Active solution:
   - Walk inward from both ends with `left` and `right`.
   - Track the best walls seen so far: `left_max`, `right_max`.
   - **Always process the side with the lower current wall**.
     - If height[left] < height[right], then the right wall is not the limiter; only
       `left_max` matters at `left`. If height[left] < left_max, we trap `left_max - height[left]`;
       else update left_max. Move left++.
     - Else (height[left] >= height[right]) process the right symmetrically.

Why this works (invariant)
--------------------------
At each step, if `height[left] < height[right]`, then:
- The water level at `left` is limited by `left_max` (the right side is at least as tall as `height[left]`,
  so the min(left_max, right_max) equals left_max or higher).
- Therefore, we can finalize water over `left` now without knowing the exact right_max.

By symmetric reasoning, when `height[left] >= height[right]`, we can finalize the right side.

Complexity
----------
Time:  O(n)  — each index processed exactly once
Space: O(1)  — only a few integers (left/right/left_max/right_max)

Dry Run (short)
---------------
height = [2,1,2]
left=0, right=2, left_max=0, right_max=0
- height[left]=2 >= height[right]=2 → process right:
  right_max = max(0,2)=2, right→1
- height[left]=2 > height[right]=1 → process right:
  1 < right_max(2) → add 2-1=1; total=1; right→0 (stop)
Answer = 1
"""

from typing import List


# ============================================================
# ✅ Active Solution: Two Pointers (O(n) time, O(1) space)
# ============================================================
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0

        left, right = 0, n - 1
        left_max, right_max = 0, 0
        total = 0

        while left < right:
            if height[left] < height[right]:
                # Left side is limiting
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    total += left_max - height[left]
                left += 1
            else:
                # Right side is limiting (or equal)
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    total += right_max - height[right]
                right -= 1

        return total


# ============================================================
# (Optional) Alternatives for learners (commented)
# ------------------------------------------------------------
# class Solution:
#     def trap_prefix_suffix(self, height: List[int]) -> int:
#         n = len(height)
#         if n == 0:
#             return 0
#         left_max = [0] * n
#         right_max = [0] * n
#         left_max[0] = height[0]
#         for i in range(1, n):
#             left_max[i] = max(left_max[i-1], height[i])
#         right_max[-1] = height[-1]
#         for i in range(n-2, -1, -1):
#             right_max[i] = max(right_max[i+1], height[i])
#         total = 0
#         for i in range(n):
#             total += max(0, min(left_max[i], right_max[i]) - height[i])
#         return total
#
# class Solution:
#     def trap_brute_force(self, height: List[int]) -> int:
#         n = len(height); total = 0
#         for i in range(n):
#             left_max = max(height[:i+1])
#             right_max = max(height[i:])
#             total += max(0, min(left_max, right_max) - height[i])
#         return total
# ============================================================


# -----------------------------
# 🧪 Inline tests (deterministic)
# -----------------------------
def _run_tests() -> None:
    trap = Solution().trap

    TESTS = [
        # Prompt-style examples
        ([0,2,0,3,1,0,1,3,2,1], 9, "example-9"),
        ([0,1,0,2,1,0,1,3,2,1,2,1], 6, "lc-classic-6"),

        # Small/edge
        ([], 0, "empty"),
        ([1], 0, "single"),
        ([1,2], 0, "two-bars"),
        ([2,1,2], 1, "small-bucket"),

        # More coverage
        ([3,0,2,0,4], 7, "two-pits"),
        ([4,1,3], 2, "simple-pit"),
        ([1,0,2,1,0,1,3], 5, "shorter-variant"),

        # Flat/monotonic
        ([0,0,0,0], 0, "all-flat"),
        ([5,4,3,2,1], 0, "strictly-decreasing"),
        ([1,2,3,4,5], 0, "strictly-increasing"),

        # Plateaus / wide basins
        ([2,2,2,2], 0, "flat-top"),
        ([4,2,0,3,2,5], 9, "wide-basin-9"),
        ([5,2,1,2,1,5], 14, "two-walls-5-and-5"),

        # Many zeros sprinkled
        ([0,0,0,1,0,0,0,2,0,0], 3, "many-zeros"),
    ]

    passed = 0
    for i, (height, expected, label) in enumerate(TESTS, 1):
        got = trap(height)
        ok = (got == expected)
        passed += ok
        print(f"[{i:02d}][{label:<22}] height={height} -> got={got} expected={expected} | {'✅' if ok else '❌'}")

    print(f"\nPassed {passed}/{len(TESTS)} tests.")


if __name__ == "__main__":
    _run_tests()
