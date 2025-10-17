"""
Problem: Find Minimum in Rotated Sorted Array

You are given a rotated sorted array `nums` that was originally sorted in ascending order.
It was rotated between 1 and n times. Your task is to find the **minimum element**.

All elements are unique. Your solution must run in O(log n) time.

Examples:
Input: nums = [3,4,5,6,1,2] → Output: 1
Input: nums = [4,5,0,1,2,3] → Output: 0
Input: nums = [4,5,6,7] → Output: 4

Constraints:
- 1 <= nums.length <= 1000
- -1000 <= nums[i] <= 1000

Link: https://neetcode.io/problems/find-minimum-in-rotated-sorted-array
"""

# Approach: Binary Search (O(log n))
#
# Imagine a sorted array like [1, 2, 3, 4, 5, 6]
# If we rotate it 2 times, it becomes: [5, 6, 1, 2, 3, 4]
# The smallest value — the one we want — is 1.
#
# The trick is that although the array is rotated, at least one half is still sorted.
# We can use that fact to eliminate half of the array each time.
#
# Goal: Find the point where the order breaks — that's the minimum.
#
# Key Observations:
# - If nums[mid] > nums[r], the smallest value must be to the right of mid.
#   Example: [4,5,6,1,2,3] → nums[mid]=6, nums[r]=3 → go right
# - If nums[mid] < nums[r], the smallest is at mid or to the left.
#   Example: [6,1,2,3,4,5] → nums[mid]=2, nums[r]=5 → go left
#
# We repeat this until l == r, which will point to the minimum.

class Solution:
    def findMin(self, nums: list[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]

"""
Dry-run Example:

nums = [4,5,6,1,2,3]

Step 1: l=0, r=5 → mid=2 → nums[mid]=6, nums[r]=3 → 6 > 3 → l = mid + 1 = 3
Step 2: l=3, r=5 → mid=4 → nums[mid]=2, nums[r]=3 → 2 < 3 → r = mid = 4
Step 3: l=3, r=4 → mid=3 → nums[mid]=1, nums[r]=2 → 1 < 2 → r = mid = 3
End: l=3, r=3 → return nums[3] = 1

This shows how the loop eliminates half of the array at each step.
We never scan the entire array — this is why the solution runs in O(log n).
"""
# ==========================================================
# 🧪 Offline Tests — Find Minimum in Rotated Sorted Array
# ==========================================================
def _run_tests() -> None:
    sol = Solution()

    TESTS = [
        # Given examples
        ([3, 4, 5, 6, 1, 2], 1, "example_mid_rotation"),
        ([4, 5, 0, 1, 2, 3], 0, "example_min_near_start"),
        ([4, 5, 6, 7],       4, "example_no_rotation"),

        # Single element
        ([10], 10, "single_elem_positive"),
        ([-5], -5, "single_elem_negative"),

        # Two elements
        ([2, 1], 1, "two_rotated"),
        ([1, 2], 1, "two_sorted"),

        # General rotations
        ([5, 6, 7, 1, 2, 3, 4], 1, "rotated_break_in_middle"),
        ([2, 3, 4, 5, 6, 7, 1], 1, "min_at_last"),
        ([1, 2, 3, 4, 5, 6, 7], 1, "already_sorted"),

        # Negatives and mixed
        ([-2, -1, 0, 1, 2], -2, "sorted_with_negatives"),
        ([0, 1, 2, -3, -2, -1], -3, "rotated_with_negatives"),
        ([-1, -5, -4, -3, -2], -5, "rotated_all_negative"),

        # Longer sequences
        (list(range(1, 101)), 1, "long_sorted"),
        (list(range(50, 101)) + list(range(1, 50)), 1, "long_rotated_half"),
        (list(range(-50, 51)), -50, "long_sorted_negatives"),
        (list(range(10, 51)) + list(range(-10, 10)), -10, "long_rotated_mixed"),
    ]

    passed = 0
    for i, (nums, expected, label) in enumerate(TESTS, 1):
        got = sol.findMin(nums)
        ok = (got == expected)
        passed += ok
        print(f"[{i:02d}] {label:<32} -> got={got:<5} expect={expected:<5} {'✅' if ok else '❌'}")

    print(f"\nPassed {passed}/{len(TESTS)} tests.")


# ==========================================================
# 🔬 Optional: Randomized Property Test
#    Compare against Python's built-in min() on random rotated arrays.
# ==========================================================
def _stress_test_random(trials: int = 200) -> None:
    import random

    sol = Solution()
    for t in range(1, trials + 1):
        n = random.randint(1, 50)
        # generate unique values, sort ascending
        base = sorted(random.sample(range(-1000, 1001), n))
        # rotate by k (including 0 rotation)
        k = random.randint(0, n - 1)
        nums = base[k:] + base[:k]

        got = sol.findMin(nums)
        expected = min(nums)

        if got != expected:
            print("❌ Mismatch at trial", t)
            print("nums:", nums)
            print("expected:", expected, "got:", got)
            return
    print(f"✅ Randomized property test passed ({trials}/{trials}).")


if __name__ == "__main__":
    _run_tests()
    # _stress_test_random()  # uncomment to run randomized validation
