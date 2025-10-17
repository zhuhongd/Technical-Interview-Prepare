r"""
=========================================================
Design LFU Cache — EECS4070 (Explained, O(1) Get/Put)
=========================================================

Problem
-------
Implement an LFU (Least Frequently Used) cache with:
  • get(key)  -> int
  • put(key, value) -> None

Rules:
  1) Evict the item with the **lowest frequency**.
  2) If multiple items share the same lowest frequency, evict the **LRU**
     (least recently used among that frequency).
  3) get/put should be **O(1)** average time.
  4) If capacity = 0, the cache stores nothing.

Link
----
https://leetcode.com/problems/lfu-cache/

Key Example
-----------
LFUCache(2)
put(1, 10)      # cache={1:10}
put(2, 20)      # cache={1:10, 2:20}
get(1) -> 10    # freq(1)=2, freq(2)=1
put(3, 30)      # capacity full; evict key=2 (freq=1 LRU), add 3
get(2) -> -1    # not found
get(3) -> 30    # freq(3)=2
put(4, 40)      # full; now keys: {1:freq=2,3:freq=2}; LRU among freq=2 is key=1
                # evict 1, add 4
get(1) -> -1
get(3) -> 30
get(4) -> 40

Beginner Intuition
------------------
We must track two things at once:
  • How OFTEN a key is used (frequency)
  • For ties, which was used most recently (LRU within a frequency)

A standard O(1) pattern:
  - Maintain a dict: key -> Node(value, freq, and pointers)
  - Maintain a dict: freq -> doubly linked list (DLL) of nodes
      * DLL head = most recent, tail = least recent in that frequency
  - Track the current minimum frequency `min_freq`
  - On get/put:
      * Move the node from its old freq list to (freq+1) list.
      * Update `min_freq` if needed.
  - On eviction:
      * Remove from the TAIL of the DLL for `min_freq`.

Approach Overview
-----------------
Data structures:
  - key_to_node: {key -> Node(key, value, freq)}
  - freq_to_list: {freq -> DLinkedList of Node}
  - min_freq: current minimum frequency in the cache
  - capacity: max items allowed

Complexity
----------
• get: O(1)
• put: O(1)
• Space: O(capacity)
=========================================================
"""

from __future__ import annotations
from typing import Optional, Dict


# -----------------------------
# Doubly Linked List Node
# -----------------------------
class Node:
    def __init__(self, key: int, value: int, freq: int = 1) -> None:
        self.key = key
        self.value = value
        self.freq = freq
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


# -----------------------------
# Doubly Linked List for a frequency bucket
# head = most recent, tail = least recent
# -----------------------------
class DLinkedList:
    def __init__(self) -> None:
        self.head = Node(0, 0)  # dummy
        self.tail = Node(0, 0)  # dummy
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def push_front(self, node: Node) -> None:
        """Insert node right after head (most recent position)."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def pop(self, node: Optional[Node] = None) -> Node:
        """
        Remove and return the given node.
        If node is None, remove the least recent (tail.prev).
        """
        if self.size == 0:
            raise IndexError("pop from empty DLinkedList")

        if node is None:
            node = self.tail.prev

        # unlink node
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = node.next = None
        self.size -= 1
        return node


# -----------------------------
# LFU Cache
# -----------------------------
class LFUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.size = 0

        self.key_to_node: Dict[int, Node] = {}
        self.freq_to_list: Dict[int, DLinkedList] = {}
        self.min_freq = 0

    def _touch(self, node: Node) -> None:
        """
        Increase node's frequency and move it to the front of the new freq list.
        Update min_freq if we emptied the old list and it was the min.
        """
        old_freq = node.freq
        old_list = self.freq_to_list[old_freq]
        old_list.pop(node)

        # if that freq bucket is now empty and it was min_freq -> bump min_freq
        if old_freq == self.min_freq and len(old_list) == 0:
            self.min_freq += 1

        # add to new freq bucket
        node.freq += 1
        new_freq = node.freq
        new_list = self.freq_to_list.get(new_freq)
        if new_list is None:
            new_list = self.freq_to_list[new_freq] = DLinkedList()
        new_list.push_front(node)

    def get(self, key: int) -> int:
        """
        Return value if key exists; otherwise -1.
        Also increases key's frequency and updates its recency (move to front).
        """
        node = self.key_to_node.get(key)
        if node is None:
            return -1
        self._touch(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Insert or update (key, value).
        If capacity is 0, do nothing.
        If insert causes overflow, evict LFU (and LRU among ties).
        """
        if self.capacity == 0:
            return

        # Update existing node
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.value = value
            self._touch(node)
            return

        # Evict if at capacity
        if self.size == self.capacity:
            # evict from min_freq list (tail = least recent)
            lfu_list = self.freq_to_list[self.min_freq]
            evicted = lfu_list.pop()   # least recent in the LFU bucket
            del self.key_to_node[evicted.key]
            self.size -= 1

        # Insert new node with freq=1
        node = Node(key, value, freq=1)
        self.key_to_node[key] = node
        freq1_list = self.freq_to_list.get(1)
        if freq1_list is None:
            freq1_list = self.freq_to_list[1] = DLinkedList()
        freq1_list.push_front(node)

        # reset min_freq to 1 because we just added a freq=1 item
        self.min_freq = 1
        self.size += 1


