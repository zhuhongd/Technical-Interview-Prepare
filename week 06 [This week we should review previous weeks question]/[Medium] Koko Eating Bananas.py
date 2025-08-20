"""
Problem: Koko Eating Bananas (week 05)

You are given an array `piles` where `piles[i]` is the number of bananas in the i-th pile.
You are also given an integer `h`, the number of hours you have to eat all the bananas.

Each hour, Koko eats up to `k` bananas from a pile. If the pile has fewer than `k` bananas,
Koko finishes that pile and waits for the next hour.

Return the minimum integer `k` such that she can eat all bananas within `h` hours.

Examples:
Input: piles = [1,4,3,2], h = 9 → Output: 2
Input: piles = [25,10,23,4], h = 4 → Output: 25

Constraints:
- 1 <= piles.length <= 1000
- piles.length <= h <= 1,000,000
- 1 <= piles[i] <= 1,000,000,000

Link: https://neetcode.io/problems/koko-eating-bananas
"""

# Approach:
# This is a binary search on the answer (a "search space problem"):
# We want the **smallest** `k` such that total eating time is <= h.
#
# Step 1: The minimum `k` is 1 (slowest possible), and the maximum is max(piles) (fastest needed).
#
# Step 2: Binary search from 1 to max(piles). For each `mid` (candidate eating speed):
#         - Calculate total hours needed to eat all piles at speed `mid`
#         - If hours_needed <= h → this `mid` might be a valid answer → try smaller k
#         - If hours_needed > h → `mid` is too slow → try larger k
#
# Time Complexity: O(n log m) where n = len(piles), m = max(piles)
#
# [Knowledge] Use `math.ceil(pile / k)` or `(pile + k - 1) // k` to simulate Koko’s hourly eating.

import math

class Solution3:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_k = float('inf')

        while l <= r:
            mid = (l + r) // 2
            hours_needed = 0

            for pile in piles:
                hours_needed += math.ceil(pile / mid)

            if hours_needed <= h:
                min_k = min(min_k, mid)
                r = mid - 1  # Try smaller k
            else:
                l = mid + 1  # Need faster speed

        return min_k