r"""
Kth Largest Element in an Array — EECS4070 (Explained, Multiple Approaches)

Problem
-------
Given an unsorted array `nums` and an integer `k`, return the **kth largest
element** in the array (in sorted order). This is **not** the kth *distinct*
element—duplicates count as separate items.

Follow-up: Solve it without fully sorting the array.

Link
----
https://leetcode.com/problems/kth-largest-element-in-an-array/

Key Examples
------------
Input : nums = [2,3,1,5,4], k = 2
Output: 4
Explanation: Sorted descending: [5,4,3,2,1] → 2nd largest = 4.

Input : nums = [2,3,1,1,5,5,4], k = 3
Output: 4
Explanation: Descending: [5,5,4,3,2,1,1] → 3rd largest = 4.

Constraints
-----------
• 1 <= k <= len(nums) <= 10_000
• -1000 <= nums[i] <= 1000

Beginner Intuition
------------------
“Kth largest” screams **selection**:
- Sort and index (simple, O(n log n)).
- For better performance, keep only the **k** largest seen so far using a
  **min-heap of size k** (O(n log k)).
- For optimal average time, use **Quickselect** (Hoare’s selection), which is
  like quicksort’s partition but only recurses on the side containing the
  answer → average **O(n)**, worst-case **O(n²)** (rare with randomization).

Approach Menu
-------------
1) Sort Descending then pick index k-1 — O(n log n), simple & reliable.
2) Min-Heap of size k — O(n log k): maintain the k largest; heap top is answer.
3) Quickselect — Average O(n), worst-case O(n²): partition around a pivot until
   the pivot lands at the target index (n-k).

Conventions
-----------
• We’ll target the **index `n - k`** if we sort **ascending**.
• Duplicates naturally handled; no need for deduplication.

"""

from __future__ import annotations
import heapq
import random
from typing import List


# ============================================================
# 1) Sort-based (ascending then index n-k) — O(n log n)
# ------------------------------------------------------------
class SolutionSort:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()                   # ascending
        return nums[len(nums) - k]    # kth largest


# ============================================================
# 2) Min-Heap of size k — O(n log k)
#    Keep only the k largest numbers; root is the kth largest.
# ------------------------------------------------------------
class SolutionHeapK:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap: List[int] = []
        for x in nums:
            if len(heap) < k:
                heapq.heappush(heap, x)
            elif x > heap[0]:
                heapq.heapreplace(heap, x)   # pop+push in O(log k)
        return heap[0]


# ============================================================
# 3) Quickselect (randomized) — Avg O(n), Worst O(n^2)
#    Partition array until pivot sits at target index (n-k).
# ------------------------------------------------------------
class SolutionQuickselect:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k  # index if nums were sorted ascending

        def partition(l: int, r: int, p: int) -> int:
            """Partition around nums[p]; return its final index."""
            pivot = nums[p]
            nums[p], nums[r] = nums[r], nums[p]
            i = l
            for j in range(l, r):
                if nums[j] < pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[r] = nums[r], nums[i]
            return i

        l, r = 0, len(nums) - 1
        while True:
            p = random.randint(l, r)
            mid = partition(l, r, p)
            if mid == target:
                return nums[mid]
            if mid < target:
                l = mid + 1
            else:
                r = mid - 1


# ============================================================
# Choose your active submission class
# (Quickselect for performance; switch to SolutionHeapK/Sort as desired)
# ------------------------------------------------------------
class Solution(SolutionQuickselect):
    """Default to randomized Quickselect for average O(n)."""
    pass


# ============================================================
# Tiny walkthrough & offline tests
# ------------------------------------------------------------
def _run_tests() -> None:
    impls = [
        ("Sort", SolutionSort().findKthLargest),
        ("HeapK", SolutionHeapK().findKthLargest),
        ("Quick", SolutionQuickselect().findKthLargest),
        ("Active", Solution().findKthLargest),
    ]
    TESTS = [
        ([2,3,1,5,4], 2, 4),
        ([2,3,1,1,5,5,4], 3, 4),
        ([3], 1, 3),
        ([7,6,5,4,3,2,1], 5, 3),
        ([-1, -1, -1, -2], 2, -1),
        ([1,1,1,1,1,1,1,0], 1, 1),
        ([5,2,4,1,3,6,0], 4, 3),
    ]

    all_ok = True
    for i, (nums, k, exp) in enumerate(TESTS, 1):
        print(f"\n[{i:02d}] nums={nums}  k={k}")
        for name, f in impls:
            got = f(nums[:], k)  # pass copy
            ok = (got == exp)
            all_ok &= ok
            print(f"  {name:<6} -> {got}  (exp={exp})  {'✅' if ok else '❌'}")
    print("\nALL PASS ✅" if all_ok else "\nSome failures ❌")


if __name__ == "__main__":
    _run_tests()
