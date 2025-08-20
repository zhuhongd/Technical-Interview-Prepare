"""
Top K Frequent Elements

Problem:
---------
Given an integer array nums and an integer k, return the k most frequent elements within the array.
You may return the answer in any order. The test cases are generated such that the answer is always unique.

Examples:
---------
Input:  nums = [1, 2, 2, 3, 3, 3], k = 2
Output: [2, 3]

Input:  nums = [7, 7], k = 1
Output: [7]

Constraints:
------------
1 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000
1 <= k <= number of distinct elements in nums

Link: https://neetcode.io/problems/top-k-elements-in-list

Approaches:
-----------
We cover two main approaches:
1. Bucket Sort (O(n) time)
2. Min-Heap (O(n log k) time)

-----------------------------------------------------------
Approach 1: Bucket Sort (Best for O(n) linear time)
-----------------------------------------------------------
"""

from typing import List

class BucketSortSolution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Frequency map
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        # Create buckets: index = frequency, value = list of numbers
        # Length of nums + 1 since max frequency could be len(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            bucket[freq].append(num)

        # Collect top k frequent elements from the end
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result

"""
Time Complexity: O(n) - build map + collect results from buckets
Space Complexity: O(n) - frequency map + buckets

Common mistake:
---------------
Do NOT use `bucket = [[]] * len(nums)` as this will create multiple references to the same list object.
Instead, use a list comprehension: `[[] for _ in range(len(nums))]`
"""

# -----------------------------------------------------------
# Approach 2: Min-Heap (Useful when k << n)
# -----------------------------------------------------------

import heapq

class HeapSolution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Frequency map
        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1

        # Use a min-heap to keep top k frequent elements
        min_heap = []
        for num, freq in freq_map.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Extract results from the heap
        return [num for freq, num in min_heap]

"""
Time Complexity: O(n log k) - heap maintains k elements
Space Complexity: O(n) - frequency map + heap

Summary:
--------
- Bucket Sort is ideal for O(n) time when n isn't massive and memory isn't tight
- Min-Heap is efficient when k is small compared to n
- Both are common patterns in top-K problems

This structured explanation is part of the EECS4070 Directed Study project by Hongda Zhu.
"""

# -----------------------------------------------------------
# Inline tests (order-insensitive; unique answer guaranteed)
# -----------------------------------------------------------

def _normalize(ans: List[int]) -> tuple:
    """Sort for stable comparison; answer treated as a set."""
    return tuple(sorted(ans))

def _run_tests() -> None:
    bucket = BucketSortSolution().topKFrequent
    heap   = HeapSolution().topKFrequent

    # Each case: (nums, k, expected_set, label)
    TEST_CASES = [
        # From prompt
        ([1, 2, 2, 3, 3, 3], 2, [2, 3], "example-1"),
        ([7, 7],             1, [7],    "example-2"),

        # Basics
        ([5],                1, [5],    "single-value"),
        ([0, 0, 0, 1, 1, 2], 1, [0],    "most-frequent-zero"),

        # Negatives and mix
        ([-1, -1, -2, -2, -2, 3], 2, [-2, -1], "negatives-mix"),
        ([4, 1, -1, 2, -1, 2, 3], 2, [-1, 2],  "classic-mix"),

        # k equals number of distinct elements
        ([1, 2, 3], 3, [1, 2, 3], "k-equals-distinct"),

        # Heavy skew + safe tie below boundary
        # Frequencies: 1->100, 2->50, 3->30, 4->30 (tie, but boundary is k=2)
        ([1]*100 + [2]*50 + [3]*30 + [4]*30, 2, [1, 2], "skewed-frequencies"),

        # All same value
        ([5,5,5,5,5,5], 1, [5], "all-same"),

        # Larger but quick
        ([9]*40 + [8]*30 + [7]*20 + [6]*10, 3, [9, 8, 7], "descending-frequencies"),
    ]

    passed = 0
    for i, (nums, k, expected, label) in enumerate(TEST_CASES, 1):
        exp = set(expected)

        got_bucket = set(bucket(nums, k))
        got_heap   = set(heap(nums, k))

        ok_bucket = (got_bucket == exp)
        ok_heap   = (got_heap == exp)
        ok_both   = ok_bucket and ok_heap
        passed += ok_both

        def _p(arr, limit=60):
            s = str(arr)
            return s if len(s) <= limit else s[:limit] + "...]"

        print(f"[{i:02d}][{label:<22}] nums={_p(nums):<64} k={k:<2} "
              f"-> bucket={sorted(got_bucket)} heap={sorted(got_heap)} expected={sorted(exp)} | "
              f"{'✅' if ok_both else '❌'}")

        if not ok_both:
            if not ok_bucket:
                print("  Bucket mismatch.")
            if not ok_heap:
                print("  Heap mismatch.")

    total = len(TEST_CASES)
    print(f"\nPassed {passed}/{total} tests (both implementations).")


if __name__ == "__main__":
    _run_tests()