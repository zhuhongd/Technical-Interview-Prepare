"""
Problem: Invert Binary Tree  (LeetCode 226)

Given the root of a binary tree, invert the tree and return its root.
"Invert" = swap the left and right children of EVERY node.

Examples:
Input:  root = [1,2,3,4,5,6,7]
Output: [1,3,2,7,6,5,4]

Input:  root = [3,2,1]
Output: [3,1,2]

Link: https://leetcode.com/problems/invert-binary-tree/
"""

# Definition for a binary tree node (LeetCode provides this).
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ---------------------------------------------------------------------
# Approach 1: Recursive DFS  [Knowledge 1.]
# - Base case: if root is None, return None.
# - Swap root.left and root.right.
# - Recurse on both children.
# Time Complexity:  O(N)  (visit each node once)
# Space Complexity: O(H)  (recursion stack, H = height of tree)
# ---------------------------------------------------------------------

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # Swap children
        root.left, root.right = root.right, root.left

        # Recurse down
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# ---------------------------------------------------------------------
# Approach 2: Iterative BFS with a queue  [Knowledge 2.]
# - Use a deque to traverse level by level.
# - For each node, swap children, then enqueue them.
# Time Complexity:  O(N)
# Space Complexity: O(W)  (W = max width of the tree; queue size)
# ---------------------------------------------------------------------

from collections import deque

class SolutionIterative:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        q = deque([root])
        while q:
            node = q.popleft()

            # Swap
            node.left, node.right = node.right, node.left

            if node.left:  q.append(node.left)
            if node.right: q.append(node.right)

        return root
