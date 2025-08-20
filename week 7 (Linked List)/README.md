# Week 5 — Linked Lists

> “Pointers are powerful—but dangerous. Handle them carefully.”\
> — Interview wisdom

---

## 1. Why Linked Lists?

Linked lists are fundamental data structures frequently tested in technical interviews. They're crucial because:

- **Pointers and References**: They test your understanding of object references and pointer manipulation.
- **Dynamic Data Management**: Excellent for situations where insertions and deletions occur frequently.
- **Foundation for Advanced Structures**: Trees, graphs, stacks, and queues often rely on linked-list mechanics.

When interview problems involve **reordering**, **merging**, **reversing**, **detecting cycles**, or **removal operations**, linked lists often provide optimal and elegant solutions.

**Mastering linked lists means mastering pointer manipulation—a key skill for coding interviews.**

---

## 2. Linked Lists vs. Arrays

| Operation               | Array          | Linked List       | Winner?        |
| ----------------------- | -------------- | ----------------- | -------------- |
| Access by index         | **O(1)**       | O(n)              | 🏆 Array       |
| Insert/Delete at start  | O(n)           | **O(1)**          | 🏆 Linked List |
| Insert/Delete at end    | O(1) amortized | O(n)\*            | 🏆 Array       |
| Insert/Delete in middle | O(n)           | O(n)              | ⚖️ Tie         |
| Memory overhead         | Low            | Higher (pointers) | 🏆 Array       |

\*With a tail pointer, linked lists achieve O(1) insertion at the end.

**Key takeaway:** Linked lists shine when frequent insertions/deletions occur, especially at the start. Arrays excel at random-access.

---

## 3. Key Concepts

### Singly Linked List

- Each node contains a `val` and a `next` pointer.
- The `head` points to the first node; `None` marks the end.
- Traversal starts at the head and continues via `node.next`.
- Deletion and insertion can be **O(1)** if node reference is known.

```python
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
```

### Circular Linked List

- Last node’s `next` points back to some previous node (or head).
- Useful for looping structures but needs cycle detection.
- **Danger:** Traversal can go into infinite loop if not handled properly.

### Doubly Linked List

- Each node contains `val`, `next`, and `prev`.
- Enables two-way traversal.
- Insertions/deletions become easier with direct access to previous nodes.

```python
class DListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
```

---

## 4. Practice Line-up & Why These Questions Matter

| # | Problem                                                                                                | Core Concept               | Why It's Important                                        |
| - | ------------------------------------------------------------------------------------------------------ | -------------------------- | --------------------------------------------------------- |
| 0 | [Design Singly Linked List](https://leetcode.com/problems/design-linked-list/)                         | Full implementation        | Foundation to understand internals of a linked list.      |
| 1 | [Reverse Linked List (LC 206)](https://leetcode.com/problems/reverse-linked-list/)                     | Reversal & pointers        | Tests basic traversal and pointer flipping.               |
| 2 | [Merge Two Sorted Lists (LC 21)](https://leetcode.com/problems/merge-two-sorted-lists/)                | Merging sorted lists       | Core pointer logic, must-know merge strategy.             |
| 3 | [Linked List Cycle (LC 141)](https://leetcode.com/problems/linked-list-cycle/)                         | Cycle detection            | Introduces Floyd’s Tortoise & Hare approach.              |
| 4 | [Reorder List (LC 143)](https://leetcode.com/problems/reorder-list/)                                   | Reordering & split/reverse | Combines several skills: mid finding, reverse, merge.     |
| 5 | [Remove Nth Node From End (LC 19)](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)    | Two-pointer edge case      | Important dummy node pattern.                             |
| 6 | [Copy List with Random Pointer (LC 138)](https://leetcode.com/problems/copy-list-with-random-pointer/) | Deep copy with mapping     | Combines hashing and pointer reconstruction.              |
| 7 | [Add Two Numbers (LC 2)](https://leetcode.com/problems/add-two-numbers/)                               | Arithmetic with pointers   | Simulates digit-by-digit addition, common interview type. |
| 8 | [Find the Duplicate Number (LC 287)](https://leetcode.com/problems/find-the-duplicate-number/)         | Cycle detection in array   | Applies linked list cycle technique to array problems.    |
| 9 | [Merge K Sorted Lists (LC 23)](https://leetcode.com/problems/merge-k-sorted-lists/)                    | Min heap, k-way merge      | Real-world data stream merging with heap.                 |

---

## 5. Learning Outcomes

By the end of Week 5, you should confidently:

1. **Explain** the trade-offs between linked lists and arrays.
2. **Demonstrate** mastery in pointer manipulation, including reversing, merging, and splitting.
3. **Efficiently** detect and remove cycles using two-pointer methods.
4. **Solve** complex linked-list problems using dummy nodes to simplify logic.
5. **Translate** interview problems into pointer-based logic quickly and accurately.

---

## 6. Skip Test

Solve Reverse Linked List II (LC 92) within 30 minutes. It tests deep pointer manipulation skills:

[https://leetcode.com/problems/reverse-linked-list-ii/](https://leetcode.com/problems/reverse-linked-list-ii/)

---

## 7. Further Reading

- [Leetcode Explore: Linked List](https://leetcode.com/explore/learn/card/linked-list/)
- [Fast and Slow Pointers Explained](https://medium.com/@arifimran5/fast-and-slow-pointer-pattern-in-linked-list-43647869ac99)
- [Python Classes and OOP (Official Docs)](https://docs.python.org/3/tutorial/classes.html)
- [Singly vs Doubly Linked Lists: GeeksforGeeks](https://www.geeksforgeeks.org/doubly-linked-list/)

---

**Next up:**\
Week 6 — Stack Essentials. 

Happy pointer chasing!

