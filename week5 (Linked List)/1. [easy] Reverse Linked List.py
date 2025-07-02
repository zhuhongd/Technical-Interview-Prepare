"""
Problem: Reverse Linked List
-----------------------------
Given the head of a singly linked list, reverse the list and return the new head.

Example 1:
----------
Input:  head = [0, 1, 2, 3]
Output: [3, 2, 1, 0]

Example 2:
----------
Input:  head = []
Output: []

Constraints:
------------
- The number of nodes in the list is in the range [0, 1000]
- -1000 <= Node.val <= 1000

Approach:
---------
Use iterative pointer manipulation with 3 variables:
- `prev`: the previous node
- `curr`: the current node
- `nxt`: the next node

This reverses the `.next` pointers in-place.

Time Complexity:  O(n)
Space Complexity: O(1)

Common Mistakes:
----------------
- Forgetting to set the `.next` of the last node to None
- Overwriting `.next` before storing the next node

link: https://neetcode.io/problems/reverse-a-linked-list?list=neetcode150
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            nxt = curr.next      # Save next node
            curr.next = prev     # Reverse pointer
            prev = curr          # Move prev forward
            curr = nxt           # Move curr forward

        return prev  # New head of reversed list

# Optional: Helper functions for testing

def list_to_linkedlist(arr):
    """Convert a Python list to a linked list."""
    dummy = ListNode()
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linkedlist_to_list(head):
    """Convert a linked list back to a Python list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

if __name__ == "__main__":
    sol = Solution()
    head = list_to_linkedlist([0, 1, 2, 3])
    reversed_head = sol.reverseList(head)
    print(linkedlist_to_list(reversed_head))  # Output: [3, 2, 1, 0]

    head = list_to_linkedlist([])
    reversed_head = sol.reverseList(head)
    print(linkedlist_to_list(reversed_head))  # Output: []
