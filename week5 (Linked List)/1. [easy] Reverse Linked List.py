r"""
Reverse Linked List — EECS4070 (Explained, Multiple Approaches + Tests)

Problem
-------
Given the head of a singly linked list, **reverse** the list and return the new head.

Link
----
https://neetcode.io/problems/reverse-a-linked-list?list=neetcode150

Key Examples
------------
Example 1
~~~~~~~~~
Input : head = [0, 1, 2, 3]
Output: [3, 2, 1, 0]

Example 2
~~~~~~~~~
Input : head = []
Output: []

Beginner Intuition
------------------
A singly linked list only points **forward**. To reverse it, walk the list and
flip each `.next` pointer to point **backward**. Keep 3 pointers:

- `prev`: node that should come **before** the current node in the reversed list
- `curr`: current node we’re processing
- `nxt` : original `curr.next` (so we don’t lose the rest of the list)

Process:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt

When `curr` becomes None, `prev` is the new head.

Complexity
----------
Time : O(n)   (touch each node once)
Space: O(1)   (in-place; just 3 pointers)

Common Mistakes
---------------
- Forgetting to set the last node’s `.next` to `None` (the loop order above handles this).
- Overwriting `.next` before saving it in `nxt` (you’d lose the rest of the list).
- Returning `head` instead of `prev` at the end.

Visual (pointer flow)
---------------------
Original:   0 -> 1 -> 2 -> 3 -> None
Step 1:     0 <- 1    2 -> 3 -> None   (prev=1, curr=2)
Step 2:     0 <- 1 <- 2    3 -> None   (prev=2, curr=3)
Step 3:     0 <- 1 <- 2 <- 3    None   (prev=3, curr=None)
Answer: head' = 3
"""

from __future__ import annotations
from typing import Optional, List, Tuple


# -----------------------------
# Definition for singly-linked list node
# -----------------------------
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next: Optional[ListNode] = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


# ============================================================
# ✅ Active Solution: Iterative (3-pointer) — O(n) time, O(1) space
# ============================================================
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev: Optional[ListNode] = None
        curr: Optional[ListNode] = head

        while curr is not None:
            nxt = curr.next      # 1) save next
            curr.next = prev     # 2) reverse link
            prev = curr          # 3) advance prev
            curr = nxt           # 4) advance curr

        return prev              # new head


# ============================================================
# Alternative: Recursive (clean but uses call stack)
#    Time: O(n) | Space: O(n) recursion stack
# ------------------------------------------------------------
# Idea:
#   reverseListRec(head):
#       if head is None or head.next is None: return head
#       new_head = reverseListRec(head.next)
#       head.next.next = head
#       head.next = None
#       return new_head
# ============================================================
class SolutionRecursive:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head


# -----------------------------
# Helpers: conversions and pretty prints
# -----------------------------
def list_to_linkedlist(arr: List[int]) -> Optional[ListNode]:
    """Build a linked list from a Python list; return head."""
    dummy = ListNode()
    cur = dummy
    for x in arr:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next


def linkedlist_to_list(head: Optional[ListNode]) -> List[int]:
    """Convert linked list to Python list of values."""
    out: List[int] = []
    cur = head
    while cur is not None:
        out.append(cur.val)
        cur = cur.next
    return out


def render_list(head: Optional[ListNode]) -> str:
    """Human-friendly arrow rendering."""
    if head is None:
        return "(empty)"
    parts: List[str] = []
    cur = head
    while cur is not None:
        parts.append(str(cur.val))
        cur = cur.next
    return " -> ".join(parts)


# -----------------------------
# Teaching walkthrough
# -----------------------------
def _walkthrough_example() -> None:
    arr = [0, 1, 2, 3]
    head = list_to_linkedlist(arr)
    print("Walkthrough (iterative 3-pointer):")
    print("  before:", render_list(head))
    new_head = Solution().reverseList(head)
    print("  after :", render_list(new_head))
    print("  as list:", linkedlist_to_list(new_head))
    print()


# -----------------------------
# Comprehensive offline tests
# -----------------------------
def _run_tests() -> None:
    impls: List[Tuple[str, callable]] = [
        ("Iter", Solution().reverseList),
        ("Recur", SolutionRecursive().reverseList),
    ]

    TESTS: List[Tuple[List[int], List[int], str]] = [
        # From prompt
        ([0, 1, 2, 3], [3, 2, 1, 0], "prompt-basic"),
        ([], [], "prompt-empty"),
        # Singles and smalls
        ([42], [42], "single"),
        ([1, 2], [2, 1], "two"),
        ([1, 2, 3], [3, 2, 1], "three"),
        # Repeated values okay
        ([5, 5, 5], [5, 5, 5], "repeats"),
        # Larger
        (list(range(10)), list(reversed(range(10))), "0..9"),
    ]

    passed = 0
    total = 0

    for i, (arr, expected, label) in enumerate(TESTS, 1):
        print(f"\n[{i:02d}][{label}] input={arr}")
        for name, f in impls:
            head = list_to_linkedlist(arr)
            got_head = f(head)
            got = linkedlist_to_list(got_head)
            ok = (got == expected)
            total += 1
            passed += ok
            print(f"  {name:<5} -> got={got!s:<20} expected={expected!s:<20} | {'✅' if ok else '❌'}")

    # Property tests
    print("\nProperty: reverse(reverse(L)) == L")
    arrs = [[], [1], [1, 2], [1, 2, 3, 4], list(range(20))]
    for j, arr in enumerate(arrs, 1):
        head = list_to_linkedlist(arr)
        head2 = Solution().reverseList(head)
        head3 = Solution().reverseList(head2)
        got = linkedlist_to_list(head3)
        ok = (got == arr)
        total += 1
        passed += ok
        print(f"  [P{j}] {arr!r:<24} -> {got!r:<24} | {'✅' if ok else '❌'}")

    print(f"\nPassed {passed}/{total} checks.")


if __name__ == "__main__":
    _walkthrough_example()
    _run_tests()
