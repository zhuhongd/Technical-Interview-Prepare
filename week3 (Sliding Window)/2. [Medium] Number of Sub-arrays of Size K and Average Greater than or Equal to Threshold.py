"""
Problem: Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

Given an integer array `arr`, and two integers `k` and `threshold`, return the number of contiguous subarrays of size `k` 
whose average is greater than or equal to `threshold`.

Examples:
Input: arr = [2, 2, 2, 2, 5, 5, 5, 8], k = 3, threshold = 4
Output: 3
Explanation:
Subarrays of size 3:
- [2,2,2] → avg = 2
- [2,2,5] → avg = 3
- [2,5,5] → avg = 4 ✅
- [5,5,5] → avg = 5 ✅
- [5,5,8] → avg = 6 ✅

Only 3 subarrays have average >= 4.

Input: arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
Output: 6
Explanation: The first 6 subarrays of size 3 have averages greater than or equal to 5.

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= arr[i] <= 10^4
- 1 <= k <= arr.length
- 0 <= threshold <= 10^4

Link: https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
"""

# -----------------------------
# Brute Force Approach:
# -----------------------------
# Slide a window of size k across the array and compute the average every time.
# Time complexity: O(n * k)
# Space complexity: O(1)

class Solution:
    def numOfSubarrays_brute(self, arr: list[int], k: int, threshold: int) -> int:
        count = 0
        for i in range(len(arr) - k + 1):
            avg = sum(arr[i:i + k]) / k
            if avg >= threshold:
                count += 1
        return count
# -----------------------------
# Optimized Sliding Window Approach:
# -----------------------------
# Instead of recomputing sum every time, we maintain a running window sum.
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def numOfSubarrays(self, arr: list[int], k: int, threshold: int) -> int:
        required_sum = k * threshold
        window_sum = sum(arr[:k])
        count = 1 if window_sum >= required_sum else 0

        for i in range(k, len(arr)):
            window_sum += arr[i] - arr[i - k]
            if window_sum >= required_sum:
                count += 1
        return count

"""
Sliding Window Summary:

- Type: Fixed-size window (size = k)
- Condition to check: Is the current window's sum >= k * threshold?
- Update logic:
    - Add next element: arr[i]
    - Remove first element from previous window: arr[i - k]

This is a classic use of sliding window to reduce repetitive work.
Instead of computing sum every time, we just update it in O(1) as the window slides.

Great practice for time-efficient window handling.
"""
