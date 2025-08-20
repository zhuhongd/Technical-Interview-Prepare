# car_fleet_explained.py

"""
Problem: Car Fleet (week 2)

There are n cars on a one-lane road heading toward the same destination. A car can:
- Catch up to another car ahead of it and become part of the same "fleet"
- Never pass another car once it has caught up

Given:
- position[i] = the starting position of the i-th car
- speed[i] = the speed of the i-th car
- target = the destination position

Return:
The number of distinct car fleets that will arrive at the destination.
"""

from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # your solution here
        return


# Sample test block
if __name__ == "__main__":
    test_cases = [
        # Each test is (target, position, speed, expected_output)
        (10, [1, 4], [3, 2], 1),
        (10, [4, 1, 0, 7], [2, 2, 1, 1], 3),
        (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3),
        (100, [0, 2, 4], [4, 2, 1], 1),
        (15, [1, 3, 5, 7], [4, 3, 2, 1], 4),  # All same time
    ]

    for target, pos, spd, expected in test_cases:
        result = Solution().carFleet(target, pos, spd)
        print(f"Input: target={target}, position={pos}, speed={spd}")
        print(f"Output: {result} | Expected: {expected}")
        print("✅ Pass\n" if result == expected else "❌ Fail\n")
