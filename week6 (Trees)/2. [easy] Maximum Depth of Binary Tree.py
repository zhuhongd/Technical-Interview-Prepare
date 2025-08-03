"""
Maximum Depth of Binary Tree — EECS4070 (Explained, Multiple Approaches) + Top-Down Visualization

Problem
-------
Given the root of a binary tree, return its depth.
Depth = number of nodes on the longest path from the root down to the farthest leaf.

Link
----
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Key Examples
------------
Input : root = [1, 2, 3, None, None, 4]
Output: 3
(One longest path is 1 → 3 → 4: 3 nodes)

Input : root = []
Output: 0

Beginner Intuition
------------------
Depth is “how many nodes you count” when you walk from the root down to the **deepest leaf**.
There are three classic ways to compute it:

1) **Recursive DFS (top-down via definition)**:
   - If node is None → depth 0.
   - Otherwise depth = 1 + max(depth(left), depth(right)).

2) **Iterative BFS (level order)**:
   - Traverse level by level; each level you finish adds 1 to depth.

3) **Iterative DFS (explicit stack)**:
   - Keep (node, current_depth) on a stack; update an answer as you go.

Complexity
----------
All three visit every node exactly once:
Time : O(N)
Space: O(H) for DFS (H = height), O(W) for BFS (W = max width). Worst-case O(N).
"""

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


# ============================================================
# ✅ Active Solution: Recursive DFS (definition-driven)
#    Time: O(N) | Space: O(H) recursion stack
# ============================================================
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# ============================================================
# Alternative 1: Iterative BFS (level order)
#    Time: O(N) | Space: O(W)
# ============================================================
class SolutionBFS:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = 0
        q: Deque[TreeNode] = deque([root])
        while q:
            # Process one whole level
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:  q.append(node.left)
                if node.right: q.append(node.right)
            depth += 1
        return depth


# ============================================================
# Alternative 2: Iterative DFS (explicit stack)
#    Time: O(N) | Space: O(H)
# ============================================================
class SolutionDFSIter:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack: List[Tuple[TreeNode, int]] = [(root, 1)]
        best = 0
        while stack:
            node, d = stack.pop()
            best = max(best, d)
            if node.left:  stack.append((node.left,  d + 1))
            if node.right: stack.append((node.right, d + 1))
        return best


