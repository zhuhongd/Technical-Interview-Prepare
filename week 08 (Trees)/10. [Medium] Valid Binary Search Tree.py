r"""
Valid Binary Search Tree — EECS4070 (Explained, 3 Approaches) + Top-Down Visualization

Problem
-------
Given the root of a binary tree, return True if it is a **valid** Binary Search Tree (BST),
otherwise return False.

A valid BST satisfies, **for every node**:
  • all keys in the left subtree are **strictly less** than the node’s key  
  • all keys in the right subtree are **strictly greater** than the node’s key  
  • both subtrees are themselves BSTs

Link
----
https://leetcode.com/problems/validate-binary-search-tree/

Key Examples
------------
Input : root = [2, 1, 3]
Output: True

Input : root = [1, 2, 3]
Output: False
Reason: node "2" is in the left subtree of "1" but 2 > 1 (violates BST rule).

Beginner Intuition
------------------
BST = “everything on the left is smaller, everything on the right is larger,” and this rule
must hold at **every** node, not just parent/child pairs.

There are multiple ways to verify this:

1) **Brute Force (local check + re-check subtrees)**  
   For each node, verify that **every** node in its left subtree is < node.val and
   **every** node in its right subtree is > node.val, then recurse into children.
   This repeats work and can be O(n^2) in the worst case, but it matches many learners’ first idea.

2) **Depth-First Search with bounds (recommended)**  
   Carry a (low, high) range down the tree:
     - at a node with value v, we must have low < v < high
     - recurse left with range (low, v), recurse right with range (v, high)
   This is linear and elegant.

3) **Breadth-First Search with bounds (queue)**  
   Same logic as (2), but iteratively: push (node, low, high) into a queue and validate while popping.

Complexity
----------
Let n = number of nodes, h = height, W = maximum width:
• Brute Force:  Time O(n^2) worst-case, Space O(n) (recursion depth up to h)  
• DFS w/ bounds: Time O(n), Space O(h) recursion (worst O(n), balanced O(log n))  
• BFS w/ bounds: Time O(n), Space O(W) (queue)
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
# 1) Brute Force (your provided approach, O(n^2) worst-case)
#    For each node, ensure all nodes in left-subtree < node.val
#    and all in right-subtree > node.val; then recurse.
# ============================================================
class SolutionBrute:
    # The following two small helpers encode the inequality direction.
    left_check  = staticmethod(lambda val, limit: val < limit)
    right_check = staticmethod(lambda val, limit: val > limit)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # Check all nodes in left subtree are < root.val
        # and all nodes in right subtree are > root.val
        if (not self._all_within(root.left,  root.val, self.left_check) or
            not self._all_within(root.right, root.val, self.right_check)):
            return False

        # Then recurse to ensure the same holds everywhere
        return self.isValidBST(root.left) and self.isValidBST(root.right)

    def _all_within(self,
                    node: Optional[TreeNode],
                    limit: int,
                    check) -> bool:
        """Return True iff ALL nodes in this subtree satisfy check(node.val, limit).
           (This is what induces the O(n^2) worst-case.)"""
        if not node:
            return True
        if not check(node.val, limit):
            return False
        return self._all_within(node.left, limit, check) and \
               self._all_within(node.right, limit, check)


# ============================================================
# 2) Depth-First Search with bounds (recommended)
#    Time: O(n) | Space: O(h)
# ============================================================
class SolutionDFSBounds:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:
                return True
            if not (low < node.val < high):
                return False
            # Left: everything must be < node.val
            # Right: everything must be > node.val
            return valid(node.left, low, node.val) and \
                   valid(node.right, node.val, high)

        return valid(root, float("-inf"), float("inf"))


# ============================================================
# 3) Breadth-First Search with bounds (queue)
#    Time: O(n) | Space: O(W)
# ============================================================
class SolutionBFSBounds:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q: Deque[Tuple[TreeNode, float, float]] = deque([(root, float("-inf"), float("inf"))])
        while q:
            node, low, high = q.popleft()
            if not (low < node.val < high):
                return False
            if node.left:
                q.append((node.left, low, node.val))
            if node.right:
                q.append((node.right, node.val, high))
        return True


# ============================================================
# Default Solution for LC submission
#   (Pick the recommended approach by default)
# ============================================================
class Solution(SolutionDFSBounds):
    """Default to DFS-bounds; other approaches above for study/contrast."""
    pass


# -----------------------------
# Helpers: build / serialize trees (level-order with None)
# -----------------------------
def build_tree_level(values: List[Optional[int]]) -> Optional[TreeNode]:
    r"""
    Robust builder: consume left/right with next(it, None) so odd tails and None runs
    don't misalign. Example [2,1,3] ->
        2
       / \
      1   3
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
# Teaching Walkthrough (tiny)
# -----------------------------
def _walkthrough_example() -> None:
    arr_valid = [2, 1, 3]
    arr_invalid = [1, 2, 3]   # not a BST: 2 is left child of 1 but 2 > 1
    print("Walkthrough 1 (valid):")
    visualize_tree(arr_valid, "valid [2,1,3]")
    print("  DFS-bounds  :", SolutionDFSBounds().isValidBST(build_tree_level(arr_valid)))
    print("  BFS-bounds  :", SolutionBFSBounds().isValidBST(build_tree_level(arr_valid)))
    print("  Brute-force :", SolutionBrute().isValidBST(build_tree_level(arr_valid)))
    print("\nWalkthrough 2 (invalid):")
    visualize_tree(arr_invalid, "invalid [1,2,3]")
    print("  DFS-bounds  :", SolutionDFSBounds().isValidBST(build_tree_level(arr_invalid)))
    print("  BFS-bounds  :", SolutionBFSBounds().isValidBST(build_tree_level(arr_invalid)))
    print("  Brute-force :", SolutionBrute().isValidBST(build_tree_level(arr_invalid)))
    print()


