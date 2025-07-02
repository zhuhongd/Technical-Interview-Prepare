# Week 5 — Linked Lists

> “Pointers are powerful—but dangerous. Handle them carefully.”  
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

| Operation                | Array                 | Linked List      | Winner?            |
|--------------------------|-----------------------|------------------|--------------------|
| Access by index          | **O(1)**              | O(n)             | 🏆 Array           |
| Insert/Delete at start   | O(n)                  | **O(1)**         | 🏆 Linked List     |
| Insert/Delete at end     | O(1) amortized        | O(n)*            | 🏆 Array           |
| Insert/Delete in middle  | O(n)                  | O(n)             | ⚖️ Tie             |
| Memory overhead          | Low                   | Higher (pointers)| 🏆 Array           |

*With a tail pointer, linked lists achieve O(1) insertion at the end.

**Key takeaway:** Linked lists shine when frequent insertions/deletions occur, especially at the start. Arrays excel at random-access.

---

## 3. Types of Linked Lists

### Singly Linked List

- **Node Structure**: Each node contains a value and a pointer (`next`) to the next node.
- **Advantages**:
  - Fast insertion and deletion if node reference is known (O(1)).
  - Low memory overhead compared to doubly linked lists.
- **Disadvantages**:
  - Traversal is forward-only.
  - Deletion and insertion require previous node references or traversal.

### Doubly Linked List

- **Node Structure**: Each node contains a value and two pointers (`next` and `prev`) pointing to the next and previous nodes, respectively.
- **Advantages**:
  - Bidirectional traversal.
  - Easier node deletion, as the previous node is directly accessible.
- **Disadvantages**:
  - Higher memory overhead due to extra pointers.

### Circular Linked List

- **Node Structure**: Similar to singly or doubly linked lists, but the last node points back to the head node.
- **Advantages**:
  - Efficient for round-robin scheduling tasks.
- **Disadvantages**:
  - Risk of infinite loops if not handled carefully.

---

## 4. Key Concepts

- **Nodes and Pointers**: Nodes store data and pointers to adjacent nodes.
- **Head & Tail**: Pointers to the first and optionally last node.
- **Dummy Node**: Simplifies edge cases for insertion/removal.
- **Fast & Slow Pointers**: Efficient for cycle detection and finding middle nodes.
- **Reverse Linked List**: Core technique for advanced reordering problems.

---

## 5. Practice Line-up & Why These Questions Matter

| # | Problem                                                                                 | Core Concept               | Why It's Important                                              |
|---|-----------------------------------------------------------------------------------------|----------------------------|-----------------------------------------------------------------|
| 1 | [Merge Two Sorted Lists (LC 21)](https://leetcode.com/problems/merge-two-sorted-lists/) | Pointer merging            | Essential pointer manipulation basics, very common question.    |
| 2 | [Linked List Cycle (LC 141)](https://leetcode.com/problems/linked-list-cycle/)          | Cycle detection            | Teaches critical fast & slow pointers (Floyd's algorithm).      |
| 3 | [Reorder List (LC 143)](https://leetcode.com/problems/reorder-list/)                    | Splitting and reversing    | Combines reversing and merging skills, frequently asked in interviews. |
| 4 | [Remove Nth Node From End (LC 19)](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Two-pointer edge cases     | Demonstrates dummy node usage and two-pointer strategy.         |
| 5 | [Copy List with Random Pointer (LC 138)](https://leetcode.com/problems/copy-list-with-random-pointer/) | Hashmap & pointers         | Combines hashmaps with pointer skills—tests understanding deeply. |
| 6 | [Add Two Numbers (LC 2)](https://leetcode.com/problems/add-two-numbers/)                | Pointer arithmetic         | Core skill for combining pointer traversal with arithmetic logic. |
| 7 | [Merge K Sorted Lists (LC 23)](https://leetcode.com/problems/merge-k-sorted-lists/)     | Priority Queue (heap)      | Advanced merging, heap implementation, critical for real-world scenarios. |

---

## 6. Learning Outcomes

By the end of Week 5, you should confidently:

1. **Explain** the trade-offs between linked lists and arrays.
2. **Demonstrate** mastery in pointer manipulation, including reversing, merging, and splitting.
3. **Efficiently** detect and remove cycles using two-pointer methods.
4. **Solve** complex linked-list problems using dummy nodes to simplify logic.
5. **Translate** interview problems into pointer-based logic quickly and accurately.

---

## 7. Skip Test

Solve Reverse Linked List II (LC 92) within 30 minutes. It tests deep pointer manipulation skills:

https://leetcode.com/problems/reverse-linked-list-ii/

---

## 8. Further Reading

- [Leetcode Explore: Linked List](https://leetcode.com/explore/learn/card/linked-list/)
- [Fast and Slow Pointers Explained](https://medium.com/@smathur0901/slow-and-fast-pointer-pattern-floyds-cycle-detection-algorithm-6995df2753b1)
- [Python Classes and OOP (Official Docs)](https://docs.python.org/3/tutorial/classes.html)

---

**Next up:**  
Week 6 — Recursion and Stack Essentials. You’ll refine your understanding of recursion and how it connects deeply to linked lists and other recursive data structures.

Happy pointer chasing!

