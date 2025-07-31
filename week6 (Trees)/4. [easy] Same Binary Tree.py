"""
📚 Problem: Same Binary Tree  (aka *Same Tree*, LeetCode #100)
-----------------------------------------------------------
Given the roots of two binary trees `p` and `q`, return **True** if the trees
are *equivalent* (they share the exact same structure **and** each pair of
corresponding nodes stores the same value); otherwise return **False**.

Example 1
~~~~~~~~~
Input   : p = [1,2,3], q = [1,2,3]
Output  : True

Example 2
~~~~~~~~~
Input   : p = [4,7], q = [4, null, 7]
Output  : False  # shapes differ ➜ not equivalent

Example 3
~~~~~~~~~
Input   : p = [1,2,3], q = [1,3,2]
Output  : False  # node values differ ➜ not equivalent

Constraints
~~~~~~~~~~~
* 0 ≤ *nodes* ≤ 100
* –100 ≤ `Node.val` ≤ 100

--------------------------------------------------------------------------
Approach 1: **Recursive Depth‑First Search (DFS)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We descend the two trees in lock‑step:
1. If both nodes are **None**, they are trivially equal — return *True*.
2. If exactly one is **None** ➜ shapes differ — return *False*.
3. If both exist, compare their values.  If unequal ➜ return *False*.
4. Recursively check the *left* children and the *right* children.

**Time Complexity:** `O(n)` — each node visited once.
**Space Complexity:** worst‑case `O(h)` where *h* is tree height (call‑stack).

Common mistakes  ➜  forgetting to short‑circuit on unequal values before
recursing, or mixing up the order of the two sub‑trees.

--------------------------------------------------------------------------
Approach 2: **Iterative Breadth‑First Search (BFS)**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Use a queue storing pairs of nodes `(u, v)` from `p` and `q`:
* Pop a pair, perform the same three checks as above (None/None, None/x, val).
* Push the paired children `(u.left,  v.left)` and `(u.right, v.right)`.

This avoids recursion depth limits and can be clearer for some beginners.

**Time Complexity:** `O(n)`
**Space Complexity:** `O(n)` in the worst case (queue can store an entire level).

--------------------------------------------------------------------------
💡 Interview Tips
~~~~~~~~~~~~~~~~
* Mention that preorder/in‑order traversals **cannot** fully verify equality by
  themselves — you must compare *both* structure and values node‑by‑node.
* Clarify that with only 100 nodes recursion depth is safe in Python; if the
  interviewer worries, offer the iterative version.
* Always test the corner cases: (None, None), single‑node trees, one empty & one non‑empty.
"""

from __future__ import annotations
from collections import deque
from typing import Optional


class TreeNode:
    """Simple binary‑tree node used by LeetCode‑style questions."""

    def __init__(self, val: int = 0,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right

    # Nice representation in the REPL / prints
    def __repr__(self):
        return f"TreeNode(val={self.val})"


class Solution:
    """Contains multiple solutions so students can compare trade‑offs."""

    # ------------------------------------------------------------------
    # Recursive DFS version (most natural)
    # ------------------------------------------------------------------
    def is_same_tree_recursive(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Recursive DFS comparing two trees node‑by‑node.

        Args:
            p (TreeNode | None): root of first tree.
            q (TreeNode | None): root of second tree.

        Returns:
            bool: True if the two trees are structurally identical *and*
                  every corresponding node holds the same value.
        """
        # 1️⃣ Both empty ➜ equivalent
        if p is None and q is None:
            return True
        # 2️⃣ One empty ➜ inequivalent (shapes differ)
        if p is None or q is None:
            return False
        # 3️⃣ Values differ ➜ inequivalent
        if p.val != q.val:
            return False
        # 4️⃣ Recurse on left & right sub‑trees
        left_equal = self.is_same_tree_recursive(p.left, q.left)
        right_equal = self.is_same_tree_recursive(p.right, q.right)
        return left_equal and right_equal

    # ------------------------------------------------------------------
    # Iterative BFS version (queue)
    # ------------------------------------------------------------------
    def is_same_tree_iterative(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """Iterative BFS using a queue for students worried about recursion depth."""
        queue: deque[tuple[Optional[TreeNode], Optional[TreeNode]]] = deque([(p, q)])
        while queue:
            u, v = queue.popleft()
            if u is None and v is None:
                continue  # pair is fine
            if u is None or v is None:
                return False
            if u.val != v.val:
                return False
            # enqueue children as pairs
            queue.append((u.left, v.left))
            queue.append((u.right, v.right))
        return True


# ----------------------------------------------------------------------
# 🧪 Quick sanity tests (run `python same_binary_tree.py` directly)
# ----------------------------------------------------------------------
if __name__ == "__main__":
    sol = Solution()

    # Example 1: identical small trees
    root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    root2 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert sol.is_same_tree_recursive(root1, root2) is True
    assert sol.is_same_tree_iterative(root1, root2) is True

    # Example 2: shape differs
    root3 = TreeNode(4, TreeNode(7))          # left child only
    root4 = TreeNode(4, None, TreeNode(7))    # right child only
    assert sol.is_same_tree_recursive(root3, root4) is False

    # Example 3: values differ
    root5 = TreeNode(1, TreeNode(2), TreeNode(3))
    root6 = TreeNode(1, TreeNode(3), TreeNode(2))
    assert sol.is_same_tree_iterative(root5, root6) is False

    # Edge case: both None ➜ equivalent
    assert sol.is_same_tree_recursive(None, None) is True

    print("All example tests passed! 🎉")
