"""
Problem: Diameter of Binary Tree  (LeetCode 543)

The diameter of a binary tree is the length (#edges) of the longest path between ANY two nodes.
The path does NOT have to pass through the root.

Examples:
Input:  root = [1,null,2,3,4,5]
Output: 3
Explanation: Paths like [1,2,3,5] or [5,3,2,4] have 3 edges.

Input:  root = [1,2,3]
Output: 2

Link: https://leetcode.com/problems/diameter-of-binary-tree/
"""

# Definition for a binary tree node (LeetCode provides this).
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ---------------------------------------------------------------------
# Approach 1: Recursive DFS (post-order)  [Knowledge 1.]
# Idea:
#   - For each node, compute its height (max depth from this node down).
#   - Candidate diameter through this node = left_height + right_height  (#edges!)
#   - Track a global max over all nodes.
#
# Time Complexity:  O(N)  (visit each node once)
# Space Complexity: O(H)  (recursion stack, H = tree height)
# ---------------------------------------------------------------------

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0  # global max diameter in edges

        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            lh = height(node.left)
            rh = height(node.right)
            # Update diameter: path length through this node = lh + rh
            self.best = max(self.best, lh + rh)
            # Return height of this node
            return 1 + max(lh, rh)

        height(root)
        return self.best


# ---------------------------------------------------------------------
# Approach 2: Iterative DFS using a stack  [Knowledge 2.]
# - Simulate post-order traversal with a stack.
# - Store (node, visited_flag). When popping second time, compute heights.
# - Keep a dict mapping node -> height.
#
# Time Complexity:  O(N)
# Space Complexity: O(N)  (stack + dict to store heights)
# ---------------------------------------------------------------------

class SolutionIterative:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, False)]
        heights = {}
        best = 0

        while stack:
            node, visited = stack.pop()
            if not node:
                continue

            if not visited:
                # Post-order: push node again as visited, then children
                stack.append((node, True))
                stack.append((node.left, False))
                stack.append((node.right, False))
            else:
                lh = heights.get(node.left, 0)
                rh = heights.get(node.right, 0)
                best = max(best, lh + rh)
                heights[node] = 1 + max(lh, rh)

        return best