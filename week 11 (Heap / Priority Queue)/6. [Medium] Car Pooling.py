r"""
Car Pooling — EECS4070 (Explained, Multiple Approaches)

Problem
-------
You have a car with `capacity` empty seats and a list of one-way eastbound trips.
Each trip is `trips[i] = [numPassengers, start, end]`, meaning:
- pick up `numPassengers` at kilometer `start`
- drop them off at kilometer `end` (with `0 <= start < end`)

The car can only drive east (in increasing kilometer order). Determine if it’s
possible to complete **all** trips without the number of passengers on board
ever exceeding `capacity`.

Link
----
https://leetcode.com/problems/car-pooling/

Key Examples
------------
Input : trips = [[4,1,2],[3,2,4]], capacity = 4
Output: True
Reason: At [1,2): 4 on board (<=4). At [2,4): 3 on board (<=4).

Input : trips = [[2,1,3],[3,2,4]], capacity = 4
Output: False
Reason: At [2,3): 2 (from first) + 3 (from second) = 5 > 4.

Constraints
-----------
• 1 <= len(trips) <= 1000
• trips[i] = [p, s, e], with 1 <= p <= 100, 0 <= s < e <= 1000
• 1 <= capacity <= 100000

Beginner Intuition
------------------
As we travel east, passengers **get on** at `start` and **get off** at `end`.
We must ensure that **at every kilometer** the running total never exceeds capacity.

Two clean patterns to model this:

Approach Menu
-------------
1) **Difference Array / Prefix Sum (O(R + N))** — R is coordinate range (≤ 1000)
   - Record +p at `start`, and -p at `end`.
   - Prefix-sum across coordinates; if any running sum > capacity → False, else True.
   - Super simple and fast given small coordinate bounds.

2) **Event Sweep with Min-Heap (O(N log N))**
   - Sort trips by `start`. Maintain a min-heap of `(end, passengers)` currently onboard.
   - Before boarding at `start`, pop and drop off all whose `end <= start`.
   - Board new passengers and check capacity.

Common Pitfalls
---------------
• Forgetting that drop-offs at `end` happen **before** any pickups also at `end`.
  (In diff-array, we add at `start` and subtract at `end`, so that’s handled.)
• Off-by-one on ranges; passengers are on board over the half-open interval `[start, end)`.

"""

from __future__ import annotations
from typing import List, Tuple
import heapq


# ============================================================
# 1) Difference Array (Prefix Sum) — O(R + N), R ≤ 1000
# ------------------------------------------------------------
class SolutionDiff:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Max coordinate bound from constraints
        MAX_POS = 1000
        diff = [0] * (MAX_POS + 1 + 1)  # +1 for 0..1000, +1 for safe end index

        for p, s, e in trips:
            diff[s] += p
            diff[e] -= p  # drop-offs at e free seats before any pickup at e

        cur = 0
        for x in range(MAX_POS + 1):
            cur += diff[x]
            if cur > capacity:
                return False
        return True


# ============================================================
# 2) Event Sweep with Min-Heap — O(N log N)
# ------------------------------------------------------------
class SolutionHeap:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Sort trips by start position
        trips.sort(key=lambda t: t[1])

        onboard = 0
        # min-heap by earliest end: (end, passengers)
        heap: List[Tuple[int, int]] = []

        for p, s, e in trips:
            # Drop off everyone whose end <= current start
            while heap and heap[0][0] <= s:
                end, passengers = heapq.heappop(heap)
                onboard -= passengers

            # Board current trip
            onboard += p
            if onboard > capacity:
                return False

            heapq.heappush(heap, (e, p))

        return True


# ============================================================
# Choose active solution (Difference Array is simplest & fastest here)
# ------------------------------------------------------------
class Solution(SolutionDiff):
    """Default to difference-array approach."""
    pass


# ============================================================
# Walkthrough & Tests
# ------------------------------------------------------------
def _run_tests() -> None:
    impls = [
        ("Diff", SolutionDiff().carPooling),
        ("Heap", SolutionHeap().carPooling),
        ("Active", Solution().carPooling),
    ]

    TESTS = [
        ([[4,1,2],[3,2,4]], 4, True),
        ([[2,1,3],[3,2,4]], 4, False),
        ([[1,0,1]], 1, True),
        ([[2,0,5],[3,3,7]], 3, False),   # overlap [3,5) -> 5 > 3
        ([[3,2,7],[3,7,9],[8,3,9]], 11, True),
        ([[9,0,1],[3,3,7]], 9, True),
        ([[9,0,1],[3,0,1]], 11, False),
        ([[9,0,1],[3,0,1]], 10, False),
        ([[5,0,5],[3,5,10]], 5, True),
        ([[5,0,5],[3,5,10]], 4, False),
        ([[1,5,6],[1,6,7],[10,7,8]], 10, True), # drop at 7 before new pickup at 7 (heap logic)
    ]

    all_ok = True
    for i, (trips, cap, exp) in enumerate(TESTS, 1):
        print(f"\n[{i:02d}] trips={trips}, capacity={cap}, expect={exp}")
        for name, fn in impls:
            got = fn([t[:] for t in trips], cap)  # copy for safety
            ok = (got == exp)
            all_ok &= ok
            print(f"  {name:<6} -> {got}  {'✅' if ok else '❌'}")

    print("\nALL PASS ✅" if all_ok else "\nSome failures ❌")


if __name__ == "__main__":
    _run_tests()
