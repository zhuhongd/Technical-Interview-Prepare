"""
Problem: Merge K Sorted Linked Lists

You are given an array of `k` linked lists, where each list is sorted in ascending order.

Merge all the linked lists into one sorted linked list and return its head.

Examples:
---------

Input:  lists = [[1,2,4], [1,3,5], [3,6]]  
Output: [1,1,2,3,3,4,5,6]

Input:  lists = []  
Output: []

Input:  lists = [[]]  
Output: []

Constraints:
------------
- 0 <= lists.length <= 1000
- 0 <= lists[i].length <= 100
- -1000 <= lists[i][j] <= 1000

Link: https://leetcode.com/problems/merge-k-sorted-lists/
"""

# 🧠 Intuition:
# This problem is like merging k sorted arrays — except the data is in linked lists.
# The most efficient way is to use a **min-heap** (priority queue).
#
# Strategy:
# 1. Push the head of each list into a min-heap
# 2. Pop the smallest node, append to result, and push its next node (if any)
# 3. Repeat until heap is empty

# 🎤 Interview Tip:
# - “This is a heap-based k-way merge, like in external sorting.”
# - “Each node insertion and removal in the heap is O(log k),
#    and we do it once per node, for O(n log k) total.”

# Time:  O(n log k), where n = total nodes, k = number of lists
# Space: O(k) for the heap


import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        heapq.heapify(heap)

        # Step 1: Put the head of each list into the heap
        for idx, node in enumerate(lists):
            if node:
                # Push tuple (val, index, node) to break ties
                heapq.heappush(heap, (node.val, idx, node))

        dummy = ListNode(0)
        current = dummy

        # Step 2: Extract min and push next from same list
        while heap:
            val, idx, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))

        return dummy.next


"""
🧪 Dry Run:

lists = [[1,4], [2,3], [0,5]]

Initial heap: (0, 2), (1, 0), (2, 1)

Step-by-step pops:
→ 0 → 1 → 2 → 3 → 4 → 5

Result: [0, 1, 2, 3, 4, 5]

✅ Handles:
- Empty input list
- Some lists are empty
- Duplicates across or within lists
"""
