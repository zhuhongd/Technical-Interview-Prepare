r"""
Balanced Binary Tree — EECS4070 (Your 3 Approaches) + Top-Down Visualization

Problem
-------
Given the root of a binary tree, return True if it is height-balanced and False otherwise.

A height-balanced binary tree is one in which, for **every** node, the heights of the left and right
subtrees differ by **no more than 1**.

Link
----
https://leetcode.com/problems/balanced-binary-tree/

Key Examples
------------
Input : root = [1, 2, 3, None, None, 4]
Output: True
Reason:
    1
   / \
  2   3
     /
    4
Every node’s left/right subtree heights differ by ≤ 1.

Input : root = [1, 2, 3, None, None, 4, None, 5]
Output: False
Reason:
    1
   / \
  2   3
     /
    4
   /
  5
At node "3", left height = 2 (3→4→5), right height = 0 → diff = 2 > 1 → not balanced.

Input : root = []
Output: True

Beginner Intuition
------------------
“Balanced” means **no subtree is much taller than its sibling**. For each node:
- Let L = height(left subtree), R = height(right subtree).
- The node is locally balanced if |L - R| ≤ 1.
- The whole tree is balanced if this holds at **every** node.

We will include exactly the three solution styles you asked for:
1) **Brute Force** (O(N^2)) — recompute subtree heights at each node.
2) **Depth-First Search (post-order)** (O(N)) — return [balanced?, height] from each subtree once.
3) **Iterative DFS (post-order)** (O(N)) — emulate recursion with an explicit stack.

Height Convention Used
----------------------
- height(None) = 0
- height(leaf) = 1
- height(node) = 1 + max(height(left), height(right))
"""

from collections import deque
from typing import Optional, List, Tuple, Deque, Dict


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
# 1) Brute Force — exactly your logic (renamed class to avoid collisions)
#    Time: O(N^2) worst-case | Space: O(H) recursion stack
# ============================================================
class SolutionBrute:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left = self.height(root.left)
        right = self.height(root.right)
        if abs(left - right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))


# ============================================================
# 2) Depth-First Search (post-order) — exactly your logic (renamed)
#    Time: O(N) | Space: O(H)
#    dfs returns [balanced: bool, height: int]
# ============================================================
class SolutionDFS:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> List[int]:
            if not node:
                return [True, 0]

            left = dfs(node.left)
            right = dfs(node.right)
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]


# ============================================================
# 3) Iterative DFS (post-order) — exactly your logic (renamed)
#    Time: O(N) | Space: O(N)
#    Uses stack with "last" pointer and a map of depths
# ============================================================
class SolutionDFSIter:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack: List[TreeNode] = []
        node = root
        last: Optional[TreeNode] = None
        depths: Dict[Optional[TreeNode], int] = {}

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    stack.pop()
                    left = depths.get(node.left, 0)
                    right = depths.get(node.right, 0)

                    if abs(left - right) > 1:
                        return False

                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right

        return True


# -----------------------------
# Helpers: build / serialize trees (level-order with None)
# -----------------------------
def build_tree_level(values: List[Optional[int]]) -> Optional[TreeNode]:
    r"""
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
    root = build_tree_level(arr)
    print(render_tree_topdown(root))


# -----------------------------
# Teaching Walkthrough (tiny dry runs)
# -----------------------------
def _walkthrough_examples() -> None:
    arr1 = [1, 2, 3, None, None, 4]
    arr2 = [1, 2, 3, None, None, 4, None, 5]
    print("Walkthrough 1 (should be balanced -> True):")
    root1 = build_tree_level(arr1)
    print(render_tree_topdown(root1))
    print("Balanced? (DFS):", SolutionDFS().isBalanced(root1), "\n")

    print("Walkthrough 2 (should be NOT balanced -> False):")
    root2 = build_tree_level(arr2)
    print(render_tree_topdown(root2))
    print("Balanced? (DFS):", SolutionDFS().isBalanced(root2), "\n")


# -----------------------------
# Comprehensive offline tests + optional visualizations
# -----------------------------
def _run_tests() -> None:
    impls = [
        ("Brute ", SolutionBrute().isBalanced),
        ("DFS   ", SolutionDFS().isBalanced),
        ("DFSIt ", SolutionDFSIter().isBalanced),
    ]

    TESTS: List[Tuple[List[Optional[int]], bool, str]] = [
        # From prompt-like
        ([1, 2, 3, None, None, 4],           True,  "prompt-1-balanced"),
        ([1, 2, 3, None, None, 4, None, 5],  False, "prompt-2-unbalanced"),
        ([],                                  True,  "empty-true"),

        # Basics
        ([42],                                True,  "single"),

        # Barely unbalanced at/near root
        ([1, 2, 3, 4, None, None, None, 5],  False, "root-barely-unbalanced"),

        # “Almost perfect” but still balanced
        ([1, 2, 3, 4, 5, 6, 7, None, 8],     True,  "perfect-plus-one"),

        # Skewed shapes
        ([1, 2, None, 3, None, 4, None],      False, "left-skewed-4"),
        ([1, None, 2, None, 3, None, 4],      False, "right-skewed-4"),

        # Same values, structure-only test
        ([7, 7, 7, 7, 7, None, None, 7, 7],   False,  "values-dont-matter"),

        # Balanced-ish classics
        ([1, 2, 3, 4, 5, 6, 7],               True,  "perfect-depth3"),
        ([3, 9, 20, None, None, 15, 7],       True,  "classic-lc-balanced"),

        # Slightly unbalanced at lower level
        ([5, 3, 8, 1, None, None, 9, None, 2], False, "mixed-nones-unbalanced"),
        # At node 3: left height 2 (1→2), right height 0 -> diff 2
    ]

    VIS = {
        "prompt-1-balanced",
        "prompt-2-unbalanced",
        "left-skewed-4",
        "right-skewed-4",
        "perfect-depth3",
        "classic-lc-balanced",
        "mixed-nones-unbalanced",
        "root-barely-unbalanced",
        "perfect-plus-one",
        "values-dont-matter",
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
            print(f"  {name} -> got={str(got):<5} expected={str(expected):<5} | {'✅' if ok else '❌'}")

        agree = len({r[1] for r in results}) == 1
        print(f"  impls-agree: {'✅' if agree else '❌'}")

    print(f"\nPassed {passed}/{total} checks.")


if __name__ == "__main__":
    _walkthrough_examples()
    _run_tests()