# -----------------------------
# Comprehensive offline tests + optional visualizations
# -----------------------------
def _run_tests() -> None:
    impls = [
        ("Brute", SolutionBrute().isValidBST),
        ("DFS  ", SolutionDFSBounds().isValidBST),
        ("BFS  ", SolutionBFSBounds().isValidBST),
    ]

    TESTS: List[Tuple[List[Optional[int]], bool, str]] = [
        # From prompt
        ([2, 1, 3], True,  "prompt-valid"),
        ([1, 2, 3], False, "prompt-invalid"),

        # Edges / basics
        ([],        True,  "empty-true"),
        ([0],       True,  "single-true"),

        # Classic LC counterexample: invalid deep in right subtree
        ([5, 1, 6, None, None, 3, 7], False, "lc-invalid-right-has-small"),

        # Duplicates (strict BST should reject equals)
        ([2, 2, 2], False, "all-equal"),

        # Valid larger shape
        ([10, 5, 15, 2, 7, 12, 20, None, 3], True, "larger-valid"),

        # Invalid: value 6 is in the right subtree of 10 but < 10
        ([10, 5, 15, 2, 7, 6, 20], False, "violates-right-range"),

        # Skewed valid
        ([1, None, 2, None, 3, None, 4], True, "right-skewed-valid"),

        # Another invalid (right subtree with a too-small value)
        ([5, 4, 6, None, None, 3, 7], False, "right-has-3"),
    ]

    VIS = {
        "prompt-valid",
        "prompt-invalid",
        "lc-invalid-right-has-small",
        "larger-valid",
        "violates-right-range",
        "right-has-3",
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
            print(f"  {name} -> got={got!s:<5} expected={expected!s:<5} | {'✅' if ok else '❌'}")

        agree = len({r[1] for r in results}) == 1
        print(f"  impls-agree: {'✅' if agree else '❌'}")

    print(f"\nPassed {passed}/{total} checks.")


if __name__ == "__main__":
    _walkthrough_example()
    _run_tests()
