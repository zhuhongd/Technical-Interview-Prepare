"""
Problem: Linked List Cycle Detection

Given the head of a linked list, return True if the list contains a cycle.
Otherwise, return False.

A cycle occurs when a node's `next` pointer points back to a previous node in the list,
creating a loop. If there's no such connection, the list ends normally with `None`.

Important:
----------
Internally, the test case may use an `index` to indicate where the cycle begins,
but the function **does not** take that as input.

Examples:
---------

Input: head = [3, 2, 0, -4], index = 1  
Output: True  
Explanation: Tail connects to the 1st node (node with value 2)

Input: head = [1, 2], index = -1  
Output: False  
Explanation: No cycle; tail points to null

Input: head = [1], index = -1  
Output: False

Common Mistakes:
----------------
- Trying to store visited nodes in a set (works, but uses O(n) space)
- Forgetting to check that `fast` and `fast.next` are not null before advancing
- Assuming cycle must start at head — not true!

Optimal Approach: Floyd’s Tortoise and Hare (Two-Pointer Method)

Time Complexity:
----------------
- O(n): In the worst case, the fast pointer loops through the entire list

Space Complexity:
-----------------
- O(1): No extra space is used (pointers only)

Link: https://leetcode.com/problems/linked-list-cycle/
"""

# 🧠 Intuition:
# Use two pointers:
# - slow moves 1 step at a time
# - fast moves 2 steps at a time
# If there's a cycle, they'll eventually meet inside the loop.
# If there's no cycle, fast will hit the end (None).

# 🎤 Interview Tip:
# “This is the classic cycle detection problem. The trick is to use two pointers
# moving at different speeds. If a cycle exists, the fast pointer will ‘lap’ the slow one,
# and they’ll meet. This uses O(1) space, unlike the visited-set approach.”

# ✅ Correctly handles:
# - Empty list (head is None)
# - Single node (no cycle)
# - Proper loop where tail links back to an earlier node


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        # Continue while fast and fast.next are not None
        while fast and fast.next:
            slow = slow.next           # Move one step
            fast = fast.next.next      # Move two steps

            # If they meet, there's a cycle
            if slow == fast:
                return True

        # If we exit the loop, there's no cycle
        return False


"""
🧪 Dry Run:

Example: head = [1, 2, 3, 4], tail connects to node 2 (index = 1)
List: 1 → 2 → 3 → 4 ↘
              ↑------

Initial:
slow = head (1)
fast = head (1)

Step 1:
slow = 2
fast = 3

Step 2:
slow = 3
fast = 1 (cycled back)

Step 3:
slow = 4
fast = 3

Step 4:
slow = 2
fast = 1

Step 5:
slow = 3
fast = 3 → They meet → return True
"""
