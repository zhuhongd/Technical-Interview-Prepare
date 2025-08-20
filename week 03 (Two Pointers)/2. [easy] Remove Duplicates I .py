"""
Remove Duplicates from Sorted Array — EECS4070 (Clarified, Teaching-First)

What you're given
-----------------
An integer array `nums` sorted in **non-decreasing** order (i.e., ascending with duplicates allowed).

What the grader expects after your function returns
---------------------------------------------------
1) Return an integer `k` — the **number of unique elements** in `nums`.
2) The first `k` positions of `nums` (i.e., `nums[:k]`) must contain those **unique values**
   in the **same relative order** they appear in the original array.
3) It is **not necessary** to consider elements beyond index `k-1` (i.e., `nums[k:]` can be anything).

Important constraints
---------------------
• You **must modify the input array in-place** (no extra result array).  
• Extra memory must be **O(1)** (besides a few variables).  
• The array is sorted — duplicates appear in **contiguous blocks**.

Examples
--------
Example A
Input : nums = [1, 1, 2, 3, 4]
Work  : Keep one copy from each block → [1, 2, 3, 4, ...]
Output: k = 4
After : nums[:k] == [1, 2, 3, 4]

Example B
Input : nums = [2, 10, 10, 30, 30, 30]
Work  : Keep one 2, one 10, one 30 → [2, 10, 30, ...]
Output: k = 3
After : nums[:k] == [2, 10, 30]

Edge thoughts
-------------
• Single element        → always k = 1, prefix is the same single value.  
• All values identical  → k = 1, prefix is that single value.  
• Already all unique    → k == len(nums), prefix equals original array.

Why the “sorted” property is the key
------------------------------------
Because `nums` is sorted, duplicates are **adjacent**. That means you can detect the **start of a new value**
by comparing `nums[fast]` with `nums[fast - 1]`. If they differ, you've just hit a new unique value.

Intuition: Two-pointer write-in-place
-------------------------------------
We’ll keep two indices:
• **fast** — scans through the array from left to right.  
• **slow** — the position where we will **write** the next unique value.

Algorithm (step by step)
------------------------
1) If the array is empty, return 0 (defensive; constraints say length ≥ 1, but this keeps code robust).
2) Initialize `slow = 1`. The first element at index 0 is always part of the unique prefix.
3) For each `fast` from 1 to n-1:
   • If `nums[fast] != nums[fast - 1]`, this is the **start of a new value block**:
       - write it to `nums[slow]`
       - advance `slow += 1`
   • Otherwise (duplicate), skip it.
4) When the loop finishes, `slow` is exactly the number of unique elements — return `slow`.
   The first `slow` entries `nums[:slow]` now hold your de-duplicated array.

Correctness invariant
---------------------
At any moment, `nums[:slow]` contains **all unique values found so far** in their original order,
and `slow` points to the next open write spot.

Complexity
----------
Time : O(n)   — one left-to-right pass  
Space: O(1)   — constant extra memory (in-place writes)

"""

from typing import List


# ============================================================
# ✅ Active Solution: Two Pointers (write unique values in-place)
# ============================================================
class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        """
        Modifies nums in-place so that each distinct value appears once in the front.
        Returns k = number of unique values. After return, nums[:k] holds those values.
        """
        if not nums:
            return 0  # Defensive; constraints say len(nums) >= 1, but safe.

        # Index 0 is always part of the unique prefix.
        slow = 1  # next write position for a newly encountered unique value

        for fast in range(1, len(nums)):
            # A new value block starts where the current value differs from the previous
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1

        return slow  # k = count of unique values; nums[:k] contains the unique prefix


# -----------------------------
# 🔎 Mini Dry Run (mental picture)
# -----------------------------
# nums = [2, 10, 10, 30, 30, 30]
# slow=1
# fast=1 → nums[1]=10 vs nums[0]=2  -> different → write nums[1]=10, slow=2
# fast=2 → nums[2]=10 vs nums[1]=10 -> same      → skip
# fast=3 → nums[3]=30 vs nums[2]=10 -> different → write nums[2]=30, slow=3
# fast=4 → 30 vs 30 -> skip
# fast=5 → 30 vs 30 -> skip
# Return slow=3; nums[:3] == [2, 10, 30]


# -----------------------------
# 🧪 Offline tests (verify k and prefix)
# -----------------------------
def _run_tests() -> None:
    def check(nums, expected_k, expected_prefix, label):
        arr = nums[:]  # keep a copy for display
        k = Solution().remove_duplicates(arr)
        ok = (k == expected_k and arr[:k] == expected_prefix)
        print(f"[{label}]")
        print(f"  input    : {nums}")
        print(f"  returned : k={k}")
        print(f"  prefix   : {arr[:k]}")
        print(f"  expected : k={expected_k}, prefix={expected_prefix}  -> {'✅' if ok else '❌'}\n")

    # Provided examples
    check([1, 1, 2, 3, 4],           4, [1, 2, 3, 4], "example-A")
    check([2, 10, 10, 30, 30, 30],   3, [2, 10, 30],  "example-B")

    # Additional coverage
    check([7],                       1, [7],          "single")
    check([5, 5, 5, 5],              1, [5],          "all-duplicates")
    check([0, 1, 2, 3],              4, [0,1,2,3],    "already-unique")
    check([-2, -2, -1, -1, 0, 0],    3, [-2,-1,0],    "negatives")
    check(list(range(8)),            8, list(range(8)),"increasing-no-dups")
    check([0,0,1,1,1,2,2,3,3,4],     5, [0,1,2,3,4],  "lc-classic")

if __name__ == "__main__":
    _run_tests()
