"""
Problem: Design Singly Linked List

Implement a singly linked list with the following operations:

- LinkedList(): Initializes an empty linked list.
- get(i): Returns the value of the ith node (0-indexed). If out of bounds, return -1.
- insertHead(val): Inserts a node with val at the head.
- insertTail(val): Inserts a node with val at the tail.
- remove(i): Removes the ith node. Return True if successful, else False.
- getValues(): Returns a list of all values from head to tail.

Example 1:
----------
ll = LinkedList()
ll.insertHead(1)      # List: 1
ll.insertTail(2)      # List: 1 -> 2
ll.insertHead(0)      # List: 0 -> 1 -> 2
ll.remove(1)          # Removes '1', List: 0 -> 2
ll.getValues()        # Returns [0, 2]

Example 2:
----------
ll = LinkedList()
ll.insertHead(2)      # List: 2
ll.insertHead(1)      # List: 1 -> 2
ll.get(5)             # Index out of bounds, returns -1

Common Mistakes:
----------------
- Not handling empty list cases in get() or remove().
- Forgetting to update the head when removing the 0th node.
- Traversing incorrectly in remove (off-by-one error in loop).
- Not checking if index is out of bounds in get/remove.

Time & Space Complexity:
------------------------
- get(i): O(n)      – traverse to the ith node
- insertHead(val): O(1)
- insertTail(val): O(n) – traverse to the end
- remove(i): O(n)
- getValues(): O(n)
- Space: O(n) for storing n nodes

link: https://neetcode.io/problems/singlyLinkedList
"""

# 🧠 Intuition:
# This is a textbook OOP data structure problem.
# Every node contains a value and a reference to the next node.
# The list only tracks the "head" node.
# You build behaviors like get, insert, delete, etc., by traversing or modifying the linked structure.

class ListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self):
        # Start with an empty list, so head is None
        self.head = None

    def get(self, index: int) -> int:
        """
        Returns the value at the given index (0-based).
        If index is out of bounds, returns -1.

        Example:
        --------
        List: 5 -> 8 -> 10
        get(0) → 5
        get(2) → 10
        get(3) → -1 (OOB)

        Strategy:
        ---------
        - Traverse using a pointer and counter
        - If counter matches the index, return current node's value
        - If we reach the end before index, return -1
        """
        current = self.head
        i = 0
        while current is not None:
            if i == index:
                return current.value
            current = current.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        """
        Inserts a new node at the beginning of the list.

        Example:
        --------
        Before: 2 -> 3
        insertHead(1)
        After : 1 -> 2 -> 3

        Strategy:
        ---------
        - Create a new node that points to the current head
        - Re-assign head to point to the new node
        """
        new_node = ListNode(val, self.head)
        self.head = new_node

    def insertTail(self, val: int) -> None:
        """
        Inserts a new node at the end of the list.

        Example:
        --------
        Before: 3 -> 4
        insertTail(5)
        After : 3 -> 4 -> 5

        Edge Case:
        ----------
        If list is empty (head is None), new node becomes the head.

        Strategy:
        ---------
        - If list is empty, set head to new node
        - Otherwise, traverse to the last node and set its `.next` to the new node
        """
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def remove(self, index: int) -> bool:
        """
        Removes the node at the given index.

        Returns True if successful, False if index is out of bounds.

        Example:
        --------
        Before: 1 -> 2 -> 3
        remove(1)
        After : 1 -> 3

        Edge Case:
        ----------
        - If index == 0, update head to head.next
        - If index >= length, return False

        Strategy:
        ---------
        - If removing the head, just move the head pointer
        - Else, traverse to (index - 1)th node and bypass the target
        """
        if self.head is None:
            return False
        if index == 0:
            self.head = self.head.next
            return True
        current = self.head
        for _ in range(index - 1):
            if not current.next:
                return False  # index too large
            current = current.next
        if current.next is None:
            return False  # index out of bounds
        current.next = current.next.next  # skip the node
        return True

    def getValues(self) -> list:
        """
        Returns a list of values from head to tail.

        Example:
        --------
        List: 1 -> 4 -> 5
        getValues() → [1, 4, 5]

        Strategy:
        ---------
        - Traverse the list and append values to a result list
        - Return the result
        """
        final = []
        current = self.head
        while current:
            final.append(current.value)
            current = current.next
        return final


# 🎤 Interview Tips:
# ------------------
# - “This class tracks only the head pointer and does not use a tail pointer,
#    so insertTail is O(n). In a real system I’d consider optimizing that.”
# - “I chose to return True/False for remove so the caller knows if the operation succeeded.”
# - “I structured the list using OOP principles: encapsulation of behavior inside the class,
#    and data modeled with ListNode.”
