r"""
Design Singly Linked List — EECS4070 (Explained, Tests)

Problem
-------
Implement a **singly linked list** with these operations:

- LinkedList()         : initialize an empty list
- get(i)               : return value at index i (0-indexed); if OOB, return -1
- insertHead(val)      : insert new node with val at the **head**
- insertTail(val)      : insert new node with val at the **tail**
- remove(i)            : remove node at index i; return True if success else False
- getValues()          : return Python list of values from head → tail

Link
----
https://neetcode.io/problems/singlyLinkedList

Beginner Intuition
------------------
Each element is a `ListNode(value, next)`. The list tracks only the **head**.
To access the i-th node, walk from head, counting steps until i.
To insert at head, make a new node that points to the current head and move head there.
To insert at tail, traverse to the end and attach the new node.
To remove the i-th node, find the (i-1)-th node and bypass its next.

Operations & Complexity
-----------------------
- get(i)          : O(n)        (walk i steps)
- insertHead(val) : O(1)
- insertTail(val) : O(n)        (no tail pointer; walk to last)
- remove(i)       : O(n)        (walk to (i-1)-th)
- getValues()     : O(n)
Space             : O(n)        (n nodes)

Common Pitfalls
---------------
- Not returning -1 when `get(i)` is out of bounds.
- Forgetting to update `head` when removing index 0.
- Off-by-one in remove (you must stop at the (i-1)-th node to relink).
- Not handling the empty-list case in get/remove/insertTail.

Key Examples
------------
Example 1
~~~~~~~~~
ll = LinkedList()
ll.insertHead(1)      # List: 1
ll.insertTail(2)      # List: 1 -> 2
ll.insertHead(0)      # List: 0 -> 1 -> 2
ll.remove(1)          # Removes '1' -> List: 0 -> 2
ll.getValues()        # [0, 2]

Example 2
~~~~~~~~~
ll = LinkedList()
ll.insertHead(2)      # List: 2
ll.insertHead(1)      # List: 1 -> 2
ll.get(5)             # -1 (out of bounds)

Interview Tips
--------------
- Mention you kept only a head pointer (so insertTail is O(n)); you could add a
  tail pointer for O(1) tail inserts if needed.
- Returning a boolean from `remove` is helpful to signal success/failure.
- Keep your traversal code tight and guard all edge cases (empty list, index 0).
"""


from __future__ import annotations
from typing import Optional, List, Tuple, Any


# -----------------------------
# Core data structures
# -----------------------------
class ListNode:
    def __init__(self, value: int, next_node: Optional["ListNode"] = None) -> None:
        self.value = value
        self.next: Optional[ListNode] = next_node

    def __repr__(self) -> str:
        return f"ListNode({self.value})"


class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[ListNode] = None

    # -------------------------
    # Queries
    # -------------------------
    def get(self, index: int) -> int:
        """
        Return value at 0-based index; return -1 if out of bounds.
        """
        i = 0
        cur = self.head
        while cur is not None:
            if i == index:
                return cur.value
            cur = cur.next
            i += 1
        return -1

    def getValues(self) -> List[int]:
        """
        Return Python list of values from head → tail.
        """
        vals: List[int] = []
        cur = self.head
        while cur is not None:
            vals.append(cur.value)
            cur = cur.next
        return vals

    # -------------------------
    # Updates
    # -------------------------
    def insertHead(self, val: int) -> None:
        """
        Insert new node at head in O(1).
        """
        self.head = ListNode(val, self.head)

    def insertTail(self, val: int) -> None:
        """
        Insert new node at tail. O(n) since we have no tail pointer.
        """
        node = ListNode(val)
        if self.head is None:
            self.head = node
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = node

    def remove(self, index: int) -> bool:
        """
        Remove node at 0-based index. Return True if success, False if OOB.
        """
        if self.head is None:
            return False

        if index == 0:
            self.head = self.head.next
            return True

        cur = self.head
        # stop at (index - 1)-th node
        for _ in range(index - 1):
            if cur.next is None:
                return False  # index out of bounds
            cur = cur.next

        # now cur is (index-1)-th; cur.next should be the target
        if cur.next is None:
            return False  # index out of bounds
        cur.next = cur.next.next
        return True

    # -------------------------
    # Pretty printer (optional)
    # -------------------------
    def __str__(self) -> str:
        parts: List[str] = []
        cur = self.head
        while cur is not None:
            parts.append(str(cur.value))
            cur = cur.next
        return " -> ".join(parts) if parts else "(empty)"


# -----------------------------
# Teaching walkthrough
# -----------------------------
def _walkthrough() -> None:
    print("Walkthrough 1:")
    ll = LinkedList()
    ll.insertHead(1)   # 1
    ll.insertTail(2)   # 1 -> 2
    ll.insertHead(0)   # 0 -> 1 -> 2
    print("  after inserts:", ll)
    ll.remove(1)       # remove value '1' at index 1
    print("  after remove(1):", ll)
    print("  getValues():", ll.getValues())
    print("  get(0):", ll.get(0), "get(1):", ll.get(1), "get(2):", ll.get(2), "\n")

    print("Walkthrough 2:")
    ll2 = LinkedList()
    ll2.insertHead(2)  # 2
    ll2.insertHead(1)  # 1 -> 2
    print("  list:", ll2)
    print("  get(5) (OOB):", ll2.get(5), "\n")


