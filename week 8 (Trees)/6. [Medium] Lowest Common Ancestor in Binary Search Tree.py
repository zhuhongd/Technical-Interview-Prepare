r"""
Lowest Common Ancestor in a Binary Search Tree — EECS4070 (Explained, Two Approaches) + Top-Down Visualization

Problem
-------
Given a Binary Search Tree (BST) with **unique** node values and two nodes `p` and `q` from the tree,
return their **lowest common ancestor (LCA)**.

The LCA of `p` and `q` is the lowest node in the tree that has **both** `p` and `q` as descendants.
(A node can be a descendant of itself.)

Link
----
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Key Examples
------------
Input : root = [5,3,8,1,4,7,9,None,2], p = 3, q = 8
Output: 5

Input : root = [5,3,8,1,4,7,9,None,2], p = 3, q = 4
Output: 3   (a node can be an ancestor of itself)

Beginner Intuition (BST ordering)
---------------------------------
In a BST, for any node `x`:
- All values in `x.left` are **less than** `x.val`
- All values in `x.right` are **greater than** `x.val`

Therefore:
- If `p.val` and `q.val` are both **smaller** than `root.val`, the LCA must be in the **left** subtree.
- If both are **greater** than `root.val`, the LCA must be in the **right** subtree.
- Otherwise, `root` is the **split point** → that `root` is the LCA.

Approaches
----------
1) Recursion (your solution)
   - Recurse down left or right using the BST property.
   - When values split (or equal), return the current root.
   Time: O(h), Space: O(h) recursion stack (h = tree height)

2) Iteration (your solution)
   - Walk down the tree iteratively using the same split logic.
   Time: O(h), Space: O(1)

Why this works
--------------
The first node where `p` and `q` are on **different sides** (or one equals the current node)
is by definition their **lowest** common ancestor due to BST ordering.

Complexity Summary
------------------
Time : O(h) for both recursion and iteration  
Space: O(h) recursion; O(1) iteration
"""

from __future__ import annotations
from collections import deque
from typing import Optional, List, Tuple, Deque


