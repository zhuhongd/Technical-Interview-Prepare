r"""
Same Binary Tree — EECS4070 (Explained, Multiple Approaches) + Top-Down Visualization

Problem
-------
Given the roots of two binary trees p and q, return **True** if the trees are *equivalent*:
they have the **same shape** and **matching values** at every corresponding node. Otherwise return False.

Link
----
https://leetcode.com/problems/same-tree/

Key Examples
------------
Input : p = [1, 2, 3], q = [1, 2, 3]
Output: True

Input : p = [4, 7], q = [4, None, 7]
Output: False   # shapes differ → not the same

Input : p = [1, 2, 3], q = [1, 3, 2]
Output: False   # values differ → not the same

What the grader expects
-----------------------
• Compare **both** structure and values.  
• The order of comparison must pair **left with left** and **right with right** at each position.  
• Handle all corner cases: both empty, one empty, single node, deeper mismatches.

Beginner Intuition
------------------
Think of walking both trees **in lock-step**:
1) If both positions are empty → they match here.
2) If exactly one is empty → shapes differ → not equal.
3) If both exist, compare values; if unequal → not equal.
4) Do the same for left children and right children.

If *every* paired position passes these checks, the trees are the same.

Tiny Visuals
------------
Same shape + values:

    p:        1          q:        1
             / \                  / \
            2   3                2   3

Different shape:

    p:        4          q:        4
             / \                    \
            7   ·                    7

Different values:

    p:        1          q:        1
             / \                  / \
            2   3                3   2

Thinking Process (step-by-step)
-------------------------------
A single rule covers everything at each step (pair u from p, v from q):
- Both None → OK at this spot.
- One None → mismatch → False.
- Values differ → False.
- Else → push/recurse on (u.left, v.left) and (u.right, v.right).

Approaches (exactly what you asked for)
---------------------------------------
1) Depth-First Search (Recursive)
   - Mirrors the definition; concise and clear.
   - Time O(N) (visit each node once), Space O(H) recursion stack (worst O(N), balanced O(log N)).

2) Iterative DFS (stack of pairs)
   - Avoid recursion; same checks via explicit stack.
   - Time O(N), Space O(N).

3) Breadth-First Search (queue of pairs)
   - Level-order lock-step comparison.
   - Time O(N), Space O(N).

Why this works
--------------
We enforce **positional equivalence**: each position is either empty in both trees or has
two nodes with equal values. By pairing left-with-left and right-with-right *recursively/iteratively*,
we guarantee identical structure and values everywhere.

Common Pitfalls
---------------
• Comparing traversals *without* structure (e.g., only preorder lists) can say two different
  shapes are “equal” — don’t do that here.  
• Forgetting the “one None, one not None” check early.  
• Swapping left and right by accident when pushing/recursing.

Complexity Summary
------------------
Let N be the number of nodes (assuming both trees have at most N nodes).
• Time  : O(N) — each pair of positions is checked once.  
• Space : O(H) for recursion (H = height) or O(N) for stack/queue in worst case.

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
# 1) Depth First Search (Recursive) — your solution
#    Time: O(N) | Space: O(H)
# ============================================================
class SolutionDFSRec:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False


# ============================================================
# 2) Iterative DFS (stack of pairs) — your solution
#    Time: O(N) | Space: O(N)
# ============================================================
class SolutionDFSIter:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack: List[Tuple[Optional[TreeNode], Optional[TreeNode]]] = [(p, q)]
        while stack:
            node1, node2 = stack.pop()

            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False

            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))
        return True


# ============================================================
# 3) Breadth First Search (queue of pairs) — your solution
#    Time: O(N) | Space: O(N)
# ============================================================
class SolutionBFS:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1: Deque[Optional[TreeNode]] = deque([p])
        q2: Deque[Optional[TreeNode]] = deque([q])

        while q1 and q2:
            # pop one pair at a time (lock-step)
            nodeP = q1.popleft()
            nodeQ = q2.popleft()

            if nodeP is None and nodeQ is None:
                # positions match as empty
                continue
            if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                return False

            q1.append(nodeP.left)
            q1.append(nodeP.right)
            q2.append(nodeQ.left)
            q2.append(nodeQ.right)

        # both queues must be empty to be identical
        return not q1 and not q2


# ============================================================
# Active alias (optional): pick the recursive version by default
# ============================================================
class Solution(SolutionDFSRec):
    """LeetCode-style single-class entry; uses the recursive DFS by default."""
    pass


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


def visualize_two_trees(p_arr: List[Optional[int]],
                        q_arr: List[Optional[int]],
                        title: str) -> None:
    print(f"\n--- {title} ---")
    p_root = build_tree_level(p_arr)
    q_root = build_tree_level(q_arr)
    print("[p]")
    print(render_tree_topdown(p_root))
    print("\n[q]")
    print(render_tree_topdown(q_root))


# -----------------------------
# Comprehensive offline tests + optional visualizations
# -----------------------------
def _run_tests() -> None:
    impls = [
        ("DFS-Rec", SolutionDFSRec().isSameTree),
        ("DFS-It ", SolutionDFSIter().isSameTree),
        ("BFS    ", SolutionBFS().isSameTree),
    ]

    TESTS: List[Tuple[List[Optional[int]], List[Optional[int]], bool, str]] = [
        # Examples
        ([1, 2, 3],           [1, 2, 3],           True,  "example-1-equal"),
        ([4, 7],              [4, None, 7],        False, "example-2-shape"),
        ([1, 2, 3],           [1, 3, 2],           False, "example-3-values"),

        # Basics / edges
        ([],                  [],                  True,  "both-empty"),
        ([42],                [],                  False, "one-empty"),
        ([0],                 [0],                 True,  "single-equal"),
        ([0],                 [1],                 False, "single-diff"),

        # Shape differences deeper down
        ([1, 2, 3, None, 5],  [1, 2, 3, 4, 5],     False, "subtree-shape-diff"),
        ([1, 2, None, 3],     [1, 2, None, None],  False, "left-chain-vs-missing"),

        # Same shape, different values at a leaf
        ([1, 2, 3, 4, None],  [1, 2, 3, 9, None],  False, "leaf-value-diff"),

        # Larger identical
        ([1,2,3,4,5,6,7],     [1,2,3,4,5,6,7],     True,  "perfect-depth3-equal"),

        # Same values but different structure
        ([2,2,2,2,None],      [2,2,2,None,2],      False, "same-values-diff-structure"),
    ]

    VIS = {
        "example-1-equal",
        "example-2-shape",
        "example-3-values",
        "subtree-shape-diff",
        "same-values-diff-structure",
    }

    passed = 0
    total = 0

    for i, (p_arr, q_arr, expected, label) in enumerate(TESTS, 1):
        print(f"\n[{i:02d}][{label}]")
        if label in VIS:
            visualize_two_trees(p_arr, q_arr, f"viz {label}")

        results = []
        for name, f in impls:
            got = f(build_tree_level(p_arr), build_tree_level(q_arr))
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
    _run_tests()
