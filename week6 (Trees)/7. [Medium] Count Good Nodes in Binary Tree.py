"""
Problem: Count Good Nodes in Binary Tree  (LeetCode 1448)

A node `x` is *good* if on the path from the **root** to `x` no node has a
value greater than `x.val`.

Return the total number of good nodes.

Examples
--------
Input : root = [2,1,1,3,null,1,5]
Output: 3        # 2 (root), 3, 5 are good

Input : root = [1,2,-1,3,4]
Output: 4        # 1, 2, 3, 4

Constraints
-----------
1 ≤ n ≤ 100
-100 ≤ Node.val ≤ 100

link: https://neetcode.io/problems/count-good-nodes-in-binary-tree?list=neetcode150
"""

from __future__ import annotations
from typing import Optional, List
from collections import deque


class TreeNode:
    """Binary-tree node."""
    def __init__(self, val: int):
        self.val: int = val
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None

    # Convenience for debugging / tests
    def __repr__(self) -> str:  # pragma: no cover
        return f"TreeNode({self.val})"


class Solution:
    # ──────────────────────────────────────────────────────────────────────────
    # Recursive DFS (pre-order: Root → Left → Right)
    # ──────────────────────────────────────────────────────────────────────────
    def goodNodes(self, root: Optional[TreeNode]) -> int:
        """
        Recursively carry along the **maximum value so far** on the path.
        A node is good when its value ≥ that running max.

        Time  : O(n) – each node visited once
        Space : O(h) – recursion stack; h ≈ log n (balanced) .. n (skewed)
        """

        def dfs(node: Optional[TreeNode], path_max: int) -> int:
            if not node:                        # base-case
                return 0
            good = int(node.val >= path_max)    # 1 if good else 0
            new_max = max(path_max, node.val)   # update running maximum
            # traverse children
            good += dfs(node.left, new_max)
            good += dfs(node.right, new_max)
            return good

        return dfs(root, float("-inf"))

    # ──────────────────────────────────────────────────────────────────────────
    # Iterative DFS (stack) – for interviewers who forbid recursion
    # ──────────────────────────────────────────────────────────────────────────
    def goodNodes_iterative(self, root: Optional[TreeNode]) -> int:
        """
        Explicit stack: (node, max_so_far) tuples.

        Time  : O(n)
        Space : O(h) – same as recursion in typical cases
        """
        if not root:
            return 0

        stack = [(root, root.val)]
        good = 0

        while stack:
            node, max_so_far = stack.pop()
            if node.val >= max_so_far:
                good += 1
            new_max = max(max_so_far, node.val)
            if node.left:
                stack.append((node.left, new_max))
            if node.right:
                stack.append((node.right, new_max))

        return good


# ─────────────────────────────────────────────────────────────────────────────
# Helpers & Self-test
# ─────────────────────────────────────────────────────────────────────────────
def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Build a binary tree from a level-order list where `None` represents
    missing children (LeetCode serialization style).
    """
    if not values:
        return None

    root = TreeNode(values[0])
    queue: deque[TreeNode] = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


if __name__ == "__main__":
    s = Solution()

    # Example 1
    root1 = build_tree([2, 1, 1, 3, None, 1, 5])
    assert s.goodNodes(root1) == 3
    assert s.goodNodes_iterative(root1) == 3

    # Example 2
    root2 = build_tree([1, 2, -1, 3, 4])
    assert s.goodNodes(root2) == 4
    assert s.goodNodes_iterative(root2) == 4

    # Edge case: single node
    assert s.goodNodes(build_tree([42])) == 1

    print("✅ All sample tests passed!")
