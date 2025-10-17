r"""
=========================================================
Design Parking System — EECS4070 (Explained, Readable OOP)
=========================================================

Problem
-------
You manage a parking lot with three types of spots:
  • big, medium, and small

At construction time, you’re given how many spots exist for each type.
Cars arrive one at a time with a type code:
  1 = big, 2 = medium, 3 = small

Implement a class:
  - ParkingSystem(big, medium, small)
  - addCar(carType) -> bool
      * If there’s at least one empty spot of that type, park the car,
        reduce the available count, and return True.
      * Otherwise return False.

Link
----
https://leetcode.com/problems/design-parking-system/  (LeetCode 1603)

Key Example
-----------
Initialize: ParkingSystem(1, 1, 0)
Calls:
  addCar(1) -> True    # big spot used (now 0 left)
  addCar(2) -> True    # medium spot used (now 0 left)
  addCar(3) -> False   # no small spots available
  addCar(1) -> False   # big is already full

Beginner Intuition
------------------
We just need to keep **counts** of available spots for each type.
Whenever `addCar(t)` is called:
  - Check if `count[t] > 0`
  - If yes, decrement and return True; else return False.
That’s it — this is a counters/encapsulation exercise.

Approach Overview
-----------------
1) Store available slots in a simple list or dict:
     index 1 -> big, 2 -> medium, 3 -> small
2) On `addCar(t)`, check availability, update, return True/False.

Complexity
----------
• Time:  O(1) per operation
• Space: O(1) (only three counters)
=========================================================
"""

from typing import List


class ParkingSystem:
    """
    A simple parking system that tracks available counts for
    big (1), medium (2), and small (3) car slots.
    """

    def __init__(self, big: int, medium: int, small: int) -> None:
        # Use a 4-length list so indices 1..3 map directly to carType.
        # Index 0 is unused for readability.
        self.available: List[int] = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        """
        Try to park a car of the given type.
        Returns True if a spot was available (and is now taken),
        otherwise False.
        """
        # Validate carType (defensive programming for robustness in teaching files)
        if carType < 1 or carType > 3:
            return False

        if self.available[carType] > 0:
            self.available[carType] -= 1
            return True
        return False


# ----------------------------------------------------------
# (Optional) Alternate design (commented out for one-active-solution rule)
# ----------------------------------------------------------
# class ParkingSystemDict:
#     def __init__(self, big: int, medium: int, small: int) -> None:
#         self.available = {1: big, 2: medium, 3: small}
#     def addCar(self, carType: int) -> bool:
#         if carType not in self.available:  # defensive
#             return False
#         if self.available[carType] > 0:
#             self.available[carType] -= 1
#             return True
#         return False


# ==========================================================
# 🧪 Offline Tests (Readable Logs)
# ==========================================================
def _run_tests() -> None:
    print("==== Basic Walkthrough ====")
    ps = ParkingSystem(1, 1, 0)
    print("addCar(1) ->", ps.addCar(1), "   # expect True (big:1->0)")
    print("addCar(2) ->", ps.addCar(2), "   # expect True (med:1->0)")
    print("addCar(3) ->", ps.addCar(3), "   # expect False (small:0)")
    print("addCar(1) ->", ps.addCar(1), "   # expect False (big already full)")

    print("\n==== Edge / Robustness ====")
    ps2 = ParkingSystem(0, 2, 3)
    # Fill all medium
    print("addCar(2) ->", ps2.addCar(2), "   # True  (med:2->1)")
    print("addCar(2) ->", ps2.addCar(2), "   # True  (med:1->0)")
    print("addCar(2) ->", ps2.addCar(2), "   # False (med:0)")
    # Fill three small
    for i in range(1, 5):
        print(f"addCar(3) attempt {i} ->", ps2.addCar(3), "   # True, True, True, then False")
    # Invalid type (defensive)
    print("addCar(0) ->", ps2.addCar(0), "       # False (invalid type)")
    print("addCar(4) ->", ps2.addCar(4), "       # False (invalid type)")

    print("\n==== Fresh Instance Sanity ====")
    ps3 = ParkingSystem(2, 0, 1)
    print("addCar(1) ->", ps3.addCar(1), "   # True  (big:2->1)")
    print("addCar(1) ->", ps3.addCar(1), "   # True  (big:1->0)")
    print("addCar(1) ->", ps3.addCar(1), "   # False (big:0)")
    print("addCar(3) ->", ps3.addCar(3), "   # True  (small:1->0)")
    print("addCar(3) ->", ps3.addCar(3), "   # False (small:0)")
    print("addCar(2) ->", ps3.addCar(2), "   # False (medium:0)")


if __name__ == "__main__":
    _run_tests()


r"""
=========================================================
✅ Sample Output
---------------------------------------------------------
==== Basic Walkthrough ====
addCar(1) -> True    # expect True (big:1->0)
addCar(2) -> True    # expect True (med:1->0)
addCar(3) -> False   # expect False (small:0)
addCar(1) -> False   # expect False (big already full)

==== Edge / Robustness ====
addCar(2) -> True    # True  (med:2->1)
addCar(2) -> True    # True  (med:1->0)
addCar(2) -> False   # False (med:0)
addCar(3) attempt 1 -> True    # True, True, True, then False
addCar(3) attempt 2 -> True    # True, True, True, then False
addCar(3) attempt 3 -> True    # True, True, True, then False
addCar(3) attempt 4 -> False   # True, True, True, then False
addCar(0) -> False             # False (invalid type)
addCar(4) -> False             # False (invalid type)

==== Fresh Instance Sanity ====
addCar(1) -> True
addCar(1) -> True
addCar(1) -> False
addCar(3) -> True
addCar(3) -> False
addCar(2) -> False

=========================================================
Complexity Recap
---------------------------------------------------------
• addCar: O(1)
• Space:  O(1)
=========================================================
"""