# ==========================================================
# 🧪 Offline Tests (Readable Logs)
# ==========================================================
def _run_tests() -> None:
    print("==== Example Walkthrough (LeetCode-like) ====")
    cache = LFUCache(2)
    cache.put(1, 10)
    cache.put(2, 20)
    print("get(1) ->", cache.get(1), "   # expect 10 (freq(1)=2)")
    cache.put(3, 30)  # evict key=2 (freq=1, LRU)
    print("get(2) ->", cache.get(2), "   # expect -1 (evicted)")
    print("get(3) ->", cache.get(3), "   # expect 30 (freq(3)=2)")
    cache.put(4, 40)  # evict among min-freq; keys 1 and 3 both freq=2 -> evict LRU (key=1)
    print("get(1) ->", cache.get(1), "   # expect -1 (evicted)")
    print("get(3) ->", cache.get(3), "   # expect 30")
    print("get(4) ->", cache.get(4), "   # expect 40")

    print("\n==== Capacity 0 Edge Case ====")
    zero = LFUCache(0)
    zero.put(1, 1)   # ignored
    print("get(1) ->", zero.get(1), "   # expect -1 (capacity=0)")

    print("\n==== Update Value + Touch ====")
    c = LFUCache(2)
    c.put(5, 50)
    c.put(6, 60)
    c.put(5, 500)  # update existing (touch 5 to freq=2)
    print("get(5) ->", c.get(5), "   # expect 500")
    c.put(7, 70)   # evict key=6 (freq(6)=1), keep 5 (freq=2)
    print("get(6) ->", c.get(6), "   # expect -1")
    print("get(7) ->", c.get(7), "   # expect 70")
    print("get(5) ->", c.get(5), "   # expect 500")


if __name__ == "__main__":
    _run_tests()


r"""
=========================================================
✅ Sample Output
---------------------------------------------------------
==== Example Walkthrough (LeetCode-like) ====
get(1) -> 10    # expect 10 (freq(1)=2)
get(2) -> -1    # expect -1 (evicted)
get(3) -> 30    # expect 30 (freq(3)=2)
get(1) -> -1    # expect -1 (evicted)
get(3) -> 30    # expect 30
get(4) -> 40    # expect 40

==== Capacity 0 Edge Case ====
get(1) -> -1    # expect -1 (capacity=0)

==== Update Value + Touch ====
get(5) -> 500   # expect 500
get(6) -> -1    # expect -1
get(7) -> 70    # expect 70
get(5) -> 500   # expect 500
---------------------------------------------------------

Complexity Recap
---------------------------------------------------------
• get: O(1)      (move node between freq buckets)
• put: O(1)      (evict from min_freq tail; insert at head of freq=1)
• Space: O(capacity)
=========================================================
"""
