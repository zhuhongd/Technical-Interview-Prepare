r"""
K Closest Points to Origin — EECS4070 (Explained, Multiple Approaches)

Problem
-------
You are given `points`, a list of 2D coordinates `[xi, yi]`, and an integer `k`.
Return the `k` points closest to the origin `(0, 0)`.

The distance metric is standard Euclidean:
    dist = sqrt((x - 0)^2 + (y - 0)^2)

You may return the answer in any order.

Link
----
https://leetcode.com/problems/k-closest-points-to-origin/

Key Examples
------------
Input : points = [[0,2],[2,2]], k = 1
Output: [[0,2]]
Explanation: (0,2) is closer (dist=2) vs (2,2) (dist≈2.828).

Input : points = [[0,2],[2,0],[2,2]], k = 2
Output: [[0,2],[2,0]]  (order flexible)

Constraints
-----------
• 1 <= k <= len(points) <= 1000
• -100 <= points[i][0], points[i][1] <= 100

Beginner Intuition
------------------
We need the *k points with smallest distance*.  
Distance comparisons can skip the `sqrt`: compare squared distance = x² + y².  

Approach Menu
-------------
1) **Sort All Points (O(n log n))**  
   - Compute squared distance for each point.
   - Sort by distance.
   - Return first k.

2) **Heap of Size n (O(n log n))**  
   - Push all into min-heap (distance, point).
   - Pop k times.
   - Cleaner but heavier than sorting.

3) **Max-Heap of Size k (O(n log k))**  
   - Maintain a heap of k closest seen so far (store as (-dist, point)).
   - For each new point, if smaller, replace.
   - Better for large n and small k.

4) **Quickselect (Average O(n))**  
   - Partition points around pivot distance.
   - Recursively narrow down until first k are smallest.
   - Trickier but optimal average.

Conventions
-----------
• We compare squared distances (no need for sqrt).  
• Return can be in any order.  

"""

import heapq
from random import randint
from typing import List, Tuple


# ============================================================
# 1) Sort-based (simplest) — O(n log n)
# ------------------------------------------------------------
class SolutionSort:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda p: p[0]*p[0] + p[1]*p[1])
        return points[:k]


# ============================================================
# 2) Min-Heap of All — O(n log n)
# ------------------------------------------------------------
class SolutionHeapAll:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap: List[Tuple[int, List[int]]] = []
        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(heap, (dist, [x, y]))
        return [heapq.heappop(heap)[1] for _ in range(k)]


# ============================================================
# 3) Max-Heap of Size k — O(n log k)
# ------------------------------------------------------------
class SolutionHeapK:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap: List[Tuple[int, List[int]]] = []  # (-dist, point)
        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(heap, (-dist, [x, y]))
            if len(heap) > k:
                heapq.heappop(heap)
        return [pt for (_, pt) in heap]


# ============================================================
# 4) Quickselect — Average O(n)
# ------------------------------------------------------------
class SolutionQuickselect:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(i: int) -> int:
            return points[i][0]**2 + points[i][1]**2

        def partition(left: int, right: int, pivot_idx: int) -> int:
            pivot_dist = dist(pivot_idx)
            points[pivot_idx], points[right] = points[right], points[pivot_idx]
            store_idx = left
            for i in range(left, right):
                if dist(i) < pivot_dist:
                    points[store_idx], points[i] = points[i], points[store_idx]
                    store_idx += 1
            points[right], points[store_idx] = points[store_idx], points[right]
            return store_idx

        def quickselect(left: int, right: int, k_smallest: int) -> None:
            if left < right:
                pivot_idx = randint(left, right)
                p = partition(left, right, pivot_idx)
                if k_smallest < p:
                    quickselect(left, p - 1, k_smallest)
                elif k_smallest > p:
                    quickselect(p + 1, right, k_smallest)

        n = len(points)
        quickselect(0, n - 1, k)
        return points[:k]


# ============================================================
# Teaching Walkthrough (tiny dry run)
# ------------------------------------------------------------
def _walkthrough_example() -> None:
    pts = [[0, 2], [2, 0], [2, 2]]
    k = 2
    print("Example points:", pts)
    ans = SolutionHeapK().kClosest(pts, k)
    print("HeapK answer:", ans)
    # Distances: (0,2)->4, (2,0)->4, (2,2)->8


# ============================================================
# Comprehensive offline tests
# ------------------------------------------------------------
def _run_tests() -> None:
    impls = [
        ("Sort", SolutionSort().kClosest),
        ("HeapAll", SolutionHeapAll().kClosest),
        ("HeapK", SolutionHeapK().kClosest),
        ("Quickselect", SolutionQuickselect().kClosest),
    ]

    TESTS = [
        ([[0,2],[2,2]], 1, [[0,2]]),
        ([[0,2],[2,0],[2,2]], 2, [[0,2],[2,0]]),  # order may vary
        ([[3,3],[5,-1],[-2,4]], 2, None),          # LeetCode classic
    ]

    for i, (points, k, expected) in enumerate(TESTS, 1):
        print(f"\nTest {i}: points={points}, k={k}")
        for name, f in impls:
            got = f(points[:], k)  # pass copy
            print(f"  {name:<10} -> {got}")


if __name__ == "__main__":
    _walkthrough_example()
    _run_tests()
