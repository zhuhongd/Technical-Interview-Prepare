r"""
Binary Tree Level Order Traversal — EECS4070 (Explained, DFS & BFS) + Top-Down Visualization

Problem
-------
Given a binary tree root, return the level order traversal as a list of lists,
where each inner list contains the node values for one level (from left to right).

Link
----
https://leetcode.com/problems/binary-tree-level-order-traversal/

Key Examples
------------
Input : root = [1, 2, 3, 4, 5, 6, 7]
Output: [[1], [2, 3], [4, 5, 6, 7]]

Input : root = [1]
Output: [[1]]

Input : root = []
Output: []

Beginner Intuition
------------------
“Level order” means **breadth-first**: visit all nodes at depth 0, then all at depth 1, etc.
There are two clean ways to produce the same result:

1) Depth-First Search (**DFS**) with a `depth` parameter  
   - Recurse (node, depth).  
   - When you first reach a new depth, append a new sublist.  
   - Append `node.val` to `res[depth]`, then recurse left and right.

2) Breadth-First Search (**BFS**) using a queue (classic level-order)  
   - Push the root; at each loop, process the **current queue length** as one level.  
   - Enqueue children; collect this level’s values and append to the result.

Complexity
----------
Let n be the number of nodes, h the height, and W the maximum width:
Time : O(n) — every node is visited once  
Space: O(n) — result holds all nodes; DFS uses O(h) stack, BFS uses O(W) queue

We include a small ASCII renderer to visualize shapes in the terminal.
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
# 1) Depth First Search (your solution)
#    Time: O(n) | Space: O(n) overall (O(h) call stack)
# ============================================================
class SolutionDFS:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res: List[List[int]] = []

        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if not node:
                return
            if len(res) == depth:   # first time we reach this depth
                res.append([])
            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return res


# ============================================================
# 2) Breadth First Search (your solution)
#    Time: O(n) | Space: O(n) overall (O(W) queue)
# ============================================================
class SolutionBFS:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res: List[List[int]] = []
        q: Deque[Optional[TreeNode]] = deque([root])

        while q:
            level_size = len(q)
            level: List[int] = []
            for _ in range(level_size):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:  # only append non-empty levels
                res.append(level)
        return res


# ============================================================
# Default Solution for LC submission
#   (Pick one approach — DFS shown here)
# ============================================================
class Solution(SolutionDFS):
    """Default to DFS-by-depth; BFS alternative is above."""
    pass


# -----------------------------
# Helpers: build / serialize trees (level-order with None)
# -----------------------------
def build_tree_level(values: List[Optional[int]]) -> Optional[TreeNode]:
    r"""
    Robust builder: consume left/right with next(it, None) so odd tails and None runs
    don't misalign. Example [1,2,3,None,4] ->
        1
       / \
      2   3
       \
        4
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


def visualize_levels(arr: List[Optional[int]], title: str) -> None:
    print(f"\n--- {title} ---")
    root = build_tree_level(arr)
    print(render_tree_topdown(root))
    dfs_levels = SolutionDFS().levelOrder(build_tree_level(arr))
    bfs_levels = SolutionBFS().levelOrder(build_tree_level(arr))
    print("DFS levels:", dfs_levels)
    print("BFS levels:", bfs_levels)


# -----------------------------
# Teaching Walkthrough (tiny)
# -----------------------------
def _walkthrough_example() -> None:
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = build_tree_level(arr)
    ans_dfs = SolutionDFS().levelOrder(root)
    ans_bfs = SolutionBFS().levelOrder(build_tree_level(arr))
    print("Walkthrough:")
    print(render_tree_topdown(root))
    print("DFS:", ans_dfs)
    print("BFS:", ans_bfs, "\n")


# -----------------------------
# Comprehensive offline tests + optional visualizations
# -----------------------------
def _run_tests() -> None:
    dfs = SolutionDFS().levelOrder
    bfs = SolutionBFS().levelOrder

    TESTS: List[Tuple[List[Optional[int]], List[List[int]], str]] = [
        # Prompt-style
        ([1, 2, 3, 4, 5, 6, 7], [[1], [2, 3], [4, 5, 6, 7]], "perfect-3-levels"),
        ([1],                   [[1]],                         "single"),
        ([],                    [],                            "empty"),

        # Mixed shapes
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]], "classic-lc"),
        ([5, 2, 8, 1, 3, 7, 9, None, None, None, 4], [[5], [2, 8], [1, 3, 7, 9], [4]], "mixed-nones"),

        # Skewed (depth shows clearly)
        ([1, 2, None, 3, None, 4, None], [[1], [2], [3], [4]], "left-skewed"),
        ([1, None, 2, None, 3, None, 4], [[1], [2], [3], [4]], "right-skewed"),

        # Wide last level with gaps (still level-order grouping)
        ([10, 5, 15, 2, 7, None, 20, None, None, 6], [[10], [5, 15], [2, 7, 20], [6]], "gappy-last-level"),
    ]

    VIS = {
        "perfect-3-levels",
        "classic-lc",
        "mixed-nones",
        "left-skewed",
        "right-skewed",
        "gappy-last-level",
    }

    passed = 0
    total = 0

    for i, (arr, expected, label) in enumerate(TESTS, 1):
        print(f"\n[{i:02d}][{label}] input={arr}  expected={expected}")
        if label in VIS:
            visualize_levels(arr, f"viz {label}")

        # Run both implementations and compare to expected
        root = build_tree_level(arr)
        got_dfs = dfs(root)
        got_bfs = bfs(build_tree_level(arr))

        for name, got in (("DFS", got_dfs), ("BFS", got_bfs)):
            total += 1
            ok = (got == expected)
            passed += ok
            print(f"  {name:<3} -> got={got} | {'✅' if ok else '❌'}")

        agree = (got_dfs == got_bfs)
        print(f"  impls-agree: {'✅' if agree else '❌'}")

    print(f"\nPassed {passed}/{total} checks.")


if __name__ == "__main__":
    _walkthrough_example()
    _run_tests()
