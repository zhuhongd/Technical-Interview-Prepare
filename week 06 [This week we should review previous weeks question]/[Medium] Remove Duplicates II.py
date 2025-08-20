"""
Remove Duplicates from Sorted Array II (week 03)

What you're given
-----------------
A sorted integer array `nums` in **non-decreasing** order.

What the grader expects after your function returns
---------------------------------------------------
1) Return an integer `k` — the number of elements kept under the rule:
     • each distinct value may appear **at most twice**.
2) The first `k` positions of `nums` (i.e., `nums[:k]`) must contain those kept elements
   in the **same relative order** as the original.
3) It is **not necessary** to consider elements beyond index `k-1`.

Important constraints
---------------------
• Modify the array **in-place** with **O(1)** extra memory.  
• The array is sorted — duplicates appear in **contiguous blocks**.

Examples
--------
Example A
Input : nums = [1, 1, 1, 2, 2, 3]
Work  : keep up to two 1's and two 2's → [1, 1, 2, 2, 3, ...]
Output: k = 5
After : nums[:k] == [1, 1, 2, 2, 3]

Example B
Input : nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
Work  : keep [0,0], [1,1], [2], [3,3] → [0,0,1,1,2,3,3, ...]
Output: k = 7
After : nums[:k] == [0, 0, 1, 1, 2, 3, 3]

"""

from typing import List


class Solution:
    def remove_duplicates_allow_twice(self, nums: List[int]) -> int:
        # your solution here
        return 


# -----------------------------
# 🧪 Offline tests (verify k and prefix)
# -----------------------------
def _run_tests() -> None:
    def check(nums, expected_k, expected_prefix, label):
        original = nums[:]
        k = Solution().remove_duplicates_allow_twice(nums)
        ok = (k == expected_k and nums[:k] == expected_prefix)
        print(f"[{label}]")
        print(f"  input    : {original}")
        print(f"  returned : k={k}")
        print(f"  prefix   : {nums[:k]}")
        print(f"  expected : k={expected_k}, prefix={expected_prefix}  -> {'✅' if ok else '❌'}\n")

    # Provided-style examples
    check([1, 1, 1, 2, 2, 3],          5, [1, 1, 2, 2, 3],      "example-A")
    check([0, 0, 1, 1, 1, 1, 2, 3, 3], 7, [0, 0, 1, 1, 2, 3, 3], "example-B")

    # Edge & coverage
    check([7],                         1, [7],                  "single")
    check([5, 5],                      2, [5, 5],               "two-only")
    check([5, 5, 5, 5],                2, [5, 5],               "all-duplicates")
    check([1, 2, 3, 4],                4, [1, 2, 3, 4],         "already-unique")
    check([-2, -2, -1, -1, -1, 0, 0, 0], 6, [-2, -2, -1, -1, 0, 0], "negatives-mix")

    # Longer duplicate blocks (ensure only two copies remain)
    check([1, 1, 2, 2, 2, 2, 2, 3, 3, 3], 6, [1, 1, 2, 2, 3, 3], "longer-blocks")

    # Many zeros and ones
    check([0, 0, 0, 0, 0, 1, 1, 1, 1, 2], 5, [0, 0, 1, 1, 2],    "zeros-ones-mix")

if __name__ == "__main__":
    _run_tests()
