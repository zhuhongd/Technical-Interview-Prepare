r"""
Kth Smallest Element in a BST — EECS4070 (Explained, Two Approaches) + Top-Down Visualization

Problem
-------
Given the root of a Binary Search Tree (BST) and an integer k, return the **k-th smallest**
value (1-indexed).

BST Rules:
- Left subtree values < node.val
- Right subtree values > node.val
- Both subtrees are BSTs

Link
----
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Key Examples
------------
 2 
/ \
1 3
Input : root = [2, 1, 3], k = 1
Output: 1
------------------------------
  4 
 / \
 3 5
/   
2 
Input : root = [4, 3, 5, 2, None], k = 4
Output: 5

Beginner Intuition (why inorder works)
-------------------------------------
In a BST, an **inorder traversal** (Left → Node → Right) visits values in **strictly increasing order**.
So if you walk the tree inorder and count nodes, the moment you visit the k-th node, you’ve found the
k-th smallest value.

Two clean ways to do this:
1) **Iterative Inorder** with an explicit stack (no recursion).
2) **Recursive Inorder** with an early stop once you’ve seen k nodes.

Complexity
----------
Let `h` be the tree height and `n` the number of nodes.
- **Time**: O(h + k) — you walk down to the leftmost leaf (O(h)) and then visit up to k nodes.
  In worst case (skewed tree and large k), this is O(n).
- **Space**: O(h) for the stack/recursion.

We also include a simple **ASCII top-down renderer** to visualize the test trees.

Notes
-----
• LeetCode guarantees `1 ≤ k ≤ number_of_nodes`.  
• Node values are unique in a valid BST.
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
# ✅ Active Solution: Iterative Inorder (stack)
#    Time: O(h + k) | Space: O(h)
# ------------------------------------------------------------
# Walk to the leftmost node, then pop/visit, then go right.
# The k-th popped/visited node is the k-th smallest.
# ============================================================
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack: List[TreeNode] = []
        cur = root

        while True:
            # 1) Go as far left as possible
            while cur:
                stack.append(cur)
                cur = cur.left

            # 2) Visit current node
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val

            # 3) Explore right subtree
            cur = cur.right


# ============================================================
# Alternative: Recursive Inorder with early stop
#    Time: O(h + k) | Space: O(h)
# ============================================================
class SolutionRecursive:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.ans: Optional[int] = None

        def inorder(node: Optional[TreeNode]) -> None:
            if not node or self.ans is not None:
                return
            inorder(node.left)
            if self.ans is not None:      # found already while unwinding
                return
            self.k -= 1
            if self.k == 0:
                self.ans = node.val
                return
            inorder(node.right)

        inorder(root)
        # By problem constraints, self.ans must be set.
        return self.ans  # type: ignore[return-value]


# -----------------------------
# Helpers: build / serialize BST from level-order with None
# -----------------------------
def build_tree_level(values: List[Optional[int]]) -> Optional[TreeNode]:
    r"""
    Robust builder: consume left/right with next(it, None) so odd tails and None runs
    don't misalign. Example [4,3,5,2,None] ->
          4
         / \
        3   5
       /
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
# Utility: inorder values (ground truth for tests)
# -----------------------------
def inorder_values(root: Optional[TreeNode]) -> List[int]:
    vals: List[int] = []
    stack: List[TreeNode] = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        vals.append(cur.val)
        cur = cur.right
    return vals


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


def visualize_kth(arr: List[Optional[int]], k: int, title: str) -> None:
    print(f"\n--- {title} ---")
    root = build_tree_level(arr)
    print(render_tree_topdown(root))
    vals = inorder_values(root)
    print(f"inorder = {vals}")
    print(f"k = {k}  -> expected k-th smallest = {vals[k-1] if 1 <= k <= len(vals) else None}")


# -----------------------------
# Teaching Walkthrough (tiny)
# -----------------------------
def _walkthrough_example() -> None:
    arr = [4, 3, 5, 2, None]
    k = 4
    root = build_tree_level(arr)
    ans_it = Solution().kthSmallest(root, k)
    ans_re = SolutionRecursive().kthSmallest(root, k)
    print("Walkthrough:")
    print(render_tree_topdown(root))
    print("Inorder:", inorder_values(root))
    print(f"k={k} -> iterative={ans_it}, recursive={ans_re}\n")


# -----------------------------
# Comprehensive offline tests + optional visualizations
# -----------------------------
def _run_tests() -> None:
    it = Solution().kthSmallest
    rc = SolutionRecursive().kthSmallest

    TESTS: List[Tuple[List[Optional[int]], int, int, str]] = [
        # Prompt-style
        ([2, 1, 3],                 1, 1, "prompt-1"),
        ([4, 3, 5, 2, None],        4, 5, "prompt-2"),

        # Basics
        ([3, 1, 4, None, 2],        2, 2, "classic-lc"),
        ([5, 3, 7, 2, 4, 6, 8],     3, 4, "perfect-depth3-k3"),
        ([5, 3, 7, 2, 4, 6, 8],     7, 8, "perfect-depth3-k7"),

        # Skewed shapes
        ([5, 4, None, 3, None, 2, None, 1], 2, 2, "left-skewed"),
        ([1, None, 2, None, 3, None, 4],    3, 3, "right-skewed"),

        # Mixed Nones (still a valid BST)
        ([5, 2, 8, 1, 3, 7, 9, None, None, None, 4], 5, 5, "mixed-nones-k5"),

        # Negatives / variety
        ([0, -2, 5, -3, -1, 3, 9],  4, 0, "negatives-k4"),

        # Edges for k (1 and n)
        ([2, 1, 3],                 3, 3, "k-equals-n"),
        ([2, 1, 3],                 1, 1, "k-equals-1-dup"),
    ]

    # Which to visualize
    VIS = {
        "prompt-1",
        "prompt-2",
        "perfect-depth3-k3",
        "left-skewed",
        "right-skewed",
        "mixed-nones-k5",
    }

    passed = 0
    total = 0

    for i, (arr, k, expected, label) in enumerate(TESTS, 1):
        print(f"\n[{i:02d}][{label}] k={k} expected={expected}  tree={arr}")
        if label in VIS:
            visualize_kth(arr, k, f"viz {label}")

        root = build_tree_level(arr)
        got_it = it(root, k)
        root = build_tree_level(arr)
        got_rc = rc(root, k)

        for name, got in (("Iter", got_it), ("Recur", got_rc)):
            total += 1
            ok = (got == expected)
            passed += ok
            print(f"  {name:<5} -> got={got:<3} expected={expected:<3} | {'✅' if ok else '❌'}")

        agree = (got_it == got_rc)
        print(f"  impls-agree: {'✅' if agree else '❌'}")

    print(f"\nPassed {passed}/{total} checks.")


if __name__ == "__main__":
    _walkthrough_example()
    _run_tests()
