"""
Problem: Search a 2D Matrix

You are given an `m x n` 2D integer array `matrix` and an integer `target`.

Each row in `matrix` is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return `True` if `target` exists in the matrix and `False` otherwise.

Your solution must run in O(log(m * n)) time.

Examples:
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
Output: True

Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15
Output: False

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 100
- -10,000 <= matrix[i][j], target <= 10,000

Link: https://neetcode.io/problems/search-a-2d-matrix
"""

# Approach:
# Step 1: Binary search across rows to find the correct row `mid`:
#         If target > matrix[mid][-1], go right.
#         If target < matrix[mid][0], go left.
#         If within bounds, break and search in that row.
#
# Step 2: Do standard binary search inside the selected row.
#
# Time Complexity: O(log m + log n) = O(log (m * n))
#
# Note: This approach is clean and easier to understand/debug than
# directly flattening the matrix.

class Solution2:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1

        # First binary search to find the row
        while l <= r:
            mid = (l + r) // 2
            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0]:
                r = mid - 1
            else:
                break  # Found the row where target could exist

        # If we exited the loop without breaking, target is not in any row range
        else:
            return False

        # Second binary search in the found row
        row = mid
        l1 = 0
        r1 = len(matrix[row]) - 1

        while l1 <= r1:
            midmid = (l1 + r1) // 2
            if target > matrix[row][midmid]:
                l1 = midmid + 1
            elif target < matrix[row][midmid]:
                r1 = midmid - 1
            else:
                return True

        return False  # target not found

# ==========================================================
# 🧪 Offline Tests for Search a 2D Matrix (Solution2)
# ==========================================================
def _run_tests() -> None:
    sol = Solution2()

    TESTS = [
        # --- Given examples ---
        (
            [[1,2,4,8],[10,11,12,13],[14,20,30,40]],
            10, True, "example_hit_middle_row_first"
        ),
        (
            [[1,2,4,8],[10,11,12,13],[14,20,30,40]],
            15, False, "example_miss_between_rows"
        ),

        # --- 1x1 matrix ---
        ([[5]], 5, True,  "single_cell_hit"),
        ([[5]], 4, False, "single_cell_miss"),

        # --- Single row ---
        ([[1,2,3,4,5]], 1, True,  "single_row_first"),
        ([[1,2,3,4,5]], 5, True,  "single_row_last"),
        ([[1,2,3,4,5]], 6, False, "single_row_miss_high"),

        # --- Single column (strictly increasing across rows) ---
        ([[-5],[0],[3],[9]], 9,  True,  "single_col_last"),
        ([[-5],[0],[3],[9]], -6, False, "single_col_too_small"),
        ([[-5],[0],[3],[9]], 4,  False, "single_col_gap"),

        # --- Row boundary & gaps ---
        ([[1,3,5],[7,9,11],[13,15,17]], 6, False, "gap_between_rows"),
        ([[1,3,5],[7,9,11],[13,15,17]], 7, True,  "row_boundary_hit_left"),

        # --- Duplicates allowed *within a row* (non-decreasing rows) ---
        ([[1,1,1],[4,4,4]], 1, True,  "duplicates_within_row_hit"),
        ([[1,1,1],[4,4,4]], 2, False, "duplicates_within_row_miss"),

        # --- Range edges & extremes ---
        ([[-10000,-9999],[-5,0],[100,150]], -9999, True,  "min_edge_value_hit"),
        ([[-10000,-9999],[-5,0],[100,150]], 200,   False, "greater_than_max"),
        ([[1,2],[10000,10000]], 10000, True, "max_value_hit"),
    ]

    passed = 0
    for i, (matrix, target, expected, label) in enumerate(TESTS, 1):
        got = sol.searchMatrix(matrix, target)
        ok = (got == expected)
        passed += ok
        print(f"[{i:02d}] {label:<30} target={target:<6} -> got={got}  expect={expected}  {'✅' if ok else '❌'}")

    print(f"\nPassed {passed}/{len(TESTS)} tests.")

if __name__ == "__main__":
    _run_tests()
