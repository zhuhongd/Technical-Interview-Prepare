"""
========================================================
EECS4080 — Pattern-Based Interview Preparation
========================================================

Problem: Design a Data Structure for TwoSum Queries
---------------------------------------------------
Design a data structure that accepts a stream of integers and checks if 
it has a pair of integers that sum up to a particular value.

Implement the TwoSum class:

- TwoSum() -> Initializes the TwoSum object, with an empty array initially.
- add(int number) -> Adds number to the data structure.
- find(int value) -> Returns True if there exists any pair of numbers 
  whose sum is equal to value, otherwise False.

Example 1:
----------
Input:
["TwoSum", "add", "add", "add", "find", "find"]
[[], [1], [3], [5], [4], [7]]

Output:
[null, null, null, null, true, false]

Explanation:
TwoSum twoSum = new TwoSum()
twoSum.add(1)   # [] --> [1]
twoSum.add(3)   # [1] --> [1,3]
twoSum.add(5)   # [1,3] --> [1,3,5]
twoSum.find(4)  # 1 + 3 = 4 -> return True
twoSum.find(7)  # No two integers sum up to 7 -> return False

Constraints:
------------
- 10^(-5) <= number <= 10^5
- -2^31 <= value <= 2^31 - 1
- At most 10^4 calls will be made to add and find.

--------------------------------------------------------
Key Examples
--------------------------------------------------------
nums = [1,3,5]
find(4) -> True   # (1 + 3)
find(7) -> False  # no valid pair
find(2) -> False  # needs two "1"s
add(1)  -> now nums = [1,3,5,1]
find(2) -> True   # (1 + 1)

--------------------------------------------------------
Beginner Intuition
--------------------------------------------------------
The naive way: keep appending numbers into a list. 
When asked to "find", check every pair (O(n^2)).

But that’s too slow for many queries. We want faster lookups.

Observation:
- If I know the counts of each number, then for each `x` 
  I can ask "is (value - x) in my store?"
- If it's the same number (x == value - x), 
  I need at least two copies.

--------------------------------------------------------
Approach Overview
--------------------------------------------------------
We use a dictionary (hashmap) to store:
- key   = number
- value = how many times it's been added

On find(value):
- Loop through all numbers
- Check if the complement exists
- Special-case when complement == number (needs >= 2 copies)

Complexity:
-----------
- add: O(1)
- find: O(n)  (where n = # of distinct numbers)

This is acceptable for <= 10^4 operations.

--------------------------------------------------------
Implementation
--------------------------------------------------------
"""

from collections import defaultdict

class TwoSum:
    def __init__(self):
        # store[number] = count of how many times number has been added
        self.store = defaultdict(int)

    def add(self, number: int) -> None:
        """Add number to the data structure."""
        self.store[number] += 1

    def find(self, value: int) -> bool:
        """
        Return True if there exists any pair (x,y) 
        with x + y == value.
        """
        for number, count in self.store.items():
            complement = value - number
            # Case 1: different numbers (e.g., 1 + 3 = 4)
            if complement in self.store and complement != number:
                return True
            # Case 2: same number must appear at least twice
            if complement == number and count > 1:
                return True
        return False


"""
--------------------------------------------------------
Tests
--------------------------------------------------------
"""

if __name__ == "__main__":
    ts = TwoSum()
    ts.add(1)
    ts.add(3)
    ts.add(5)
    print("find(4) ->", ts.find(4), "expected True")   # 1 + 3
    print("find(7) ->", ts.find(7), "expected False")  # no pair
    print("find(2) ->", ts.find(2), "expected False")  # needs 2 copies of 1
    ts.add(1)
    print("find(2) ->", ts.find(2), "expected True")   # 1 + 1 now possible

