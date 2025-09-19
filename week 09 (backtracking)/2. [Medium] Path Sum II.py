"""
Path Sum II (LeetCode 113) — EECS4070 Teaching-First Version

Problem
-------
Given the root of a binary tree and an integer targetSum, return *all* root-to-leaf
paths where each path’s sum equals targetSum. A leaf has no children.

Link
----
https://leetcode.com/problems/path-sum-ii/

Key Examples
------------
Input : root = [5,4,8,11,None,13,4,7,2,None,None,5,1], targetSum = 22
Output: [[5,4,11,2], [5,8,4,5]]

Input : root = [1,2,3], targetSum = 5
Output: []

Input : root = [], targetSum = 0
Output: []

Beginner Intuition
------------------
This is like Path Sum I but instead of answering Yes/No, we must *collect* every
root-to-leaf path whose values add up to targetSum. The natural pattern is DFS
with a temporary "current path" list:
 - Walk down, append node value to the path, subtract from remaining target.
 - When we hit a leaf and remaining == node.val, we record a *copy* of the path.
 - Backtrack (pop) to try other branches.

Approach Overview
-----------------
1) Recursive DFS with backtracking (active):
   - Maintain 'path' list; push before exploring, pop when returning.
   - When at a leaf and remaining == node.val, append path copy to answers.

2) Iterative DFS with explicit stack (alternative):
   - Stack holds (node, running_sum, path_list_so_far).
   - On leaves with sum match, append path copy.

3) BFS (alternative):
   - Queue of (node, running_sum, path_list_so_far). Record at matching leaves.

Complexity
----------
Let N be nodes, H be height, and K be the total number of matching paths.
Time : O(N + total_length_of_output)  ~ O(N + sum(len(path_i))) since we copy paths.
Space: O(H) recursion stack + O(H) path; worst O(N) for skewed trees.

Helpers
-------
- build_tree_level(values): build from level-order list with None gaps.
- to_level_list(root)     : serialize back (trims trailing Nones).
- render_tree_topdown     : ASCII visualization.

Tests
-----
- Includes prompt-style cases, negatives, edges, and multi-path checks.
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
# ✅ Active Solution: Recursive DFS + Backtracking
#    Time: O(N + output) | Space: O(H)
# ============================================================
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans: List[List[int]] = []
        path: List[int] = []

        def dfs(node: Optional[TreeNode], remaining: int) -> None:
            if node is None:
                return
            path.append(node.val)
            remaining -= node.val

            # Leaf: record a copy if match
            if node.left is None and node.right is None:
                if remaining == 0:
                    ans.append(path.copy())
            else:
                dfs(node.left, remaining)
                dfs(node.right, remaining)

            path.pop()  # backtrack

        dfs(root, targetSum)
        return ans


# ============================================================
# Alternative 1: Iterative DFS with explicit stack
#    Time: O(N + output) | Space: O(H)
# ============================================================
class SolutionIterDFS:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        ans: List[List[int]] = []
        stack: List[Tuple[TreeNode, int, List[int]]] = [(root, root.val, [root.val])]
        while stack:
            node, acc, path = stack.pop()
            if node.left is None and node.right is None and acc == targetSum:
                ans.append(path)
            # Push right then left to process left first (if desired)
            if node.right:
                stack.append((node.right, acc + node.right.val, path + [node.right.val]))
            if node.left:
                stack.append((node.left, acc + node.left.val, path + [node.left.val]))
        return ans


# ============================================================
# Alternative 2: BFS level-order with paths
#    Time: O(N + output) | Space: O(W) where W is max width
# ============================================================
class SolutionBFS:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        ans: List[List[int]] = []
        q: Deque[Tuple[TreeNode, int, List[int]]] = deque([(root, root.val, [root.val])])
        while q:
            node, acc, path = q.popleft()
            if node.left is None and node.right is None and acc == targetSum:
                ans.append(path)
            if node.left:
                q.append((node.left, acc + node.left.val, path + [node.left.val]))
            if node.right:
                q.append((node.right, acc + node.right.val, path + [node.right.val]))
        return ans


# -----------------------------
# Helpers: build / serialize trees (level-order with None)
# -----------------------------
def build_tree_level(values: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Build a binary tree from a level-order list where None means “no node”.
    Example: [1,2,3,None,4] ->

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
    return root


def to_level_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """
    Serialize to a level-order list with None for missing children.
    Trailing None's trimmed for compactness.
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
# Top-Down ASCII Tree Renderer (same style as your other files)
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
        return ([first, second] + shifted, left_w + s_width, left_h + 2, (left_w + s_width) // 2)

    if node.left is None:
        right_lines, right_w, right_h, right_mid = _render_topdown_aux(node.right)
        first = s + "_" * right_mid + " " * (right_w - right_mid)
        second = " " * (s_width + right_mid) + "\\" + " " * (right_w - right_mid - 1)
        shifted = [" " * s_width + line for line in right_lines]
        return ([first, second] + shifted, s_width + right_w, right_h + 2, s_width // 2)

    left_lines, left_w, left_h, left_mid = _render_topdown_aux(node.left)
    right_lines, right_w, right_h, right_mid = _render_topdown_aux(node.right)
    first = (" " * (left_mid + 1)
             + "_" * (left_w - left_mid - 1)
             + s
             + "_" * right_mid
             + " " * (right_w - right_mid))
    second = (" " * left_mid + "/"
              + " " * (left_w - left_mid - 1 + s_width + right_mid)
              + "\\"
              + " " * (right_w - right_mid - 1))
    if left_h < right_h:
        left_lines += [" " * left_w] * (right_h - left_h)
    elif right_h < left_h:
        right_lines += [" " * right_w] * (left_h - right_h)
    zipped = [l + " " * s_width + r for l, r in zip(left_lines, right_lines)]
    return ([first, second] + zipped, left_w + s_width + right_w, max(left_h, right_h) + 2, left_w + s_width // 2)


def render_tree_topdown(root: Optional[TreeNode]) -> str:
    if root is None:
        return "(empty)"
    lines, *_ = _render_topdown_aux(root)
    return "\n".join(line.replace("·", " ") for line in lines)


def visualize_tree(arr: List[Optional[int]], title: str) -> None:
    print(f"\n--- {title} ---")
    root = build_tree_level(arr)
    print(render_tree_topdown(root))


# -----------------------------
# Teaching Walkthrough (tiny)
# -----------------------------
def _walkthrough_example() -> None:
    # Example from prompt variant producing two paths:
    arr = [5,4,8,11,None,13,4,7,2,None,None,5,1]
    target = 22
    root = build_tree_level(arr)
    out = Solution().pathSum(root, target)
    print("Walkthrough Example (expect two paths summing to 22):")
    print(render_tree_topdown(root))
    print(f"target={target} -> {out}")
    print()


# -----------------------------
# Comprehensive offline tests + agreement checks
# -----------------------------
def _run_tests() -> None:
    impls = [
        ("RecDFS", Solution().pathSum),
        ("ItDFS",  SolutionIterDFS().pathSum),
        ("BFS",    SolutionBFS().pathSum),
    ]

    def norm(paths: List[List[int]]) -> List[List[int]]:
        # Normalize for unordered comparison
        return sorted((list(p) for p in paths), key=lambda x: (len(x), x))

    TESTS: List[Tuple[List[Optional[int]], int, List[List[int]], str]] = [
        # Prompt-style
        ([5,4,8,11,None,13,4,7,2,None,None,5,1], 22, [[5,4,11,2],[5,8,4,5]], "prompt-two-paths"),
        ([1,2,3],                                 5, [],                              "prompt-none"),
        ([],                                      0, [],                              "empty"),

        # Single node
        ([7],                                     7, [[7]],                           "single-match"),
        ([7],                                     0, [],                              "single-no"),

        # Negatives / mix
        ([1, -2, -3, 1, 3, -2, None, -1],       -1, [[1,-2,1,-1]],                  "negatives"),

        # Multiple matches, different depths
        ([5,4,8,11,None,13,4,7,2,None,None,5,1], 26, [[5,8,13]],                     "one-at-right"),
        ([5,3,8,2,4,None,10],                    12, [[5,3,4]],                      "one-left"),
        ([5,3,8,2,4,None,10],                    18, [[5,8,5]],                      "synth-extra"),  # modify tree below
    ]

    # Adjust the synthetic case to actually enable a 5 under 8's left.
    # Replace the None at index 5 with a 5 to create 8->5 leaf path: [5,3,8,2,4,5,10]
    TESTS[-1] = ([5,3,8,2,4,5,10], 18, [[5,8,5]], "synth-extra")

    passed = 0
    total = 0

    for i, (arr, target, expected_paths, label) in enumerate(TESTS, 1):
        print(f"\n[{i:02d}][{label}] target={target} input={arr}")
        if label in {"prompt-two-paths", "negatives"}:
            visualize_tree(arr, f"viz {label}")

        results = []
        for name, f in impls:
            root = build_tree_level(arr)
            got = f(root, target)
            results.append((name, got))

        # Compare normalized results
        exp_n = norm(expected_paths)
        all_ok = True
        for name, got in results:
            ok = (norm(got) == exp_n)
            all_ok = all_ok and ok
            total += 1
            passed += ok
            print(f"  {name:<6} -> got={norm(got)} expected={exp_n} | {'✅' if ok else '❌'}")

        # Agreement among implementations
        agree = len({tuple(map(tuple, norm(g))) for _, g in results}) == 1
        print(f"  impls-agree: {'✅' if agree else '❌'}")

    print(f"\nPassed {passed}/{total} checks.")


if __name__ == "__main__":
    _walkthrough_example()
    _run_tests()
