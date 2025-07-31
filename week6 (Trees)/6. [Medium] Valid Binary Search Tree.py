"""
Problem: Valid Binary Search Tree  (LeetCode 98)

Given the root of a binary tree, return True if it is a valid BST, otherwise False.

BST Rules:
1. Left subtree of every node has values < node.val
2. Right subtree of every node has values > node.val
3. Both subtrees must themselves be valid BSTs.

Examples:
Input:  root = [2,1,3]
Output: True

Input:  root = [1,2,3]
Output: False
Explanation: root = 1, but its left child = 2 (> 1), so it's invalid.

Link: https://leetcode.com/problems/validate-binary-search-tree/
"""

# Definition for a binary tree node (LeetCode provides this).
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ---------------------------------------------------------------------
# Approach 1: Recursive DFS with value bounds  [Knowledge 1.]
# - Pass down the valid (min_val, max_val) range for each node.
# - For node.val to be valid:  min_val < node.val < max_val
# - Recursively validate left with (min_val, node.val) and right with (node.val, max_val)
# Time Complexity:  O(N)
# Space Complexity: O(H)  (recursion stack; H = height of tree)
# ---------------------------------------------------------------------

from typing import Optional

class Solution:
    def isValidBST(self, root: Optional['TreeNode']) -> bool:
        def dfs(node: Optional['TreeNode'], low: float, high: float) -> bool:
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, float("-inf"), float("inf"))


# ---------------------------------------------------------------------
# Approach 2: Iterative Inorder Traversal  [Knowledge 2.]
# - Inorder of a valid BST is strictly increasing.
# - Do an inorder traversal and ensure current value > previous value.
# Time Complexity:  O(N)
# Space Complexity: O(H)  (stack; H = height of tree)
# ---------------------------------------------------------------------

class SolutionInorder:
    def isValidBST(self, root: Optional['TreeNode']) -> bool:
        stack = []
        prev_val = float("-inf")
        node = root

        while stack or node:
            # Go left
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            # Current value must be > previous inorder value
            if node.val <= prev_val:
                return False
            prev_val = node.val

            # Go right
            node = node.right

        return True
