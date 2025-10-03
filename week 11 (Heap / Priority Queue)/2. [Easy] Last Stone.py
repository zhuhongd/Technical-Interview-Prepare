"""
EECS4080 — Pattern-Based Interview Preparation
Problem: Last Stone Weight (LeetCode 1046)

------------------------------------------------------------------------------
Problem
------------------------------------------------------------------------------
You are given an array of integers stones where stones[i] represents the weight
of the ith stone.

Simulation:
• At each step, pick the two heaviest stones x and y (x <= y).
• Smash them:
    - If x == y: both destroyed.
    - If x < y: replace y with (y - x).
• Repeat until ≤ 1 stone remains.

Return the weight of the last stone, or 0 if none remain.

Example 1:
    Input: [2,3,6,2,4]
    Output: 1
Example 2:
    Input: [1,2]
    Output: 1

Constraints:
    1 <= len(stones) <= 20
    1 <= stones[i] <= 100

------------------------------------------------------------------------------
Beginner Intuition
------------------------------------------------------------------------------
We always need the two largest stones. A brute-force approach could sort the
array every time and smash the two largest, but repeated sorting is costly.

Instead, a *heap* is perfect:
- Python's `heapq` is a min-heap by default, so store negative weights to
  simulate a max-heap.
- Each step: pop twice, compute result, push back if needed.

------------------------------------------------------------------------------
Approach Overview (Active Solution: Max-Heap Simulation)
------------------------------------------------------------------------------
1) Convert stones into negative values and heapify (so largest stones become
   smallest negatives).
2) While ≥ 2 stones:
      pop two (largest two stones).
      if they differ, push back the difference.
3) Return stone if one remains, else 0.

------------------------------------------------------------------------------
Complexity
------------------------------------------------------------------------------
Let n = number of stones.
Time:  O(n log n) because each pop/push is O(log n), and we may do up to n times.
Space: O(n) for the heap.

------------------------------------------------------------------------------
Common Mistakes & Gotchas
------------------------------------------------------------------------------
• Forgetting Python’s `heapq` is min-heap → must store negatives.
• Not handling the case when both stones are equal.
• Forgetting to check for empty heap at the end.

------------------------------------------------------------------------------
"""

from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Simulate the stone smashing process and return the last remaining stone.

        Args:
            stones: list of stone weights (1 <= len(stones) <= 20)

        Returns:
            int: weight of the last stone, or 0 if none remain
        """
        # Convert to max-heap using negative values
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            # Pop two largest stones
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            if y > x:
                # Push back the difference
                heapq.heappush(heap, -(y - x))

        return -heap[0] if heap else 0


# ------------------------------------------------------------------------------
# Helpers & Offline Tests
# ------------------------------------------------------------------------------
def _run_single_case(stones: List[int], expected: int) -> None:
    s = Solution()
    got = s.lastStoneWeight(stones)
    print(f"[TEST] stones={stones} -> {got}, expected={expected}")
    assert got == expected, f"Expected {expected}, got {got}"


if __name__ == "__main__":
    # Examples
    _run_single_case([2, 3, 6, 2, 4], 1)
    _run_single_case([1, 2], 1)

    # Edge: single stone
    _run_single_case([7], 7)

    # Edge: all equal stones
    _run_single_case([5, 5, 5, 5], 0)

    # Mixed
    _run_single_case([9, 3, 2, 10], 0)   # 10-9=1, heap=[3,2,1] => 3-2=1 => 1-1=0

    print("All tests passed ✅")
