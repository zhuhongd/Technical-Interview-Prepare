"""
Path Sum — EECS4070 (Explained, Multiple Approaches) + Top-Down Visualization

Problem
-------
Given the root of a binary tree and an integer targetSum, return True if the tree has a
root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

Link
----
https://leetcode.com/problems/path-sum/

Key Examples
------------
Input : root = [5,4,8,11,None,13,4,7,2,None,None,None,1], targetSum = 22
Output: True
(One valid path is 5 → 4 → 11 → 2 = 22)

Input : root = [1,2,3], targetSum = 5
Output: False
(No root→leaf path sums to 5)

Beginner Intuition
------------------
We want to check if **any root-to-leaf path adds up exactly to targetSum**.
Think recursively:
- Subtract the current node’s value from the target.
- If we reach a leaf, check if the remaining target equals that leaf’s value.
- Otherwise, recurse on left/right subtrees.

Complexity
----------
Time : O(N)  – visit each node once
Space: O(H)  – recursion depth (worst-case O(N) if tree is skewed)
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
# ✅ Active Solution: Recursive DFS
#    Time: O(N) | Space: O(H)
# ============================================================
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        # Leaf check
        if not root.left and not root.right:
            return root.val == targetSum
        rem = targetSum - root.val
        return (self.hasPathSum(root.left, rem) or
                self.hasPathSum(root.right, rem))


# ============================================================
# Alternative: Iterative DFS with explicit stack
#    Time: O(N) | Space: O(H)
# ============================================================
class SolutionIter:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack: List[Tuple[TreeNode, int]] = [(root, targetSum - root.val)]
        while stack:
            node, rem = stack.pop()
            if not node.left and not node.right and rem == 0:
                return True
            if node.left:
                stack.append((node.left, rem - node.left.val))
            if node.right:
                stack.append((node.right, rem - node.right.val))
        return False


# Don't worry anything below here
# -----------------------------
# Helpers: build / serialize trees (level-order with None)
# -----------------------------
def build_tree_level(values: List[Optional[int]]) -> Optional[TreeNode]:
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
        try:
            lv = next(it)
            if lv is not None:
                node.left = TreeNode(lv)
                q.append(node.left)
            rv = next(it)
            if rv is not None:
                node.right = TreeNode(rv)
                q.append(node.right)
        except StopIteration:
            break
    return root


# -----------------------------
# Top-Down ASCII Tree Renderer (for visualization)
# -----------------------------
def _render_topdown_aux(node: Optional[TreeNode]) -> Tuple[List[str], int, int, int]:
    if node is None:
        return (["·"], 1, 1, 0)
    s = str(node.val)
    s_width = len(s)
    if node.left is None and node.right is None:
        return ([s], s_width, 1, s_width // 2)

    if node.right is None:
        left_lines, left_w, left_h, left_mid = _render_topdown_aux(node.left)
        first = " " * (left_mid + 1) + "_" * (left_w - left_mid - 1) + s
        second = " " * left_mid + "/" + " " * (left_w - left_mid - 1 + s_width)
        shifted = [line + " " * s_width for line in left_lines]
        return [first, second] + shifted, left_w + s_width, left_h + 2, (left_w + s_width) // 2

    if node.left is None:
        right_lines, right_w, right_h, right_mid = _render_topdown_aux(node.right)
        first = s + "_" * right_mid + " " * (right_w - right_mid)
        second = " " * (s_width + right_mid) + "\\" + " " * (right_w - right_mid - 1)
        shifted = [" " * s_width + line for line in right_lines]
        return [first, second] + shifted, s_width + right_w, right_h + 2, s_width // 2

    left_lines, left_w, left_h, left_mid = _render_topdown_aux(node.left)
    right_lines, right_w, right_h, right_mid = _render_topdown_aux(node.right)
    first = (" " * (left_mid + 1) + "_" * (left_w - left_mid - 1) + s +
             "_" * right_mid + " " * (right_w - right_mid))
    second = (" " * left_mid + "/" + " " * (left_w - left_mid - 1 + s_width + right_mid) +
              "\\" + " " * (right_w - right_mid - 1))
    if left_h < right_h:
        left_lines += [" " * left_w] * (right_h - left_h)
    elif right_h < left_h:
        right_lines += [" " * right_w] * (left_h - right_h)
    lines = [l + " " * s_width + r for l, r in zip(left_lines, right_lines)]
    return [first, second] + lines, left_w + s_width + right_w, max(left_h, right_h) + 2, left_w + s_width // 2


def render_tree_topdown(root: Optional[TreeNode]) -> str:
    if root is None:
        return "(empty)"
    lines, _, _, _ = _render_topdown_aux(root)
    return "\n".join(line.replace("·", " ") for line in lines)


# -----------------------------
# Teaching Walkthrough
# -----------------------------
def _walkthrough_example() -> None:
    arr = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
    root = build_tree_level(arr)
    target = 22
    print("--- Walkthrough Example ---")
    print(render_tree_topdown(root))
    ans = Solution().hasPathSum(root, target)
    print("Target =", target, "Result =", ans)
    print()


# -----------------------------
# Comprehensive offline tests
# -----------------------------
def _run_tests() -> None:
    impls = [
        ("RecDFS", Solution().hasPathSum),
        ("Iter",   SolutionIter().hasPathSum),
    ]
    TESTS = [
        # From prompt
        ([5,4,8,11,None,13,4,7,2,None,None,None,1], 22, True, "prompt-1"),
        # Basic no-path
        ([1,2,3], 5, False, "no-path"),
        # Empty tree
        ([], 0, False, "empty"),
        # Single node equals target
        ([7], 7, True, "single-hit"),
        # Single node not equal
        ([7], 8, False, "single-miss"),
    ]
    for arr, target, exp, label in TESTS:
        print(f"\n[{label}] arr={arr}, target={target}")
        root = build_tree_level(arr)
        print(render_tree_topdown(root))
        for name, f in impls:
            got = f(root, target)
            print(f"  {name:<6} -> got={got} expected={exp} | {'✅' if got==exp else '❌'}")


if __name__ == "__main__":
    _walkthrough_example()
    _run_tests()
