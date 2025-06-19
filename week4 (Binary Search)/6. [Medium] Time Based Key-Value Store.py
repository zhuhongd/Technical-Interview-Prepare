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
