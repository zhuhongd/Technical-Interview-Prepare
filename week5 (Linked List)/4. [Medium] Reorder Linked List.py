"""
Problem: Reorder Linked List

You are given the head of a singly linked list. Reorder the nodes of the list so that
the list is reordered in this pattern:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the node values — only change the pointers.

Examples:
---------

Input:  head = [2, 4, 6, 8]
Output: [2, 8, 4, 6]

Input:  head = [2, 4, 6, 8, 10]
Output: [2, 10, 4, 8, 6]

Constraints:
------------
- 1 <= Length <= 1000
- 1 <= Node.val <= 1000

Link: https://leetcode.com/problems/reorder-list/
"""

# 🧠 Intuition:
# We want to interleave nodes from the front and back of the list:
# [2, 4, 6, 8] → [2, 8, 4, 6]
#
# Strategy:
# 1. Find the middle of the list using slow/fast pointers.
# 2. Reverse the second half.
# 3. Merge the two halves in alternating order.

# 🎤 Interview Tip:
# “This question is a great test of manipulating pointers safely.
# I made sure to cut the list into two, reverse the second half, then merge while
# carefully tracking all next pointers.”

# Time:  O(n)
# Space: O(1) – in-place operations

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: Find middle node using slow and fast pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half of the list
        second = slow.next       # Starting point of second half
        slow.next = None         # Cut the list at the middle
        prev = None

        while second:
            nxt = second.next    # Save next node
            second.next = prev   # Reverse pointer
            prev = second        # Move prev forward
            second = nxt         # Move current forward

        # Now prev is the head of the reversed second half
        # For example: head = [2, 4], prev = [8, 6]

        # Step 3: Merge two halves together
        while prev:
            h_nxt = head.next    # Save next from first half
            p_nxt = prev.next    # Save next from second half

            head.next = prev     # Link head to node from second half
            prev.next = h_nxt    # Link that node back to first half's next

            head = h_nxt         # Advance in first half
            prev = p_nxt         # Advance in second half


"""
🧪 Dry Run Example:

Input: [2, 4, 6, 8, 10]

Step 1: Find mid
  slow → 6
  head = [2 → 4 → 6]
  second half = [8 → 10]

Step 2: Reverse second half
  becomes [10 → 8]

Step 3: Merge:
  head = [2]
  prev = [10]
  => 2 → 10 → 4 → 8 → 6

Final Result: [2, 10, 4, 8, 6]
"""