# -----------------------------
# Tree definition (LeetCode-style)
# -----------------------------
class TreeNode:
    def __init__(self, val: int = 0,
                 left: "Optional[TreeNode]" = None,
                 right: "Optional[TreeNode]" = None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode(val={self.val})"


# ============================================================
# 1) Recursion (your solution)
#    Time: O(h) | Space: O(h)
# ============================================================
class SolutionRecursive:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        if not root or not p or not q:
            return None
        # If both p and q are strictly less than root, LCA is in the left subtree.
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # If both are strictly greater, LCA is in the right subtree.
        elif min(p.val, q.val) > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # Otherwise, current root is the split point --> LCA.
        else:
            return root


# ============================================================
# 2) Iteration (your solution)
#    Time: O(h) | Space: O(1)
# ============================================================
class SolutionIterative:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        cur = root
        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur
        return None


# ============================================================
# Default Solution for LC submission (choose one)
# ============================================================
class Solution(SolutionIterative):
    """Default to the iterative solution (O(1) extra space)."""
    pass


# -----------------------------
# Helpers: build / serialize BST from level-order with None
# -----------------------------
def build_tree_level(values: List[Optional[int]]) -> Optional[TreeNode]:
    r"""
    Robust builder: consume left/right with next(it, None) so odd tails and None runs
    don't misalign. Example [5,3,8,1,4,7,9,None,2] ->
            5
          /   \
         3     8
        / \   / \
       1   4 7   9
        \
         2
    """
    if not values:
        return None

    it = iter(values)
    root_val = next(it, None)
    if root_val is None:
        return None

    root = TreeNode(root_val)
    q: Deque[TreeNode] = deque([root])

    while q:
        node = q.popleft()

        v_left = next(it, None)
        if v_left is not None:
            node.left = TreeNode(v_left)
            q.append(node.left)

        v_right = next(it, None)
        if v_right is not None:
            node.right = TreeNode(v_right)
            q.append(node.right)

        # Iterator may naturally exhaust here
    return root


def to_level_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """
    Serialize to level-order list with None placeholders.
    Trailing None's are trimmed (LeetCode-style).
    """
    if root is None:
        return []
    out: List[Optional[int]] = []
    q: Deque[Optional[TreeNode]] = deque([root])
    while q:
        node = q.popleft()
        if node is None:
            out.append(None)
        else:
            out.append(node.val)
            q.append(node.left)
            q.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


def find_by_value(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """Find a node by value in a BST (unique values)."""
    cur = root
    while cur:
        if val == cur.val:
            return cur
        cur = cur.left if val < cur.val else cur.right
    return None


# -----------------------------
# Top-Down ASCII Tree Renderer (your preferred style)
# -----------------------------
def _render_topdown_aux(node: Optional[TreeNode]) -> Tuple[List[str], int, int, int]:
    r"""
    Build ASCII lines top-down with / and \ connectors.
    Returns: (lines, width, height, middle_index)
    """
    if node is None:
        return (["·"], 1, 1, 0)

    s = str(node.val)
    s_w = len(s)

    # Leaf
    if node.left is None and node.right is None:
        return ([s], s_w, 1, s_w // 2)

    # Only left
    if node.right is None:
        left_lines, left_w, left_h, left_mid = _render_topdown_aux(node.left)
        first = " " * (left_mid + 1) + "_" * (left_w - left_mid - 1) + s
        second = " " * left_mid + "/" + " " * (left_w - left_mid - 1 + s_w)
        shifted = [line + " " * s_w for line in left_lines]
        return ([first, second] + shifted, left_w + s_w, left_h + 2, (left_w + s_w) // 2)

    # Only right
    if node.left is None:
        right_lines, right_w, right_h, right_mid = _render_topdown_aux(node.right)
        first = s + "_" * right_mid + " " * (right_w - right_mid)
        second = " " * (s_w + right_mid) + "\\" + " " * (right_w - right_mid - 1)
        shifted = [" " * s_w + line for line in right_lines]
        return ([first, second] + shifted, s_w + right_w, right_h + 2, s_w // 2)

    # Two children
    left_lines, left_w, left_h, left_mid = _render_topdown_aux(node.left)
    right_lines, right_w, right_h, right_mid = _render_topdown_aux(node.right)
    first = (" " * (left_mid + 1)
             + "_" * (left_w - left_mid - 1)
             + s
             + "_" * right_mid
             + " " * (right_w - right_mid))
    second = (" " * left_mid + "/"
              + " " * (left_w - left_mid - 1 + s_w + right_mid)
              + "\\"
              + " " * (right_w - right_mid - 1))

    if left_h < right_h:
        left_lines += [" " * left_w] * (right_h - left_h)
    elif right_h < left_h:
        right_lines += [" " * right_w] * (left_h - right_h)

    merged = [l + " " * s_w + r for l, r in zip(left_lines, right_lines)]
    return ([first, second] + merged, left_w + s_w + right_w, max(left_h, right_h) + 2, left_w + s_w // 2)


def render_tree_topdown(root: Optional[TreeNode]) -> str:
    if root is None:
        return "(empty)"
    lines, _, _, _ = _render_topdown_aux(root)
    return "\n".join(line.replace("·", " ") for line in lines)


def visualize_lca(arr: List[Optional[int]], p_val: int, q_val: int, lca_val: int, title: str) -> None:
    print(f"\n--- {title} ---")
    root = build_tree_level(arr)
    print(render_tree_topdown(root))
    print(f"p = {p_val}, q = {q_val}, expected LCA = {lca_val}")


# -----------------------------
# Teaching Walkthrough (tiny)
# -----------------------------
def _walkthrough_example() -> None:
    arr = [5, 3, 8, 1, 4, 7, 9, None, 2]
    root = build_tree_level(arr)
    p = find_by_value(root, 3)
    q = find_by_value(root, 8)
    ans_iter = SolutionIterative().lowestCommonAncestor(root, p, q)
    ans_recu = SolutionRecursive().lowestCommonAncestor(root, p, q)
    print("Walkthrough:")
    print(render_tree_topdown(root))
    print(f"p=3, q=8 -> LCA (iter) = {ans_iter.val if ans_iter else None}, LCA (recur) = {ans_recu.val if ans_recu else None}\n")


# -----------------------------
# Comprehensive offline tests + optional visualizations
# -----------------------------
def _run_tests() -> None:
    impls = [
        ("Recur", SolutionRecursive().lowestCommonAncestor),
        ("Iter",  SolutionIterative().lowestCommonAncestor),
    ]

    TESTS: List[Tuple[List[Optional[int]], int, int, int, str]] = [
        # From prompt
        ([5,3,8,1,4,7,9,None,2], 3, 8, 5, "prompt-1-split-at-root"),
        ([5,3,8,1,4,7,9,None,2], 3, 4, 3, "prompt-2-one-is-ancestor"),

        # Basics / edges within constraints (p != q; both exist; unique values)
        ([2,1,3], 1, 3, 2, "tiny-balanced-root-is-lca"),
        ([6,2,8,0,4,7,9,None,None,3,5], 2, 8, 6, "classic-lc-root-split"),
        ([6,2,8,0,4,7,9,None,None,3,5], 2, 4, 2, "ancestor-on-left-branch"),
        ([6,2,8,0,4,7,9,None,None,3,5], 7, 9, 8, "both-on-right"),
        ([5,3,7,2,4,6,8,1], 1, 4, 3, "deep-left-and-mid"),
        # Skewed (height ~ n)
        ([1, None, 2, None, 3, None, 4], 2, 4, 2, "right-skewed"),
    ]

    VIS = {
        "prompt-1-split-at-root",
        "prompt-2-one-is-ancestor",
        "classic-lc-root-split",
        "ancestor-on-left-branch",
        "right-skewed",
    }

    passed = 0
    total = 0

    for i, (arr, p_val, q_val, expected_lca, label) in enumerate(TESTS, 1):
        print(f"\n[{i:02d}][{label}] p={p_val} q={q_val} expected={expected_lca}  tree={arr}")
        if label in VIS:
            visualize_lca(arr, p_val, q_val, expected_lca, f"viz {label}")

        root = build_tree_level(arr)
        p = find_by_value(root, p_val)
        q = find_by_value(root, q_val)

        results = []
        for name, f in impls:
            got_node = f(root, p, q)
            got = got_node.val if got_node else None
            ok = (got == expected_lca)
            results.append((name, got, ok))

        for name, got, ok in results:
            total += 1
            passed += ok
            print(f"  {name:<5} -> got={got!s:<3} expected={expected_lca!s:<3} | {'✅' if ok else '❌'}")

        agree = len({r[1] for r in results}) == 1
        print(f"  impls-agree: {'✅' if agree else '❌'}")

    print(f"\nPassed {passed}/{total} checks.")


if __name__ == "__main__":
    _walkthrough_example()
    _run_tests()
