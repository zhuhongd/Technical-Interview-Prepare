r"""
Diameter of Binary Tree — EECS4070 (Explained, Multiple Approaches) + Top-Down Visualization

Problem
-------
The diameter of a binary tree is the length (#edges) of the **longest path** between ANY two nodes.
The path does **not** have to pass through the root.

Link
----
https://leetcode.com/problems/diameter-of-binary-tree/

Key Examples
------------
Input : root = [1, None, 2, 3, 4, 5]
Output: 3
Explanation: A longest path is 5 → 3 → 2 → 4 (3 edges). Another is 1 → 2 → 3 → 5 (also 3 edges).

Input : root = [1, 2, 3]
Output: 2
Explanation: Longest path 2 → 1 → 3 (2 edges).

Beginner Intuition
------------------
Think “what’s the longest walk you can take in the tree if you can start and end anywhere?”
For any node:
  - Let LH = height of its left subtree (in **#nodes**)
  - Let RH = height of its right subtree (in **#nodes**)
  - A long path that **passes through** this node has edges = LH + RH
So if we can compute subtree heights for every node, the diameter is the maximum LH+RH over all nodes.

Approach Menu
-------------
1) **Brute Force (O(N^2) worst-case)**  
   For each node:
     - compute height(left) and height(right) (each is O(N) in worst-case)
     - candidate diameter = left_height + right_height
     - also recurse to children to get their best
   Simple but recomputes heights many times.

2) **Depth-First Search (O(N))**  
   Post-order traversal:
     - From each node, return its height (in #nodes)
     - Update a global `res` with left_height + right_height (edges)
   Each node is visited once; heights are computed once.

3) **Iterative DFS (O(N))**  
   Emulate post-order with your own stack:
     - Use a dict to store (height, diameter) for each visited node
     - Combine children’s results when you pop a node the second time

Conventions
-----------
• We use **height in #nodes** (leaf has height 1; empty tree has height 0).  
• The **diameter is in edges**; at a node, edges = left_height + right_height.

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
# 1) Brute Force  (requested version)
#    Time: O(N^2) worst-case | Space: O(H) recursion stack
# ------------------------------------------------------------
class SolutionBrute:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        leftHeight = self.maxHeight(root.left)
        rightHeight = self.maxHeight(root.right)
        diameter = leftHeight + rightHeight  # edges through root
        sub = max(self.diameterOfBinaryTree(root.left),
                  self.diameterOfBinaryTree(root.right))
        return max(diameter, sub)

    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxHeight(root.left), self.maxHeight(root.right))


# ============================================================
# 2) Depth First Search (O(N))  (requested version)
#    Time: O(N) | Space: O(H) recursion stack
# ------------------------------------------------------------
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal res
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            # update best diameter (in edges) at this node
            res = max(res, left + right)
            # return height in #nodes
            return 1 + max(left, right)

        dfs(root)
        return res


# ============================================================
# 3) Iterative DFS (post-order with stack)  (requested version)
#    Time: O(N) | Space: O(N)
# ------------------------------------------------------------
class SolutionIter:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        stack = [root]
        mp: dict[Optional[TreeNode], Tuple[int, int]] = {None: (0, 0)}
        # mp[node] = (height_in_nodes, best_diameter_in_edges_in_subtree)

        while stack:
            node = stack[-1]
            # push left if unseen
            if node.left and node.left not in mp:
                stack.append(node.left)
                continue
            # push right if unseen
            if node.right and node.right not in mp:
                stack.append(node.right)
                continue

            # now both children computed (or None)
            node = stack.pop()
            leftHeight, leftDiameter = mp[node.left]
            rightHeight, rightDiameter = mp[node.right]
            height_here = 1 + max(leftHeight, rightHeight)
            best_here = max(leftHeight + rightHeight, leftDiameter, rightDiameter)
            mp[node] = (height_here, best_here)

        return mp[root][1]


# -----------------------------
# Helpers: build / serialize trees (level-order with None)
# -----------------------------
def build_tree_level(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Robust builder: consume left/right with next(it, None), so odd tails and None runs
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

    return root


def to_level_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """
    Serialize to level-order list with None placeholders.
    Trailing None's are trimmed for compactness (LeetCode-style).
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
    """
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
    root = build_tree_level(arr)
    print(render_tree_topdown(root))


# -----------------------------
# Teaching Walkthrough (tiny dry run)
# -----------------------------
def _walkthrough_example() -> None:
    # Example: [1, None, 2, 3, 4, 5]
    # One possible shape:
    #   1
    #    \
    #     2
    #    / \
    #   3   4
    #  /
    # 5
    arr = [1, None, 2, 3, 4, 5]
    root = build_tree_level(arr)
    ans = Solution().diameterOfBinaryTree(root)
    print("Walkthrough:")
    print(render_tree_topdown(root))
    print("Diameter (edges):", ans)
    print()


# -----------------------------
# Comprehensive offline tests + optional visualizations
# -----------------------------
def _run_tests() -> None:
    impls = [
        ("Brute ", SolutionBrute().diameterOfBinaryTree),
        ("RecDFS", Solution().diameterOfBinaryTree),
        ("IterDF", SolutionIter().diameterOfBinaryTree),
    ]

    TESTS: List[Tuple[List[Optional[int]], int, str]] = [
        # Prompt-like and basics
        ([1, None, 2, 3, 4, 5], 3, "prompt-like-right-biased"),
        ([1, 2, 3],             2, "simple-three"),
        ([],                    0, "empty"),
        ([42],                  0, "single-node"),

        # Skewed
        ([1, 2, None, 3, None, 4, None], 3, "left-skewed-4-nodes"),
        ([1, None, 2, None, 3, None, 4], 3, "right-skewed-4-nodes"),

        # Balanced-ish
        ([1, 2, 3, 4, 5, 6, 7], 4, "perfect-depth3"),   # path 4-2-1-3-7 = 4 edges

        # Diameter not through the root (deep on one side)
        ([1, 2, 3, 4, 5, None, None, 6, None], 4, "left-subtree-long"),
        # e.g., 6-4-2-1-3 is 4 edges

        # Mixed Nones
        ([5, 3, 8, 1, None, None, 9, None, 2], 5, "mixed-nones-longer-left"),
        # Long path: 2-1-3-5-8-9 (5 edges)
    ]

    VIS = {
        "prompt-like-right-biased",
        "left-skewed-4-nodes",
        "right-skewed-4-nodes",
        "perfect-depth3",
        "left-subtree-long",
        "mixed-nones-longer-left",
    }

    passed = 0
    total = 0

    for i, (arr, expected, label) in enumerate(TESTS, 1):
        print(f"\n[{i:02d}][{label}] input={arr!s}")
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
            print(f"  {name:<6} -> got={got:<2} expected={expected:<2} | {'✅' if ok else '❌'}")

        agree = len({r[1] for r in results}) == 1
        print(f"  impls-agree: {'✅' if agree else '❌'}")

    print(f"\nPassed {passed}/{total} checks.")


if __name__ == "__main__":
    _walkthrough_example()
    _run_tests()
