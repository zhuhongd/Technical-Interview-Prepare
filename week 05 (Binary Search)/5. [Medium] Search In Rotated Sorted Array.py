"""
🔍 Problem: Search in Rotated Sorted Array

You are given a rotated version of a sorted array with **distinct integers**.
Return the index of the target if it's found, otherwise return -1.

Example:
Input: nums = [3,4,5,6,1,2], target = 1 → Output: 4
Input: nums = [3,5,6,0,1,2], target = 4 → Output: -1

Constraints:
- All elements are unique
- Time complexity must be O(log n)
- 1 <= len(nums) <= 1000

🔗 Link: https://neetcode.io/problems/search-in-rotated-sorted-array
"""

# ✅ Approach:
# This is a **modified binary search** problem.
# Even though the array is rotated, at every step, **one side is guaranteed to be sorted**.

# Step-by-step:
# 1. Compute the middle index.
# 2. Check if the middle element is the target.
# 3. Decide which half is sorted:
#    - If nums[left] <= nums[mid]: the **left half** is sorted.
#    - Otherwise, the **right half** is sorted.
# 4. Determine whether the target is in the sorted half:
#    - If it is, narrow the search to that half.
#    - If not, search the other half.

# ❗️Why it works:
# Because we're eliminating half the array each time — just like in regular binary search —
# the time complexity remains O(log n), even with the rotation.

# 💡 Tip:
# Always draw out a rotated array with mid pointers to visualize sorted vs unsorted halves.

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

# ==========================================================
# 🧪 Offline Tests — Search in Rotated Sorted Array
# ==========================================================
def _run_tests() -> None:
    sol = Solution()

    TESTS = [
        # --- Provided examples ---
        ([3, 4, 5, 6, 1, 2], 1, 4, "example_found_right_half"),
        ([3, 5, 6, 0, 1, 2], 4, -1, "example_not_found"),

        # --- No rotation (pure sorted array) ---
        ([1, 2, 3, 4, 5, 6], 1, 0, "sorted_first"),
        ([1, 2, 3, 4, 5, 6], 6, 5, "sorted_last"),
        ([1, 2, 3, 4, 5, 6], 3, 2, "sorted_middle"),
        ([1, 2, 3, 4, 5, 6], 10, -1, "sorted_not_found"),

        # --- Full rotation (same as no rotation) ---
        ([1, 2, 3, 4, 5], 2, 1, "full_rotation_equiv_sorted"),
        ([1, 2, 3, 4, 5], 5, 4, "full_rotation_equiv_sorted_end"),

        # --- Small arrays ---
        ([5], 5, 0, "single_element_hit"),
        ([5], 7, -1, "single_element_miss"),
        ([2, 1], 1, 1, "two_elements_rotated_hit"),
        ([2, 1], 2, 0, "two_elements_rotated_hit_first"),
        ([2, 1], 3, -1, "two_elements_rotated_miss"),

        # --- General rotations ---
        ([4, 5, 6, 7, 0, 1, 2], 0, 4, "classic_rotation_found_right"),
        ([4, 5, 6, 7, 0, 1, 2], 4, 0, "classic_rotation_found_left"),
        ([4, 5, 6, 7, 0, 1, 2], 2, 6, "classic_rotation_found_end"),
        ([4, 5, 6, 7, 0, 1, 2], 9, -1, "classic_rotation_not_found"),

        # --- Rotations with negatives ---
        ([6, 7, 8, -3, -2, -1, 0, 1, 2], -3, 3, "rotation_with_negatives_found"),
        ([6, 7, 8, -3, -2, -1, 0, 1, 2], 8, 2, "rotation_with_negatives_left_half"),
        ([6, 7, 8, -3, -2, -1, 0, 1, 2], 3, -1, "rotation_with_negatives_miss"),

        # --- Edge: all increasing but rotated once ---
        ([9, 1, 2, 3, 4, 5, 6, 7, 8], 1, 1, "rotated_once_min_near_start"),
        ([9, 1, 2, 3, 4, 5, 6, 7, 8], 9, 0, "rotated_once_first_element"),
        ([9, 1, 2, 3, 4, 5, 6, 7, 8], 8, 8, "rotated_once_last_element"),

        # --- Long arrays ---
        (list(range(50, 100)) + list(range(1, 50)), 1, 50, "long_rotation_target_at_boundary"),
        (list(range(50, 100)) + list(range(1, 50)), 99, 49, "long_rotation_target_end_of_first_half"),
        (list(range(50, 100)) + list(range(1, 50)), 25, 74, "long_rotation_target_in_second_half"),
        (list(range(50, 100)) + list(range(1, 50)), 100, -1, "long_rotation_target_not_present"),
    ]

    passed = 0
    for i, (nums, target, expected, label) in enumerate(TESTS, 1):
        got = sol.search(nums, target)
        ok = (got == expected)
        passed += ok
        print(f"[{i:02d}] {label:<40} target={target:<5} -> got={got:<5} expect={expected:<5} {'✅' if ok else '❌'}")

    print(f"\nPassed {passed}/{len(TESTS)} tests.")


# ==========================================================
# 🔬 Optional Property Test
# Verify correctness by comparing binary search result with naive linear search
# on random rotated arrays.
# ==========================================================
def _stress_test_random(trials: int = 200) -> None:
    import random

    sol = Solution()
    for t in range(1, trials + 1):
        n = random.randint(1, 50)
        base = sorted(random.sample(range(-1000, 1000), n))
        k = random.randint(0, n - 1)
        nums = base[k:] + base[:k]
        target = random.choice(base)
        expected = nums.index(target)
        got = sol.search(nums, target)

        if got != expected:
            print(f"❌ Mismatch trial {t}")
            print("nums:", nums)
            print("target:", target)
            print("expected:", expected, "got:", got)
            return
    print(f"✅ Randomized property test passed ({trials}/{trials}).")


if __name__ == "__main__":
    _run_tests()
    # _stress_test_random()  # Uncomment for randomized validation
