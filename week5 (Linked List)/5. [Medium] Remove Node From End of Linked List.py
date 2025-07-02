"""
Problem: Remove Node From End of Linked List

You are given the beginning of a linked list `head`, and an integer `n`.

Remove the nth node from the end of the list and return the beginning of the updated list.

Examples:
---------

Input:  head = [1, 2, 3, 4], n = 2  
Output: [1, 2, 4]  
Explanation: Remove the 2nd node from the end (node with value 3)

Input:  head = [5], n = 1  
Output: []  
Explanation: Remove the only node

Input:  head = [1, 2], n = 2  
Output: [2]  
Explanation: Remove head node

Constraints:
------------
- 1 <= list length <= 30
- 0 <= Node.val <= 100
- 1 <= n <= length of list

Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

# 🧠 Intuition:
# We need to remove the nth node from the end, but we can’t directly count from the end.
# So we use two pointers:
#   - Advance one pointer `n` steps first.
#   - Then move both pointers together until the fast one hits the end.
#   - The slow pointer will be just before the node to remove.
#
# A dummy node is used to handle edge cases where the head might be removed.

# 🎤 Interview Tip:
# - “This is a classic two-pointer technique. The key insight is to create a gap of n nodes
#    between the two pointers.”
# - “Using a dummy node makes removing the head node consistent with other cases.”
# - “This runs in one pass and uses O(1) extra space.”

# Time:  O(L) — where L is the length of the list
# Space: O(1) — only pointer manipulation

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create dummy node that points to head
        dummy = ListNode()
        dummy.next = head
        slow = dummy
        fast = head

        # 🧪 Edge case: removing the only node
        if head.next is None:
            return None

        # Step 1: Move fast n steps ahead
        for i in range(n):
            fast = fast.next

        # Step 2: Move both pointers until fast reaches the end
        # At that point, slow is at the node before the one we want to remove
        curr = dummy
        while fast:
            fast = fast.next
            curr = curr.next

        # Step 3: Skip the node to delete
        curr.next = curr.next.next

        # Return the real head (which might be new if the old head was removed)
        return dummy.next


"""
🧪 Dry Run:

head = [1, 2, 3, 4, 5], n = 2

Step 1:
- fast moves 2 steps → fast = 3
- curr = dummy (points to 0 → 1 → ...)

Step 2:
- Move fast and curr until fast reaches end:
    fast = 4 → 5 → None
    curr = 0 → 1 → 2 → 3

Step 3:
- curr is at 3, remove curr.next (which is 4)
- result: 1 → 2 → 3 → 5

Return dummy.next → 1

✅ Works even if the node to remove is head (n == length)
✅ Handles one-element list case
"""
