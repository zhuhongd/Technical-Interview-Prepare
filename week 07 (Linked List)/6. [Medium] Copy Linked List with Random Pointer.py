"""
Problem: Copy Linked List with Random Pointer

You're given the head of a linked list where each node contains:
- a `val` (integer),
- a `next` pointer, and
- a `random` pointer, which may point to **any node** in the list or be None.

Return a **deep copy** of the list, meaning:
- Each node is **newly created**
- The new list has the same structure and values
- All `next` and `random` pointers reference nodes in the **new list**, not the original

Examples:
---------

Input: head = [[3,null],[7,3],[4,0],[5,1]]
Output: [[3,null],[7,3],[4,0],[5,1]]

Input: head = [[1,null],[2,2],[3,2]]
Output: [[1,null],[2,2],[3,2]]

Constraints:
------------
- 0 <= n <= 100
- -100 <= Node.val <= 100
- Each `random` pointer is either None or points to a node in the same list

Link: https://leetcode.com/problems/copy-list-with-random-pointer/
"""

# 🧠 Intuition:
# We want to deep copy each node and make sure both `next` and `random` point
# to **new** nodes, not old ones.
#
# Strategy:
# 1. Use a dictionary to map original nodes to their copies
# 2. First pass: create all nodes (no connections yet)
# 3. Second pass: assign both `next` and `random` using the map

# 🎤 Interview Tip:
# “This problem is about understanding object references.
# You can’t just copy values—you need to rewire both the `next` and `random` pointers
# to point to newly created nodes. A dictionary helps map originals to their copies.”

# Time:  O(n) — visit each node twice
# Space: O(n) — dictionary to hold mapping from original → copy


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Hashmap to hold mapping: original_node → copied_node
        hashmap = {None: None}  # ensures we don't need to null-check later
        curr = head

        # 🧹 Edge case: empty list
        if head is None:
            return None

        # Pass 1: Create copy of each node (values only, no links yet)
        while curr:
            # Copy the node and store it in the hashmap
            currentNode = Node(curr.val)
            hashmap[curr] = currentNode
            curr = curr.next

        # Pass 2: Assign .next and .random pointers
        curr = head
        while curr:
            copynode = hashmap[curr]         # get the copy
            copynode.next = hashmap[curr.next]     # point to copy of next
            copynode.random = hashmap[curr.random] # point to copy of random
            curr = curr.next

        # Return the head of the new copied list
        return hashmap[head]


"""
🧪 Dry Run:

Original: 3 → 7 → 4 → 5
randoms:  [None, 3, 0, 1]

1. Create hashmap:
   hashmap = {
       3 (original) → Node(3),
       7 (original) → Node(7),
       ...
   }

2. Assign next and random:
   Node(3).next = Node(7)
   Node(7).random = Node(5)  (copied version)

Return Node(3)

✅ Handles edge cases:
- Empty list
- Self-pointing randoms
- Multiple nodes pointing to same random
"""
