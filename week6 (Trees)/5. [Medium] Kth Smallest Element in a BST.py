"""
Problem: Kth Smallest Element in a BST  (LeetCode 230)

Given the root of a Binary Search Tree and an integer k, return the k-th smallest value (1-indexed).

BST Rules:
- Left subtree values < node.val
- Right subtree values > node.val
- Both subtrees are BSTs

Examples:
Input:  root = [2,1,3], k = 1
Output: 1

Input:  root = [4,3,5,2,null], k = 4
Output: 5

Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""

# Definition for a binary tree node (LeetCode provides this).
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

# ---------------------------------------------------------------------
# Approach 1: Iterative Inorder Traversal (Stack)  [Knowledge 1.]
# - Inorder of BST gives values in strictly increasing order.
# - Traverse inorder and count until we hit the k-th node.
# Time Complexity:  O(H + k)  (H = height; in worst-case O(N))
# Space Complexity: O(H)      (stack)
# ---------------------------------------------------------------------

class Solution:
    def kthSmallest(self, root: Optional['TreeNode'], k: int) -> int:
        stack = []
        curr = root

        while True:
            # Go as left as possible
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val

            curr = curr.right


# ---------------------------------------------------------------------
# Approach 2: Recursive Inorder with Early Stop  [Knowledge 2.]
# - Use a helper that stops once count reaches k.
# Time Complexity:  O(H + k)
# Space Complexity: O(H)  (recursion stack)
# ---------------------------------------------------------------------

class SolutionRecursive:
    def kthSmallest(self, root: Optional['TreeNode'], k: int) -> int:
        self.k = k
        self.ans = None

        def inorder(node: Optional['TreeNode']):
            if not node or self.ans is not None:
                return
            inorder(node.left)
            if self.ans is not None:  # already found
                return
            self.k -= 1
            if self.k == 0:
                self.ans = node.val
                return
            inorder(node.right)

        inorder(root)
        return self.ans
