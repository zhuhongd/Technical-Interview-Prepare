r"""
Binary Tree Right Side View — EECS4070 (Explained, 2 Approaches) + Top-Down Visualization

Problem
-------
You are given the root of a binary tree. Return the values of the nodes that are
visible from the **right side** of the tree, ordered from top (root level) to bottom.

Link
----
https://leetcode.com/problems/binary-tree-right-side-view/

Key Examples
------------
Input : root = [1, 2, 3]
Output: [1, 3]

Input : root = [1, 2, 3, 4, 5, 6, 7]
Output: [1, 3, 7]

Beginner Intuition
------------------
At every depth (level), the “rightmost” node is what you would see if you
stood at the right edge and looked across the tree.

Two classic ways to capture that:

1) **Depth-First Search (right-first preorder)**
   - Traverse as (node → right → left).
   - The *first* node you visit at depth `d` is the rightmost one for that depth,
     so record its value if you haven’t recorded a value for `d` yet.
   - Time: O(n)    Space: O(h) recursion stack (worst O(n), balanced O(log n))

2) **Breadth-First Search (level order)**
   - Process the tree level-by-level with a queue.
   - For each level, the last non-null node you pop is the right view at that level.
   - Time: O(n)    Space: O(w) (w = max width, ≤ n)

Both approaches visit each node once (linear time). Pick whichever you’re more comfortable with.
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
# 1) Depth First Search (right-first preorder)
#    Time: O(n) | Space: O(h)
# ------------------------------------------------------------
# Matches your provided solution; we keep the right-first order so the
# first node seen per depth is the rightmost.
# ============================================================
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res: List[int] = []

        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if not node:
                return
            # First time we reach this depth -> record rightmost
            if depth == len(res):
                res.append(node.val)
            # Right first, then left
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res


# ============================================================
# 2) Breadth First Search (level order)
#    Time: O(n) | Space: O(w)
# ------------------------------------------------------------
# Also mirrors your provided solution: keep the last non-null node per level.
# ============================================================
class SolutionBFS:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res: List[int] = []
        q: Deque[Optional[TreeNode]] = deque([root])
        while q:
            rightmost: Optional[TreeNode] = None
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    rightmost = node
                    q.append(node.left)
                    q.append(node.right)
            if rightmost:
                res.append(rightmost.val)
        return res


# -----------------------------
# Helpers: build / serialize trees (level-order with None)
# -----------------------------
def build_tree_level(values: List[Optional[int]]) -> Optional[TreeNode]:
    r"""
    Robust builder: consume left/right with next(it, None) so odd tails and None runs
    don't misalign. Example [1,2,3,None,5,None,4] ->
        1
       / \
      2   3
       \   \
        5   4
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

        # Iterator may exhaust naturally
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


def visualize_tree(arr: List[Optional[int]], title: str) -> None:
    print(f"\n--- {title} ---")
    print(render_tree_topdown(build_tree_level(arr)))


# -----------------------------
# Teaching Walkthrough (tiny dry runs)
# -----------------------------
def _walkthrough_examples() -> None:
    arr1 = [1, 2, 3]
    arr2 = [1, 2, 3, 4, 5, 6, 7]
    print("Walkthrough 1:")
    visualize_tree(arr1, "tree [1,2,3]")
    print("  Right view (DFS) :", Solution().rightSideView(build_tree_level(arr1)))
    print("  Right view (BFS) :", SolutionBFS().rightSideView(build_tree_level(arr1)))

    print("\nWalkthrough 2:")
    visualize_tree(arr2, "tree [1,2,3,4,5,6,7]")
    print("  Right view (DFS) :", Solution().rightSideView(build_tree_level(arr2)))
    print("  Right view (BFS) :", SolutionBFS().rightSideView(build_tree_level(arr2)))
    print()


# -----------------------------
# Comprehensive offline tests + optional visualizations
# -----------------------------
def _run_tests() -> None:
    impls = [
        ("DFS ", Solution().rightSideView),
        ("BFS ", SolutionBFS().rightSideView),
    ]

    TESTS: List[Tuple[List[Optional[int]], List[int], str]] = [
        # From prompt
        ([1, 2, 3],               [1, 3],      "prompt-1"),
        ([1, 2, 3, 4, 5, 6, 7],   [1, 3, 7],   "prompt-2"),

        # Basics / edges
        ([],                      [],          "empty"),
        ([1],                     [1],         "single"),

        # Classic LC199 shape
        ([1, 2, 3, None, 5, None, 4], [1, 3, 4], "lc199-classic"),

        # Right-skewed (all visible)
        ([1, None, 2, None, 3, None, 4], [1, 2, 3, 4], "right-skewed"),

        # Left-skewed (also all visible, since no right siblings)
        ([1, 2, None, 3, None, 4, None], [1, 2, 3, 4], "left-skewed"),

        # Mixed deeper rightmost changes across levels
        ([1, 2, 3, 4, None, None, 5, None, 6], [1, 3, 5, 6], "mixed-deep"),
    ]

    VIS = {
        "prompt-1",
        "prompt-2",
        "lc199-classic",
        "right-skewed",
        "left-skewed",
        "mixed-deep",
    }

    passed = 0
    total = 0

    for i, (arr, expected, label) in enumerate(TESTS, 1):
        print(f"\n[{i:02d}][{label}] input={arr} expected={expected}")
        if label in VIS:
            visualize_tree(arr, f"viz {label}")

        results = []
        for name, f in impls:
            root = build_tree_level(arr)
            got = f(root)
            ok = (got == expected)
            results.append((name, got, ok))

        for name, got, ok in results:
            total += 1
            passed += ok
            print(f"  {name} -> got={got!s:<16} expected={expected!s:<16} | {'✅' if ok else '❌'}")

        agree = len({tuple(r[1]) for r in results}) == 1
        print(f"  impls-agree: {'✅' if agree else '❌'}")

    print(f"\nPassed {passed}/{total} checks.")


if __name__ == "__main__":
    _walkthrough_examples()
    _run_tests()
