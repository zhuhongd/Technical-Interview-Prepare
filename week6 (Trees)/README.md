# Week 3 — Binary Trees, Traversals & BSTs

> “Recursion is like climbing a tree—the scenery repeats at every branch.”

---

## 1.  Big‑Picture Concept

A **binary tree** is a collection of `TreeNode` objects, each holding a value plus *up to two* child pointers: `left` and `right`.

```python
class TreeNode:
    def __init__(self, val: int):
        self.val  = val          # data stored at the node
        self.left = None        # pointer to left child (≤ 2 children)
        self.right = None
```

Unlike linked lists—which form a single chain—trees branch downward, giving us a *hierarchy* that is perfect for divide‑and‑conquer algorithms.

A **Binary Search Tree (BST)** adds one critical *ordering* rule: *All nodes in a node’s left‑subtree < current node < all nodes in its right‑subtree* (recursively).\
This turns the tree into a dynamic, logarithmic search structure.

---

## 2.  Quick‑Reference Terminology

| Term                      | What it means & why you care                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------ |
| **Root**                  | Top‑most node with no parent.  Starting point for traversals.                                                |
| **Leaf**                  | Node with *no* children.  Every finite tree has ≥ 1 leaf—useful base case.                                   |
| **Height**                | # nodes on the longest path **downward** from root (edges = height−1).  Drives recursion depth & complexity. |
| **Depth**                 | # nodes on the path **upward** to root (root depth = 1).                                                     |
| **Ancestor / Descendant** | Standard family terms—important in LCA/diameter questions.                                                   |
| **Balanced**              | Height ≈ log n.  Guarantees O(log n) search/insert for BSTs.                                                 |
| **Skewed**                | Height ≈ n (degrades to linked list).  Worst‑case O(n) operations.                                           |

---

## 3.  Traversal Playbook

(*Depth‑First Search vs. Breadth‑First Search*)

| DFS Variant           | Order                    | Classic Use‑case                                       |
| --------------------- | ------------------------ | ------------------------------------------------------ |
| **Preorder**          | Root → Left → Right      | Serialize a tree, copy/clone, build prefix expressions |
| **Inorder**           | Left → Root → Right      | Returns *sorted* list for BSTs, validates BST property |
| **Postorder**         | Left → Right → Root      | Compute subtree values (size, depth), delete/free tree |
| **BFS / Level Order** | level‑by‑level via queue | Shortest‑path in unweighted trees, zig‑zag traversal   |

```python
# Recursive In‑order
def inorder(root):
    if not root: return
    inorder(root.left)
    visit(root)
    inorder(root.right)

# Iterative BFS (level order)
from collections import deque

def bfs(root):
    q = deque([root]) if root else deque()
    while q:
        for _ in range(len(q)):
            node = q.popleft(); visit(node)
            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)
```

*Time:* O(n) — every node visited once.\
*Space:* O(h) for DFS recursion stack, O(width) for BFS queue.

---

## 4.  BST Operations Cheat‑Sheet

| Operation  | Idea (recursive)                                                              | Balanced Cost | Skewed Cost |
| ---------- | ----------------------------------------------------------------------------- | ------------- | ----------- |
| **Search** | Compare → go left/right                                                       | O(log n)      | O(n)        |
| **Insert** | Search until reaching `None`, attach node                                     | O(log n)      | O(n)        |
| **Remove** | 0–1 child: splice; 2 children: replace w/ *in‑order successor* then delete it | O(log n)      | O(n)        |

```python
# Search (returns True/False)
def search(root, target):
    if not root: return False
    if target > root.val:
        return search(root.right, target)
    if target < root.val:
        return search(root.left, target)
    return True  # found
```

> **Why BSTs?** Same O(log n) lookup as a sorted array *plus* cheap O(log n) insert/delete.

---

## 5.  Practice Line‑up & Why These Matter

| # | Problem (LeetCode)                       | Theme                       | Interview Takeaway                      |
| - | ---------------------------------------- | --------------------------- | --------------------------------------- |
| 1 | Same Tree (#100)                         | Parallel traversal          | Equality logic & base‑case discipline   |
| 2 | Invert Binary Tree (#226)                | Recursion fundamentals      | "Hello world" of tree problems          |
| 3 | Maximum Depth (#104)                     | Height calculation          | Base for balance/diameter questions     |
| 4 | Symmetric Tree (#101)                    | Mirror recursion            | Intro to dual‑pointer thinking          |
| 5 | Binary Tree Level‑Order Traversal (#102) | BFS queue                   | First exposure to breadth‑wise scanning |
| 6 | Validate BST (#98)                       | Range propagation / inorder | Solidifies BST invariant reasoning      |
| 7 | Serialize & Deserialize BT (#297)        | Design & codec              | End‑to‑end reasoning, string ↔ tree     |
| 8 | Insert into BST (#701)                   | BST insertion               | Reinforces balanced vs. skewed analysis |

---

## 6.  Learning Outcomes

By the end of this chapter you will be able to:

1. **Define** core tree terminology (root, leaf, height, balanced, etc.).
2. **Implement** all four canonical traversals recursively *and* iteratively.
3. **Analyze** how height affects time/space complexities.
4. **Perform** BST search/insert/delete with confidence.
5. **Recognize** when to choose a tree over arrays/hashes in design questions.

---

## 7.  Skip Test

If you can solve **Serialize & Deserialize Binary Tree** (LC 297) in ≤ 40 min—producing a working codec and explaining trade‑offs—you’re ready to move on.

---

## 8.  Further Reading & Visualizers

- [Tech Interview Handbook – Binary Tree Patterns](https://www.techinterviewhandbook.org/grind75)
- [Brian Holt – Illustrated BST Guide](https://frontendmasters.com)
- [Visualgo Tree Traversal Animator](https://visualgo.net/en)
- [MIT 6.006 Lecture – Balanced Trees](https://ocw.mit.edu)

---

**Next:** Week 7 — Heaps & Priority Queues. We'll turn trees sideways to prioritize *highest* (or *lowest*) elements in O(log n) time.
