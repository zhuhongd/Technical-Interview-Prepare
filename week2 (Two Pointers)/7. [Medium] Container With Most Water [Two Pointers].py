"""
Container With Most Water — EECS4070 (Explained, Single Active Solution)

Problem
-------
You are given an integer array `height` where `height[i]` is the height of the i-th vertical line.
Pick two lines to form a container. The container's area is:
    area = min(height[left], height[right]) * (right - left)
Return the **maximum** area possible.

Link
----
https://leetcode.com/problems/container-with-most-water/

Key Examples

Each column is a vertical line. We shade the **usable area** up to min(h[i],h[j]):

  index:   0  1  2  3  4  5  6  7
  height: [ 1, 7, 2, 5, 4, 7, 3, 6 ]

  7 |     │  █   │        █     
  6 |     │  █   │        █     █
  5 |     │  █   │  █     █     █
  4 |     │  █   │  █  █  █     █
  3 |     │  █   │  █  █  █  █  █
  2 |     │  █   █  █  █  █  █  █
  1 |  █  │  █   █  █  █  █  █  █
    +--------------------------------
       0    (1)  2  3  4  5  6 (7)

height = [1, 7, 2, 5, 4, 7, 3, 6] -> 36
  (pick indices 1 and 7: min(7,6)* (7-1) = 6*6 = 36)

--------------------------------------------------------------------

  2 |  █  │  █   █  
  1 |  █  │  █   █ 
    +--------------
      (0)   (1)  2  

height = [2, 2, 2] -> 4
  (pick ends: min(2,2)* (2-0) = 2*2 = 4)

Classic LC test:
height = [1,8,6,2,5,4,8,3,7] -> 49
  (pick indices 1 and 8: min(8,7)* (8-1) = 7*7 = 49)

Thinking Process (Two Pointers, O(n))
-------------------------------------
1) Start with the **widest** container: left=0, right=n-1. Compute current area.
2) The limiting height is the **shorter** wall (because area uses min(height[left], height[right])).
3) To possibly improve the area, we must try to find a **taller** wall while width shrinks.
   - If left wall < right wall → move `left` inward (left += 1).
   - Else → move `right` inward (right -= 1).
4) Keep a running **max_area** while moving pointers until they meet.

Why moving the shorter wall works
---------------------------------
Suppose height[left] <= height[right]. If we move the taller wall (right) inward,
the new width is smaller and the min height cannot increase beyond height[left] (the shorter wall),
so area cannot improve. Only moving the **shorter** wall could increase min height enough
to offset the reduced width. Symmetric reasoning holds for height[left] > height[right].

Complexity
----------
Time:  O(n)  — each pointer moves at most n steps total.
Space: O(1)  — only a few integers.

Dry Run (short)
---------------
height = [1, 7, 2, 5, 4, 7, 3, 6]
left=0 (1), right=7 (6): area = min(1,6)*7 = 7; move left (1<6)
left=1 (7), right=7 (6): area = min(7,6)*6 = 36  -> max=36; move right (7>6)
left=1 (7), right=6 (3): area = min(7,3)*5 = 15 ; move right
left=1 (7), right=5 (7): area = min(7,7)*4 = 28 ; move right
... pointers meet; answer stays 36.
"""

from typing import List


# ============================================================
# ✅ Active Solution: Two Pointers (O(n) time, O(1) space)
# ============================================================
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        if n < 2:
            return 0

        left, right = 0, n - 1
        max_area = 0

        while left < right:
            h = height[left] if height[left] < height[right] else height[right]
            w = right - left
            area = h * w
            if area > max_area:
                max_area = area

            # Move the pointer at the shorter wall
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# ============================================================
# (Optional) Brute Force for study (commented)
# ------------------------------------------------------------
# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         n = len(height)
#         best = 0
#         for i in range(n):
#             for j in range(i+1, n):
#                 best = max(best, min(height[i], height[j]) * (j - i))
#         return best
# ============================================================


# -----------------------------
# 🧪 Offline tests (deterministic)
# -----------------------------
def _run_tests() -> None:
    f = Solution().maxArea

    TESTS = [
        # Prompt-style examples
        ([1, 7, 2, 5, 4, 7, 3, 6], 36, "example-36"),
        ([2, 2, 2],                  4, "all-twos"),

        # Classic LeetCode sample
        ([1,8,6,2,5,4,8,3,7],       49, "lc-classic-49"),

        # Small/edge
        ([1,1],                      1, "two-bars"),
        ([0,0],                      0, "two-zeros"),
        ([0,1,0],                    0, "zero-center"),
        ([5,0,0,0,5],               20, "tall-edges"),

        # Monotonic sequences
        ([1,2,3,4,5],                6, "increasing"),
        ([5,4,3,2,1],                6, "decreasing"),

        # Mixed shapes
        ([3,9,3,4,7,2,12,6],        45, "mixed-45"),  # indices 1..6: min(9,12)*5=45
        ([1,3,2,5,25,24,5],         24, "mixed-24"),  # indices 4..6: min(25,5)*2=10; best is 3..5: min(5,24)*2=10? classic has 24 at 1..5? Let's check: 1..6 min(3,5)*5=15; best known answer is 24 (indices 2..5: min(3,24)*3=9; 4..5 min(5,24)*1=5). The true best is 24 (indices 1..5: min(3,24)*4=12) — Actually best is 24 from indices 4..5: min(25,24)*1=24.
    ]

    passed = 0
    for i, (heights, expected, label) in enumerate(TESTS, 1):
        got = f(heights)
        ok = (got == expected)
        passed += ok
        print(f"[{i:02d}][{label:<16}] height={heights} -> got={got} expected={expected} | {'✅' if ok else '❌'}")

    print(f"\nPassed {passed}/{len(TESTS)} tests.")


if __name__ == "__main__":
    _run_tests()
