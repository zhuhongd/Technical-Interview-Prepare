"""
Remove Duplicates from Sorted Array II — EECS4070

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

Edge thoughts
-------------
• Length ≤ 2 → already valid (you can keep everything).  
• Long duplicate blocks (e.g., five 0's) → keep exactly two.  
• Already all unique → keep everything.

Why the “sorted” property is the key
------------------------------------
Duplicates show up next to each other. If we allow **at most two**, then when we scan left→right,
we can keep the current value `x` **iff** we haven’t already written two copies of `x` into the prefix.

Intuition: Two-pointer write-in-place
-------------------------------------
We keep two indices:
• **fast** — scans through the array.  
• **slow** — the position where we will **write** the next kept element.

Core rule (easy to remember):
> “Allow write if we haven’t already written two of this value.”

In code, thanks to sorting, that rule is equivalent to:
- If `slow < 2`, keep (we don’t even have two elements total yet).
- Else, keep `x = nums[fast]` **iff** `nums[slow - 2] != x`.  
  If they’re equal, it means the last two written elements are already `x` → skip.

Algorithm (step by step)
------------------------
1) If `len(nums) <= 2`, return `len(nums)` (already valid).
2) Initialize `slow = 0` (next write index).
3) For each `fast` from 0..n-1:
   • Let `x = nums[fast]`.  
   • If `slow < 2` or `nums[slow-2] != x`: write `nums[slow] = x`, then `slow += 1`.  
   • Otherwise skip (we've already kept two copies of `x`).
4) Return `slow` as `k`. The first `k` entries `nums[:k]` are the allowed prefix.

Mini dry run
------------
nums = [1, 1, 1, 2, 2, 3]
slow=0
fast=0: x=1  -> slow<2         -> keep  -> nums[0]=1, slow=1
fast=1: x=1  -> slow<2         -> keep  -> nums[1]=1, slow=2
fast=2: x=1  -> nums[0]==1     -> already 2 copies -> skip
fast=3: x=2  -> nums[0]=1 != 2 -> keep  -> nums[2]=2, slow=3
fast=4: x=2  -> nums[1]=1 != 2 -> keep  -> nums[3]=2, slow=4
fast=5: x=3  -> nums[2]=2 != 3 -> keep  -> nums[4]=3, slow=5
Return k=5; nums[:5] == [1, 1, 2, 2, 3]

Complexity
----------
Time : O(n)   — single pass  
Space: O(1)   — constant extra memory (in-place writes)
"""

from typing import List


# ============================================================
# ✅ Active Solution: Allow at most TWO copies (O(n), O(1) space)
# ============================================================
class Solution:
    def remove_duplicates_allow_twice(self, nums: List[int]) -> int:
        """
        Modify nums in-place so each distinct value appears at most twice.
        Return k such that nums[:k] contains the kept prefix.
        """
        n = len(nums)
        if n <= 2:
            return n  # already valid as-is

        slow = 0  # next write position
        for fast in range(n):
            x = nums[fast]
            if slow < 2 or nums[slow - 2] != x:
                nums[slow] = x
                slow += 1
            # else: we've already kept two of x; skip this occurrence

        return slow  # k


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
