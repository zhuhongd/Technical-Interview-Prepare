"""
Problem: Maximum Depth of Binary Tree  (LeetCode 104)

Given the root of a binary tree, return its depth.
Depth = number of nodes on the longest path from the root down to the farthest leaf.

Examples:
Input:  root = [1,2,3,null,null,4]
Output: 3

Input:  root = []
Output: 0

Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

# Definition for a binary tree node (LeetCode provides this).
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ---------------------------------------------------------------------
# Approach 1: Recursive DFS  [Knowledge 1.]
# - If root is None -> depth = 0.
# - Depth = 1 + max(depth(left), depth(right)).
# Time Complexity:  O(N)  (visit every node once)
# Space Complexity: O(H)  (recursion stack; H = tree height)
# ---------------------------------------------------------------------

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# ---------------------------------------------------------------------
# Approach 2: Iterative BFS (level-order)  [Knowledge 2.]
# - Use a queue; each loop processes one level and increments depth.
# Time Complexity:  O(N)
# Space Complexity: O(W)  (W = max width of the tree)
# ---------------------------------------------------------------------

from collections import deque

class SolutionBFS:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 0
        q = deque([root])

        while q:
            level_size = len(q)
            for _ in range(level_size):
                node = q.popleft()
                if node.left:  q.append(node.left)
                if node.right: q.append(node.right)
            depth += 1

        return depth


# ---------------------------------------------------------------------
# Approach 3: Iterative DFS with stack  [Knowledge 3.]
# - Store pairs (node, current_depth) in a stack and track the max.
# Time Complexity:  O(N)
# Space Complexity: O(H)  (stack can grow with tree height)
# ---------------------------------------------------------------------

class SolutionDFSIter:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, 1)]
        max_depth = 0

        while stack:
            node, d = stack.pop()
            max_depth = max(max_depth, d)
            if node.left:  stack.append((node.left,  d + 1))
            if node.right: stack.append((node.right, d + 1))

        return max_depth
