r"""
Subtree of Another Tree — EECS4070 (Explained, Multiple Approaches) + Top-Down Visualization

Problem
-------
Given the roots of two binary trees `root` and `subRoot`, return True if there is a subtree of `root`
with the same **structure and values** as `subRoot`. Otherwise, return False.

A subtree of `root` is a node in `root` together with **all of its descendants**. The tree `root`
is also considered a subtree of itself.

Link
----
https://leetcode.com/problems/subtree-of-another-tree/

Key Examples
------------
Input : root = [1, 2, 3, 4, 5], subRoot = [2, 4, 5]
Output: True

Input : root = [1, 2, 3, 4, 5, None, None, 6], subRoot = [2, 4, 5]
Output: False

Beginner Intuition
------------------
Two ways to think about it:

1) **Scan + Compare (DFS):**  
   At each node of `root`, ask: "Does the subtree starting here match `subRoot` exactly?"
   - Base cases: if `subRoot` is None → True (empty tree is a subtree of anything).
                 if `root` is None (but `subRoot` is not) → False.
   - Otherwise, check `sameTree(root, subRoot)`. If not equal here, **recurse down** to `root.left` and `root.right`.

2) **Serialize + Pattern Matching:**  
   If you serialize trees (with null markers and value delimiters) to strings, then
   "is `subRoot` a subtree of `root`?" becomes "is `serialize(subRoot)` a substring of `serialize(root)`?"  
   Use a linear-time string matching like **Z-algorithm** to search efficiently.

Why delimiters and null markers matter
--------------------------------------
We must avoid false positives such as confusing `12` with `1|2`, or shape ambiguities.
By using a value prefix (e.g., '$') and explicit null marker (e.g., '#'), **preorder** serialization
uniquely captures both **structure** and **values**.

Approaches
----------
1) Depth First Search (DFS) — *Scan every node in `root` and compare subtrees*  
   • Time: O(m * n)  (in the worst case, `sameTree` is O(m) and you try it at many `root` nodes)  
   • Space: O(m + n) recursion stacks in the worst case

2) Serialization + Z-function (linear pattern search)  
   • Time: O(m + n)  to serialize and run Z across combined string  
   • Space: O(m + n)  for the strings and Z array

Common Pitfalls
---------------
• Forgetting to treat `subRoot == None` as True.  
• Comparing values without comparing structure (must match both left and right recursively).  
• Serialization without null markers or delimiters can yield false matches.

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
# 1) Depth First Search (DFS) — Scan + Compare (your solution)
#    Time: O(m * n) | Space: O(m + n) worst-case (recursion)
# ============================================================
class SolutionDFS:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # empty subRoot is always a subtree (convention used in LC)
        if not subRoot:
            return True
        # non-empty subRoot cannot be subtree of empty root
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        # otherwise, try left or right subtree
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
        if not a and not b:
            return True
        if a and b and a.val == b.val:
            return self.sameTree(a.left, b.left) and self.sameTree(a.right, b.right)
        return False


# ============================================================
# 2) Serialization + Z-function (your solution adapted)
#    Time: O(m + n) | Space: O(m + n)
# ------------------------------------------------------------
# Preorder serialize with '$' prefix for values and '#' for Nones.
# Then check if serial(subRoot) is a substring of serial(root) using Z algo.
# ============================================================
class SolutionSerializeZ:
    def serialize(self, node: Optional[TreeNode]) -> str:
        # '$value' marks a node value; '# ' marks null; no spaces to keep compact.
        if node is None:
            return "$#"
        # preorder: node, left, right
        return f"${node.val}" + self.serialize(node.left) + self.serialize(node.right)

    def z_function(self, s: str) -> List[int]:
        n = len(s)
        z = [0] * n
        L = R = 0
        for i in range(1, n):
            if i <= R:
                z[i] = min(R - i + 1, z[i - L])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > R:
                L, R = i, i + z[i] - 1
        return z

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # By convention, empty subRoot is a subtree of any root
        if subRoot is None:
            return True
        if root is None:
            return False

        s_root = self.serialize(root)
        s_sub = self.serialize(subRoot)
        # Use a separator char not present in the serialization alphabet {'$', '#', digits, '-'}
        combined = s_sub + "|" + s_root
        z = self.z_function(combined)
        sub_len = len(s_sub)

        # If at any position we match the entire pattern length, it's a hit
        for i in range(sub_len + 1, len(combined)):
            if z[i] == sub_len:
                return True
        return False


# ============================================================
# (Optional) Choose DFS as the active LeetCode-style Solution
# ============================================================
class Solution(SolutionDFS):
    """Default to DFS-scan solution for LeetCode submission."""
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


def visualize_two(root_arr: List[Optional[int]], sub_arr: List[Optional[int]], title: str) -> None:
    print(f"\n--- {title} ---")
    root = build_tree_level(root_arr)
    sub = build_tree_level(sub_arr)
    print("[root]")
    print(render_tree_topdown(root))
    print("\n[subRoot]")
    print(render_tree_topdown(sub))


# -----------------------------
# Comprehensive offline tests + optional visualizations
# -----------------------------
def _run_tests() -> None:
    impls = [
        ("DFS", SolutionDFS().isSubtree),
        ("SerZ", SolutionSerializeZ().isSubtree),
    ]

    TESTS: List[Tuple[List[Optional[int]], List[Optional[int]], bool, str]] = [
        # Given examples
        ([1, 2, 3, 4, 5],             [2, 4, 5],              True,  "example-true"),
        ([1, 2, 3, 4, 5, None, None, 6], [2, 4, 5],            False, "example-false"),

        # Basics / edges
        ([],                           [],                     True,  "both-empty"),
        ([1],                          [],                     True,  "empty-subtree"),
        ([],                           [1],                    False, "empty-root-nonempty-sub"),
        ([1],                          [1],                    True,  "single-equal"),
        ([1],                          [2],                    False, "single-diff"),

        # Root equals subRoot (full match)
        ([3, 4, 5, 1, 2],              [3, 4, 5, 1, 2],        True,  "identical-trees"),

        # Classic tricky: repeated values — must check structure too
        ([3, 4, 5, 1, 2, None, None, None, None, 0],
         [4, 1, 2],                                           False, "repeated-values-shape-mismatch"),

        # Multiple potential match points — only one correct structure
        ([1, 1, 1, 1, None, 1, None, 2], [1, 1, None, 2],     True,  "deep-left-match"),

        # Subtree on the right side
        ([5, 3, 8, 1, 4, 7, 9],         [8, 7, 9],            True,  "right-subtree"),

        # Negative values + mixed shapes
        ([0, -1, 2, None, -2, 1],       [-1, None, -2],       True,  "negative-values-true"),

        # No match anywhere
        ([2, 1, 3],                     [4],                  False, "no-match-anywhere"),
    ]

    VIS = {
        "example-true",
        "example-false",
        "repeated-values-shape-mismatch",
        "right-subtree",
        "deep-left-match",
    }

    passed = 0
    total = 0

    for i, (root_arr, sub_arr, expected, label) in enumerate(TESTS, 1):
        print(f"\n[{i:02d}][{label}] root={root_arr}  sub={sub_arr}")
        if label in VIS:
            visualize_two(root_arr, sub_arr, f"viz {label}")

        results = []
        for name, f in impls:
            got = f(build_tree_level(root_arr), build_tree_level(sub_arr))
            ok = (got == expected)
            results.append((name, got, ok))

        for name, got, ok in results:
            total += 1
            passed += ok
            print(f"  {name:<4} -> got={str(got):<5} expected={str(expected):<5} | {'✅' if ok else '❌'}")

        agree = len({r[1] for r in results}) == 1
        print(f"  impls-agree: {'✅' if agree else '❌'}")

    print(f"\nPassed {passed}/{total} checks.")


if __name__ == "__main__":
    _run_tests()
