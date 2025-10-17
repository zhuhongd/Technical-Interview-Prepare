"""
Problem: Koko Eating Bananas

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
    
# ==========================================================
# 🧪 Offline Tests for Koko Eating Bananas (Solution3)
# ==========================================================
def _run_tests() -> None:
    sol = Solution3()

    TESTS = [
        # --- Provided examples ---
        ([1, 4, 3, 2], 9, 2, "example_easy_spread"),
        ([25, 10, 23, 4], 4, 25, "example_tight_hours"),

        # --- Edge cases ---
        ([5], 10, 1, "single_pile_many_hours"),      # 1 banana/hour is enough
        ([5], 1, 5, "single_pile_one_hour"),         # must finish all at once
        ([1, 1, 1, 1], 4, 1, "uniform_small_piles"), # all can be eaten slowly

        # --- Small constraints ---
        ([3, 6, 7, 11], 8, 4, "neetcode_standard_case"),
        ([30, 11, 23, 4, 20], 5, 30, "official_leetcode_case_1"),
        ([30, 11, 23, 4, 20], 6, 23, "official_leetcode_case_2"),

        # --- When h equals # of piles (minimal possible time flexibility) ---
        ([10, 10, 10, 10], 4, 10, "h_equals_piles_each_pile_hour"),
        ([9, 9, 9], 3, 9, "must_finish_one_pile_per_hour"),

        # --- Large h allows slower speed ---
        ([9, 9, 9], 100, 1, "large_hours_allow_min_speed"),
        ([100, 200, 300], 1000, 1, "huge_h_can_eat_one_per_hour"),

        # --- Tight h requires fast speed ---
        ([100, 200, 300], 3, 300, "tight_hours_force_max_speed"),
        ([5, 8, 6], 3, 8, "tight_small_case"),

        # --- Mixed moderate piles ---
        ([1, 10, 20, 30, 50], 10, 15, "mixed_case_moderate_speed"),
        ([1, 10, 20, 30, 50], 15, 10,  "mixed_case_more_hours"),

        # --- Extremely large pile values (sanity) ---
        ([10**9], 10**9, 1, "single_large_pile_many_hours"),
        ([10**9], 1, 10**9, "single_large_pile_one_hour"),
        ([10**6, 10**6, 10**6], 3, 10**6, "multi_large_each_one_hour"),
        ([10**6, 10**6, 10**6], 3000000, 1, "multi_large_slow_possible"),
    ]

    passed = 0
    for i, (piles, h, expected, label) in enumerate(TESTS, 1):
        got = sol.minEatingSpeed(piles, h)
        ok = (got == expected)
        passed += ok
        print(f"[{i:02d}] {label:<35} piles={piles[:5]}... h={h:<7} -> got={got:<6} expect={expected:<6} {'✅' if ok else '❌'}")

    print(f"\nPassed {passed}/{len(TESTS)} tests.")

if __name__ == "__main__":
    _run_tests()
