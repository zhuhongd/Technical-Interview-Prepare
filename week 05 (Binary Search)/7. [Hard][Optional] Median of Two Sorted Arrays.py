# Before you approach this question, I've marked it as "Optional" because I personally feel it's too difficult. 
# If you're a beginner to intermediate level, feel free to skip this question for now and revisit it in the future if you'd like. 
# However, if you're more advanced, feel free to give it a try. This question is by far the hardest in the last 4 weeks, in my opinion.

"""
Problem: Median of Two Sorted Arrays

You are given two sorted arrays nums1 and nums2.
Return the median of the combined sorted array in O(log(m + n)) time.

Examples:
Input: nums1 = [1, 2], nums2 = [3] → Output: 2.0
Input: nums1 = [1, 3], nums2 = [2, 4] → Output: 2.5

Constraints:
- Both arrays are sorted
- 0 <= m, n <= 1000
- 1 <= nums1[i], nums2[i] <= 10^6

Link: https://neetcode.io/problems/median-of-two-sorted-arrays
"""

# Approach: Binary Search on the Shorter Array
#
# The idea is to partition the two arrays such that:
# - Left half contains the smaller elements
# - Right half contains the larger elements
# - Median lies between the end of left half and start of right half
#
# We use binary search to find the correct partition point on the shorter array
# so that we minimize time complexity to O(log(min(m, n)))
#
# Key properties:
# - If total length is even → median = avg(maxLeft, minRight)
# - If total length is odd → median = maxLeft
#
# We assume nums1 is the shorter array to avoid index errors.

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        l, r = 0, m
        while True:
            i = (l + r) // 2
            j = half - i

            left1  = nums1[i-1] if i > 0 else float('-inf')
            right1 = nums1[i]   if i < m else float('inf')
            left2  = nums2[j-1] if j > 0 else float('-inf')
            right2 = nums2[j]   if j < n else float('inf')

            if left1 <= right2 and left2 <= right1:
                if total % 2 == 1:
                    # odd total: left side has 'half' elements; median is next element
                    return float(min(right1, right2))
                # even total
                return (max(left1, left2) + min(right1, right2)) / 2.0
            elif left1 > right2:
                r = i - 1
            else:
                l = i + 1

# ==========================================================
# ✅ Assert-Based Tests — Median of Two Sorted Arrays
# ==========================================================
def _median_merge(a, b):
    """Ground-truth via merge (O(m+n)), returns float."""
    i = j = 0
    merged = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i]); i += 1
        else:
            merged.append(b[j]); j += 1
    merged.extend(a[i:]); merged.extend(b[j:])
    n = len(merged)
    if n % 2 == 1:
        return float(merged[n//2])
    return (merged[n//2 - 1] + merged[n//2]) / 2.0


def _run_tests_assert() -> None:
    sol = Solution()
    TESTS = [
        # Provided examples
        ([1, 2], [3],                2.0,  "example_odd_total"),
        ([1, 3], [2, 4],             2.5,  "example_even_total"),

        # One array empty
        ([],       [1],              1.0,  "one_empty_singleton"),
        ([],       [1, 2],           1.5,  "one_empty_even"),
        ([5, 6, 7], [],              6.0,  "other_empty"),

        # Uneven sizes
        ([1, 2],   [3, 4, 5, 6, 7],  4.0,  "uneven_sizes_odd"),
        ([1, 2],   [3, 4, 5, 6],     3.5,  "uneven_sizes_even"),
        ([1],      [2, 3, 4, 5, 6],  3.5,  "tiny_vs_large_even"),
        ([1],      [2, 3, 4, 5],     3.0,  "tiny_vs_large_odd"),

        # Duplicates & overlaps
        ([1, 1, 1], [1, 1],          1.0,  "all_equal"),
        ([1, 2, 2], [2, 2, 3],       2.0,  "many_duplicates"),
        ([1, 2, 3], [2, 2, 2, 2],    2.0,  "dominant_value"),

        # Negative + positive
        ([-5, -2, 0], [1, 3, 4],     0.5,  "mixed_signs_even"),
        ([-3, -1],    [2, 4, 6],     2.0,  "mixed_signs_odd"),
        ([-10, -4],   [-3, -2, -1],  -3.0, "all_negative"),

        # Wide values
        ([1_000_000], [1_000_000],   1_000_000.0, "large_values_equal"),
        ([1], [1_000_000],           500000.5,    "far_apart_two_elems"),
    ]

    print("==== Running Median-of-Two-Sorted-Arrays Tests ====")
    passed = 0
    for i, (a, b, expected, label) in enumerate(TESTS, 1):
        got = sol.findMedianSortedArrays(a, b)
        try:
            assert abs(got - expected) < 1e-9
            print(f"[{i:02d}] {label:<30} ✅ PASS (got {got})")
            passed += 1
        except AssertionError:
            print(f"[{i:02d}] {label:<30} ❌ FAIL (got {got}, expected {expected})")
    print(f"\nTotal: {passed}/{len(TESTS)} passed ✅")


# ----------------------------------------------------------
# 🔬 Optional: Randomized property test (assert-based)
# ----------------------------------------------------------
def _stress_test_random_assert(trials: int = 300) -> None:
    import random
    sol = Solution()
    print(f"==== Randomized Property Test x{trials} ====")
    for t in range(1, trials + 1):
        m = random.randint(0, 30)
        n = random.randint(0, 30)
        # Allow empty arrays but not both empty
        if m == 0 and n == 0:
            n = 1
        a = sorted(random.sample(range(-2000, 2001), m)) if m else []
        b = sorted(random.sample(range(-2000, 2001), n)) if n else []
        expected = _median_merge(a, b)
        got = sol.findMedianSortedArrays(a, b)
        assert abs(got - expected) < 1e-9, f"trial {t}: got {got}, expected {expected}, a={a}, b={b}"
    print("✅ Randomized property test passed.")


if __name__ == "__main__":
    _run_tests_assert()
    # _stress_test_random_assert()  # uncomment to run randomized validator

