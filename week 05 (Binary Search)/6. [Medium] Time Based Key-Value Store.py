"""
Problem: Time Based Key-Value Store

Design a class that supports storing multiple values for the same key with timestamps,
and retrieving the value at a specific timestamp.

You must implement the following:

1️⃣ TimeMap() → Initializes the object
2️⃣ set(key, value, timestamp) → Stores the key with value at given timestamp
3️⃣ get(key, timestamp) → Returns the value at the most recent timestamp 
                          that is <= given timestamp. If no such value exists, return ""

Note: All timestamps in `set` are strictly increasing.

Example:
Input:
["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2],
 "set", ["alice", "sad", 3], "get", ["alice", 3]]
Output:
[null, null, "happy", "happy", null, "sad"]

Constraints:
- key and value contain only lowercase letters and digits
- 1 <= key.length, value.length <= 100
- 1 <= timestamp <= 1000

🔗 Link: https://neetcode.io/problems/time-based-key-value-store
"""

# ✅ Approach:
# For each key, we store a list of (timestamp, value) pairs.
# Because timestamps are strictly increasing, the list is sorted.

# For get(key, timestamp):
#    ➤ Use binary search to find the largest timestamp <= the given timestamp.
#    ➤ This keeps the time complexity to O(log n) per query.

# Example:
# "alice": [(1, "happy"), (3, "sad")]
# get("alice", 2) → use binary search → return "happy"
# get("alice", 3) → exact match → return "sad"
# get("alice", 0) → no valid timestamp ≤ 0 → return ""

import bisect

class TimeMap:
    def __init__(self):
        # Store data as: key -> list of (timestamp, value)
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        time_list = self.store[key]
        # Binary search on timestamp
        left, right = 0, len(time_list) - 1
        res = ""

        while left <= right:
            mid = (left + right) // 2
            if time_list[mid][0] <= timestamp:
                res = time_list[mid][1]   # potential answer
                left = mid + 1           # try to find a later one
            else:
                right = mid - 1

        return res
# ==========================================================
# ✅ Assert-Based Tests — Time Based Key-Value Store (fixed)
# ==========================================================
def _run_tests_assert() -> None:
    print("==== Running TimeMap Tests ====")

    tm = TimeMap()
    ctx = {}  # holds tm2, tm3, tm4 across lambdas

    tests = [
        # --- Example from prompt ---
        (lambda: (tm.set("alice", "happy", 1), None)[1], None, "set(alice,happy,1)"),
        (lambda: tm.get("alice", 1), "happy", "get(alice,1 exact)"),
        (lambda: tm.get("alice", 2), "happy", "get(alice,2 after 1)"),
        (lambda: (tm.set("alice", "sad", 3), None)[1], None, "set(alice,sad,3)"),
        (lambda: tm.get("alice", 3), "sad", "get(alice,3 exact)"),
        (lambda: tm.get("alice", 0), "", "get(alice,0 before first)"),

        # --- Multiple keys (persist via ctx['tm2']) ---
        (lambda: (ctx.update({'tm2': TimeMap()}),
                  ctx['tm2'].set("a", "x", 1),
                  ctx['tm2'].set("b", "y", 2),
                  ctx['tm2'].set("a", "z", 3),
                  None)[-1], None, "init multi-key"),
        (lambda: ctx['tm2'].get("a", 1), "x", "multi-key get a@1"),
        (lambda: ctx['tm2'].get("a", 2), "x", "multi-key get a@2"),
        (lambda: ctx['tm2'].get("a", 3), "z", "multi-key get a@3"),
        (lambda: ctx['tm2'].get("b", 2), "y", "multi-key get b@2"),
        (lambda: ctx['tm2'].get("b", 3), "y", "multi-key get b@3"),

        # --- Edge cases (persist via ctx['tm3']) ---
        (lambda: (ctx.update({'tm3': TimeMap()}),
                  ctx['tm3'].set("cat", "sleep", 10),
                  None)[-1], None, "edge init"),
        (lambda: ctx['tm3'].get("cat", 10), "sleep", "get(cat,10 exact)"),
        (lambda: ctx['tm3'].get("cat", 5), "", "get(cat,5 before first)"),
        (lambda: ctx['tm3'].get("dog", 10), "", "get(dog,10 nonexistent key)"),
        (lambda: (ctx['tm3'].set("cat", "eat", 12),
                  ctx['tm3'].set("cat", "run", 15),
                  None)[-1], None, "set additional"),
        (lambda: ctx['tm3'].get("cat", 11), "sleep", "get(cat,11 before 12)"),
        (lambda: ctx['tm3'].get("cat", 12), "eat", "get(cat,12 exact)"),
        (lambda: ctx['tm3'].get("cat", 13), "eat", "get(cat,13 between 12&15)"),
        (lambda: ctx['tm3'].get("cat", 15), "run", "get(cat,15 exact)"),
        (lambda: ctx['tm3'].get("cat", 20), "run", "get(cat,20 after last)"),

        # --- Sequential inserts (persist via ctx['tm4']) ---
        (lambda: (ctx.update({'tm4': TimeMap()}),
                  [ctx['tm4'].set("temp", f"v{t}", t) for t in range(1, 6)],
                  None)[-1], None, "sequential init"),
        (lambda: ctx['tm4'].get("temp", 0), "", "get(temp,0 before all)"),
        (lambda: ctx['tm4'].get("temp", 1), "v1", "get(temp,1 exact)"),
        (lambda: ctx['tm4'].get("temp", 3), "v3", "get(temp,3 exact)"),
        (lambda: ctx['tm4'].get("temp", 5), "v5", "get(temp,5 exact)"),
        (lambda: ctx['tm4'].get("temp", 6), "v5", "get(temp,6 after all)"),
    ]

    passed = 0
    for i, (fn, expected, label) in enumerate(tests, 1):
        try:
            result = fn()
            if expected is None:  # setup steps
                print(f"[{i:02d}] {label:<35} ⚙️ SETUP OK")
                passed += 1
            else:
                assert result == expected
                print(f"[{i:02d}] {label:<35} ✅ PASS (got {result!r})")
                passed += 1
        except AssertionError:
            print(f"[{i:02d}] {label:<35} ❌ FAIL (got {result!r}, expected {expected!r})")
        except Exception as e:
            print(f"[{i:02d}] {label:<35} ⚠️ ERROR ({type(e).__name__}: {e})")

    print(f"\nTotal: {passed}/{len(tests)} passed ✅")


if __name__ == "__main__":
    _run_tests_assert()
