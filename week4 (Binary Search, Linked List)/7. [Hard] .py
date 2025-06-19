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
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1  # ensure nums1 is shorter

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        l, r = 0, m

        while True:
            i = (l + r) // 2  # nums1 partition
            j = half - i      # nums2 partition

            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')

            # Check if partition is valid
            if left1 <= right2 and left2 <= right1:
                if total % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
            elif left1 > right2:
                r = i - 1  # move left
            else:
                l = i + 1  # move right
