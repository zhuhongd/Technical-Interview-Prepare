r"""
LRU Cache — EECS4070 (OrderedDict Solution, with Teaching Before & After)

Problem
-------
Implement an LRU (Least Recently Used) cache with operations:
- LRUCache(capacity): initialize with positive capacity.
- get(key): return value if present, else -1. Access marks the key as most‑recently‑used (MRU).
- put(key, value): insert or update and mark MRU. If size exceeds capacity, evict the least‑recently‑used (LRU).

Both get and put must be **O(1)** average time.

Link
----
https://leetcode.com/problems/lru-cache/

Key Example
-----------
Example A (from prompt)
Input Ops : ["LRUCache", [2], "put", [1,10], "get", [1], "put", [2,20], "put", [3,30], "get", [2], "get", [1]]
Expected  : [None, None, None, 10, None, None, 20, -1]

Trace (keys in cache, left=Lru, right=Mru):
  put(1,10)   -> [1]
  get(1)=10   -> [1]
  put(2,20)   -> [1,2]
  put(3,30)   -> [2,3]   (evict 1)
  get(2)=20   -> [3,2]
  get(1)=-1   -> [3,2]

Beginner Intuition
------------------
We want **O(1)** access/update and eviction by LRU. Python’s `OrderedDict` already maintains insertion order,
with methods to *move* an entry to the end (MRU) and *pop* from the start (LRU). By using this, we can solve the
problem concisely while still reasoning about why it works.

Approach (Using OrderedDict)
----------------------------
- Keep cache in an `OrderedDict` mapping key -> value.
- For any **get**:
    - If key missing, return -1.
    - If present, move it to end (MRU) and return its value.
- For any **put**:
    - If key already present, update value and move to end (MRU).
    - Else, if capacity full, evict least-recent (first item).
    - Insert key at end (MRU).

Complexity
----------
Time: **O(1)** average per get/put (dict + OrderedDict operations).  Space: **O(capacity)**.

Common Pitfalls
---------------
- Forgetting to `move_to_end` on **get** means recency order breaks.
- Using `popitem(last=True)` instead of `last=False` will remove MRU instead of LRU.
"""

from collections import OrderedDict
from typing import List, Tuple, Any

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_store = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.cache_store:
            self.cache_store.move_to_end(key, last=True)
            return self.cache_store[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache_store:
            self.cache_store[key] = value
            self.cache_store.move_to_end(key, last=True)
        else:
            if len(self.cache_store) >= self.capacity:
                self.cache_store.popitem(last=False)
            self.cache_store[key] = value


# -----------------------------
# Clear Offline Tests
# -----------------------------

def _run_tests() -> None:
    def run_case(ops: List[str], args: List[Tuple[Any,...]], expected: List[Any], label: str):
        print(f"\n[{label}] ======================")
        obj = None
        out: List[Any] = []
        for op, ar in zip(ops, args):
            if op == "LRUCache":
                obj = LRUCache(*ar)
                out.append(None)
                print(f"init cap={ar[0]}")
            elif op == "put":
                obj.put(*ar)  # type: ignore
                out.append(None)
                print(f"put{ar}")
            elif op == "get":
                val = obj.get(*ar)  # type: ignore
                out.append(val)
                print(f"get{ar} -> {val}")
        print("expected:", expected)
        print("got     :", out)
        print("result  :", "✅" if out == expected else "❌")

    # Test 1: Prompt example
    ops1  = ["LRUCache","put","get","put","put","get","get"]
    args1 = [(2,), (1,10), (1,), (2,20), (3,30), (2,), (1,)]
    expected1 = [None, None, 10, None, None, 20, -1]
    run_case(ops1, args1, expected1, "prompt-example")

    # Test 2: Capacity=1
    ops2  = ["LRUCache","put","put","get","put","get","get"]
    args2 = [(1,), (1,1), (2,2), (1,), (3,3), (2,), (3,)]
    expected2 = [None, None, None, -1, None, -1, 3]
    run_case(ops2, args2, expected2, "capacity-1")

    # Test 3: Update existing key moves MRU
    ops3  = ["LRUCache","put","put","put","get","put","get","get"]
    args3 = [(2,), (1,1), (2,2), (1,9), (2,), (3,3), (1,), (3,)]
    expected3 = [None, None, None, None, 2, None, -1, 3]
    run_case(ops3, args3, expected3, "update-mru")

    # Test 4: Recency by gets
    ops4  = ["LRUCache","put","put","get","get","put","get","get"]
    args4 = [(2,), (1,1), (2,2), (1,), (1,), (3,3), (1,), (2,)]
    expected4 = [None, None, None, 1, 1, None, 1, -1]
    run_case(ops4, args4, expected4, "recency-by-get")

if __name__ == "__main__":
    _run_tests()
