"""
Problem: Add Two Numbers (Linked List Version)

You're given two **non-empty** linked lists, `l1` and `l2`, representing two non-negative integers.

- Digits are stored **in reverse order** (e.g. 123 → 3 → 2 → 1)
- Each node contains a **single digit**
- Return a linked list representing their sum, also in reverse order

You may assume:
- No leading zeros (except the number 0 itself)
- The two numbers can have different lengths

Examples:
---------

Input:  l1 = [1, 2, 3], l2 = [4, 5, 6]  
Output: [5, 7, 9]  
Explanation: 321 + 654 = 975 → reversed → 5 → 7 → 9

Input:  l1 = [9], l2 = [9]  
Output: [8, 1]  
Explanation: 9 + 9 = 18 → reversed → 8 → 1

Constraints:
------------
- 1 <= len(l1), len(l2) <= 100
- 0 <= Node.val <= 9

Link: https://leetcode.com/problems/add-two-numbers/
"""

# 🧠 Intuition:
# We simulate digit-by-digit addition like how you would do it by hand.
# Start from the least significant digit (head of each list), add values, track carry.
# Use a dummy node to simplify list construction.
# Continue while there's something to add from l1, l2, or a remaining carry.

# 🎤 Interview Tip:
# “This problem combines digit math with pointer logic.
# I use a dummy node to build the output list and carry logic to manage overflow.”

# Time:  O(max(n, m)) — where n and m are lengths of l1 and l2
# Space: O(max(n, m)) — result list is one node per digit


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()     # Dummy head to simplify logic
        curr = dummy
        carry = 0

        # Loop until both lists are exhausted AND there's no carry
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0  # Value from l1 or 0
            v2 = l2.val if l2 else 0  # Value from l2 or 0

            total = v1 + v2 + carry   # Total sum
            carry = total // 10       # Carry for next position
            new_digit = total % 10    # Current digit

            curr.next = ListNode(new_digit)  # Append to result
            curr = curr.next

            # Move pointers forward
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next


"""
🧪 Dry Run Example:

l1 = [2, 4, 3]  # represents 342
l2 = [5, 6, 4]  # represents 465

Step-by-step:
- 2 + 5 = 7 → no carry → [7]
- 4 + 6 = 10 → carry = 1, digit = 0 → [7 → 0]
- 3 + 4 + 1 = 8 → [7 → 0 → 8]

Result: [7, 0, 8] (342 + 465 = 807)

✅ Handles:
- Lists of different lengths
- Carry on final digit (e.g. 5 + 5 = 10)
- One or both lists empty (though per constraints, non-empty)
"""