# -----------------------------
# Helpers: build / serialize trees (level-order with None)
# -----------------------------
def build_tree_level(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Build a binary tree from a level-order list where None means “no node”.
    Example: [1,2,3,None,4] ->
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
        # left
        v_left = next(it, None)
        if v_left is not None:
            node.left = TreeNode(v_left)
            q.append(node.left)
        # right
        v_right = next(it, None)
        if v_right is not None:
            node.right = TreeNode(v_right)
            q.append(node.right)
        # iterator may already be exhausted; loop will exit naturally
    return root


def to_level_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """
    Serialize to a level-order list with None for missing children.
    Trailing None's trimmed for compactness.
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
# Top-Down ASCII Tree Renderer (same style you asked for)
# -----------------------------
def _render_topdown_aux(node: Optional[TreeNode]) -> Tuple[List[str], int, int, int]:
    """
    Recursively build ASCII lines for a binary tree (top-down with / and \ connectors).

    Returns:
        lines: List[str]  -> the rendered lines
        width: int        -> total width of the rendering
        height: int       -> number of lines
        middle: int       -> horizontal position of the node's root label
    """
    if node is None:
        return (["·"], 1, 1, 0)  # placeholder (we won’t show it in final)

    s = str(node.val)
    s_width = len(s)

    # Leaf node
    if node.left is None and node.right is None:
        return ([s], s_width, 1, s_width // 2)

    # Only left child
    if node.right is None:
        left_lines, left_w, left_h, left_mid = _render_topdown_aux(node.left)
        first_line = " " * (left_mid + 1) + "_" * (left_w - left_mid - 1) + s
        second_line = " " * left_mid + "/" + " " * (left_w - left_mid - 1 + s_width)
        shifted = [line + " " * s_width for line in left_lines]
        return ([first_line, second_line] + shifted,
                left_w + s_width, left_h + 2, (left_w + s_width) // 2)

    # Only right child
    if node.left is None:
        right_lines, right_w, right_h, right_mid = _render_topdown_aux(node.right)
        first_line = s + "_" * right_mid + " " * (right_w - right_mid)
        second_line = " " * (s_width + right_mid) + "\\" + " " * (right_w - right_mid - 1)
        shifted = [" " * s_width + line for line in right_lines]
        return ([first_line, second_line] + shifted,
                s_width + right_w, right_h + 2, s_width // 2)

    # Two children
    left_lines, left_w, left_h, left_mid = _render_topdown_aux(node.left)
    right_lines, right_w, right_h, right_mid = _render_topdown_aux(node.right)
    first_line = (" " * (left_mid + 1)
                  + "_" * (left_w - left_mid - 1)
                  + s
                  + "_" * right_mid
                  + " " * (right_w - right_mid))
    second_line = (" " * left_mid + "/"
                   + " " * (left_w - left_mid - 1 + s_width + right_mid)
                   + "\\"
                   + " " * (right_w - right_mid - 1))

    # Make both sides the same height
    if left_h < right_h:
        left_lines += [" " * left_w] * (right_h - left_h)
    elif right_h < left_h:
        right_lines += [" " * right_w] * (left_h - right_h)

    zipped = [l + " " * s_width + r for l, r in zip(left_lines, right_lines)]
    return ([first_line, second_line] + zipped,
            left_w + s_width + right_w,
            max(left_h, right_h) + 2,
            left_w + s_width // 2)


def render_tree_topdown(root: Optional[TreeNode]) -> str:
    """
    Render a binary tree top-down with / and \ connectors, like:

            1
           / \
          2   3
           \
            4
    """
    if root is None:
        return "(empty)"
    lines, _, _, _ = _render_topdown_aux(root)
    # Remove placeholder dots if any slipped through
    lines = [line.replace("·", " ") for line in lines]
    return "\n".join(lines)


def visualize_tree(arr: List[Optional[int]], title: str) -> None:
    """
    Build a tree from level-order `arr` and print the top-down ASCII rendering.
    """
    print(f"\n--- {title} ---")
    root = build_tree_level(arr)
    print(render_tree_topdown(root))


# -----------------------------
# Teaching Walkthrough (tiny)
# -----------------------------
def _walkthrough_example() -> None:
    # Example: [1,2,3,None, None, 4] → depth 3 (1→3→4)
    arr = [1, 2, 3, None, None, 4]
    root = build_tree_level(arr)
    d = Solution().maxDepth(root)
    print("Walkthrough:")
    print(render_tree_topdown(root))
    print("Depth:", d)
    print()


# -----------------------------
# Comprehensive offline tests + optional visualizations
# -----------------------------
def _run_tests() -> None:
    impls = [
        ("RecDFS", Solution().maxDepth),
        ("BFS",    SolutionBFS().maxDepth),
        ("DFSIt",  SolutionDFSIter().maxDepth),
    ]

    TESTS: List[Tuple[List[Optional[int]], int, str]] = [
        # From prompt
        ([1, 2, 3, None, None, 4], 3, "prompt-1"),

        # Basics / edges
        ([],                         0, "empty"),
        ([42],                       1, "single"),

        # Skewed shapes (good for seeing recursion depth vs BFS levels)
        ([1, 2, None, 3, None, 4, None], 4, "left-skewed"),
        ([1, None, 2, None, 3, None, 4], 4, "right-skewed"),

        # Perfect tree depth 3
        ([1, 2, 3, 4, 5, 6, 7],      3, "perfect-depth3"),

        # Classic LC shape
        ([3, 9, 20, None, None, 15, 7], 3, "classic-lc"),

        # Mixed Nones, deeper on one side
        ([5, 3, 8, 1, None, None, 9, None, 2], 4, "mixed-nones"),
    ]

    passed = 0
    total = 0

    for i, (arr, expected, label) in enumerate(TESTS, 1):
        print(f"\n[{i:02d}][{label}] input={arr}")
        # Visualize selected interesting cases
        VISUALIZE_LABELS = {
            "prompt-1",
            "left-skewed",
            "right-skewed",
            "perfect-depth3",
            "classic-lc",
            "mixed-nones",
        }
        if label in VISUALIZE_LABELS:
            visualize_tree(arr, f"viz {label}")

        # Run three implementations and verify agreement + expected match
        results = []
        for name, f in impls:
            root = build_tree_level(arr)
            got = f(root)
            ok = (got == expected)
            results.append((name, got, ok))

        for name, got, ok in results:
            total += 1
            passed += ok
            print(f"  {name:<6} -> got={got:<2} expected={expected:<2} | {'✅' if ok else '❌'}")

        agree = len({r[1] for r in results}) == 1
        print(f"  impls-agree: {'✅' if agree else '❌'}")

    print(f"\nPassed {passed}/{total} checks.")


if __name__ == "__main__":
    _walkthrough_example()
    _run_tests()