# -----------------------------
# Simple operation runner for tests
# -----------------------------
def _run_sequence(ops: List[Tuple[str, Tuple[Any, ...]]]) -> List[Any]:
    """
    Helper for tests. Run a sequence of (method_name, args) on a new LinkedList.
    Returns a list of method results (for void methods we append None).
    """
    ll = LinkedList()
    out: List[Any] = []
    for name, args in ops:
        fn = getattr(ll, name)
        res = fn(*args)
        out.append(res)
    return out


# -----------------------------
# Comprehensive offline tests
# -----------------------------
def _run_tests() -> None:
    print("Running tests...\n")

    # 1) Basic sequences check return values and final getValues()
    TESTS_SEQ = [
        # (ops, expected_results, label)
        (
            [
                ("insertHead", (1,)),     # [1]
                ("insertTail", (2,)),     # [1,2]
                ("insertHead", (0,)),     # [0,1,2]
                ("getValues",  ()),       # -> [0,1,2]
                ("get",        (0,)),     # -> 0
                ("get",        (2,)),     # -> 2
                ("get",        (3,)),     # -> -1
                ("remove",     (1,)),     # remove '1' -> [0,2]
                ("getValues",  ()),       # -> [0,2]
            ],
            [None, None, None, [0,1,2], 0, 2, -1, True, [0,2]],
            "example-1-seq",
        ),
        (
            [
                ("get",        (0,)),     # empty -> -1
                ("remove",     (0,)),     # empty -> False
                ("insertTail", (5,)),     # [5]
                ("remove",     (1,)),     # OOB -> False
                ("remove",     (0,)),     # remove head -> []
                ("getValues",  ()),       # -> []
            ],
            [-1, False, None, False, True, []],
            "edge-empty-and-removes",
        ),
        (
            [
                ("insertTail", (1,)),     # [1]
                ("insertTail", (2,)),     # [1,2]
                ("insertTail", (3,)),     # [1,2,3]
                ("remove",     (2,)),     # remove tail -> [1,2]
                ("remove",     (1,)),     # remove new tail -> [1]
                ("remove",     (0,)),     # remove head -> []
                ("getValues",  ()),       # -> []
            ],
            [None, None, None, True, True, True, []],
            "remove-tail-steps",
        ),
        (
            [
                ("insertHead", (3,)),     # [3]
                ("insertHead", (2,)),     # [2,3]
                ("insertHead", (1,)),     # [1,2,3]
                ("getValues",  ()),       # -> [1,2,3]
                ("remove",     (5,)),     # OOB -> False
                ("remove",     (2,)),     # remove '3' -> [1,2]
                ("getValues",  ()),       # -> [1,2]
                ("get",        (1,)),     # -> 2
            ],
            [None, None, None, [1,2,3], False, True, [1,2], 2],
            "head-build-then-remove",
        ),
    ]

    passed = 0
    for i, (ops, expected, label) in enumerate(TESTS_SEQ, 1):
        got = _run_sequence(ops)
        ok = (got == expected)
        passed += ok
        print(f"[{i:02d}][{label:<22}]")
        print(f"  got      = {got}")
        print(f"  expected = {expected}  -> {'✅' if ok else '❌'}\n")

    # 2) Property-style sanity checks
    # After a sequence of inserts at head (0..n-1), getValues should be reversed order of insert.
    print("[P1] insertHead order property")
    ll = LinkedList()
    for x in range(5):  # insert 0..4 at head -> list becomes 4..0
        ll.insertHead(x)
    got_vals = ll.getValues()
    expected_vals = [4, 3, 2, 1, 0]
    ok = (got_vals == expected_vals)
    passed += ok
    print(f"  list      = {ll}")
    print(f"  getValues = {got_vals}, expected {expected_vals} -> {'✅' if ok else '❌'}\n")

    # After inserting at tail 1..5, we should get [1..5]
    print("[P2] insertTail order property")
    ll2 = LinkedList()
    for x in range(1, 6):
        ll2.insertTail(x)
    got_vals2 = ll2.getValues()
    expected_vals2 = [1, 2, 3, 4, 5]
    ok2 = (got_vals2 == expected_vals2)
    passed += ok2
    print(f"  list      = {ll2}")
    print(f"  getValues = {got_vals2}, expected {expected_vals2} -> {'✅' if ok2 else '❌'}\n")

    total = len(TESTS_SEQ) + 2
    print(f"Passed {passed}/{total} checks.")


if __name__ == "__main__":
    _walkthrough()
    _run_tests()
