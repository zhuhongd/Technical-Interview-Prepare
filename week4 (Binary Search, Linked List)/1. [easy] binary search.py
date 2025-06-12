"""
Problem: Binary Search  (LC 704)

You are given a **sorted** array of **distinct** integers `nums` and an integer `target`.

Return the index of `target` in `nums`.  
If `target` is not present, return **-1**.

The algorithm must run in **O(log n)** time.

Examples
--------
Input : nums = [-1, 0, 2, 4, 6, 8], target = 4
Output: 3          # nums[3] == 4

Input : nums = [-1, 0, 2, 4, 6, 8], target = 3
Output: -1

Constraints
-----------
1 ≤ len(nums) ≤ 10 000  
-10 000 < nums[i], target < 10 000  
All elements in nums are **unique** and sorted ascending.
"""

# -------------------------------------------------
# Brute-Force Linear Scan (for contrast)
# -------------------------------------------------
# Time complexity : O(n)
# Space complexity: O(1)

class Solution:
    def search_linear(self, nums: list[int], target: int) -> int:
        """
        Scan each element until we find target or exhaust the list.
        """
        for i, val in enumerate(nums):
            if val == target:
                return i
        return -1

# -------------------------------------------------
# Optimal Binary Search (Iterative)
# -------------------------------------------------
# Time complexity : O(log n)
# Space complexity: O(1)

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        Standard binary search on a sorted array.

        left ……… mid ……… right
        |--------------|     (size n)
        After each step window halves → log₂(n) iterations.
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            # Avoid potential overflow in other languages:
            mid = left + (right - left) // 2
            mid_val = nums[mid]

            if mid_val == target:
                return mid                    # 🎯 found
            elif mid_val < target:
                # Target must be in the right half
                left = mid + 1
            else:
                # Target must be in the left half
                right = mid - 1

        # Target was not found
        return -1

"""
Binary-Search Key Points
------------------------
1. Works only on **sorted** data.
2. Repeatedly halves the search interval → O(log n).
3. Maintain two pointers (`left`, `right`) and a `mid`.
4. If `nums[mid]` is less than target → discard left half.
   If greater → discard right half.
5. Stop when window collapses (`left > right`).

Edge cases handled:
- Single-element arrays
- Target smaller than first or larger than last
- Negative numbers (array is still sorted)
"""
