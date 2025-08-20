"""
Problem: Merge Two Sorted Linked Lists

You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists into one sorted linked list and return the head of the new list.

The new list should be made by splicing together the nodes from `list1` and `list2`.

Examples:
---------

Input:  list1 = [1, 2, 4], list2 = [1, 3, 5]
Output: [1, 1, 2, 3, 4, 5]

Input:  list1 = [], list2 = [1, 2]
Output: [1, 2]

Input:  list1 = [], list2 = []
Output: []

Constraints:
------------
- 0 <= length of each list <= 100
- -100 <= Node.val <= 100

Link: https://leetcode.com/problems/merge-two-sorted-lists/
"""

# 🧠 Intuition:
# Both lists are already sorted.
# We use a dummy node to simplify edge cases.
# Walk through both lists using two pointers, and at each step,
# attach the smaller node to the result list.
# When one list is exhausted, append the remaining of the other.

# 🎤 Interview Tip:
# - “I used a dummy head to avoid handling special cases like inserting the first node.”
# - “Since both input lists are already sorted, I can merge them in one pass using two pointers.”
# - “This is a common pattern: use dummy node + current pointer for building a new list.”

# Time Complexity:
# O(n + m), where n and m are the lengths of the two lists

# Space Complexity:
# O(1) — no extra space is used beyond pointers (in-place merge)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to act as the starting point of the merged list
        dummynode = ListNode()
        curr = dummynode  # Pointer to build the merged list

        # 🔁 Step 1: Traverse both lists while both are non-empty
        while list1 and list2:
            # Compare current values in both lists
            if list1.val < list2.val:
                # Attach the smaller node to the result
                curr.next = list1
                list1 = list1.next  # Move list1 forward
            else:
                curr.next = list2
                list2 = list2.next  # Move list2 forward
            curr = curr.next  # Move the result pointer forward

        # 🧹 Step 2: Attach the rest of whichever list is not yet finished
        if list1 is not None:
            curr.next = list1
        elif list2 is not None:
            curr.next = list2

        # 📎 Return the node after the dummy (i.e., head of the merged list)
        return dummynode.next


"""
🧪 Example Dry Run:

list1 = [1 → 2 → 4]
list2 = [1 → 3 → 5]

Step-by-step merging:
1. list1.val=1, list2.val=1 → attach list2 (1), move list2
2. list1.val=1, list2.val=3 → attach list1 (1), move list1
3. list1.val=2, list2.val=3 → attach list1 (2), move list1
4. list1.val=4, list2.val=3 → attach list2 (3), move list2
5. list1.val=4, list2.val=5 → attach list1 (4), move list1
6. list1 is None → attach rest of list2 (5)

Result: 1 → 1 → 2 → 3 → 4 → 5
"""
