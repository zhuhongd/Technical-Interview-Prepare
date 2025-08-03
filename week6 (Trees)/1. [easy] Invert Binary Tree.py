"""
Invert Binary Tree — EECS4070 (Three Approaches: BFS, Recursive DFS, Iterative DFS)

Problem
-------
Given the root of a binary tree, invert the tree and return its root.
“Invert” means: swap the left and right child of **every** node.

Link
----
https://leetcode.com/problems/invert-binary-tree/

Key Examples
------------
Input : [1, 2, 3, 4, 5, 6, 7]
Output: [1, 3, 2, 7, 6, 5, 4]

Input : [3, 2, 1]
Output: [3, 1, 2]

Beginner Intuition (mirror image)
---------------------------------
Imagine holding the tree in front of a mirror: every node’s left/right children flip.
If you do this at **every** node, you get the inverted tree.

Approach Overview
-----------------
1) **Breadth-First Search (BFS)** using a queue:
   - Process nodes level by level.
   - For each node: swap its children, then push children to the queue (if not None).
   - Time: O(N), Space: O(W) ~ O(N) in worst case (W = max width).

2) **Depth-First Search (Recursive DFS)**:
   - Base case: node is None → return.
   - Swap the node’s children, recurse on both (new) children.
   - Time: O(N), Space: O(H) for recursion stack (H = height, worst-case O(N), balanced O(log N)).

3) **Depth-First Search (Iterative DFS)** using an explicit stack:
   - Emulates recursion with your own stack.
   - Pop a node, swap its children, push non-null children.
   - Time: O(N), Space: O(H) ~ O(N) worst-case.

All three do the **same work**; choose the one that fits your style or interview guidance:
- BFS is great if you’re already thinking in levels.
- Recursive DFS reads like the definition and is concise.
- Iterative DFS avoids recursion (useful if stack depth is a concern).
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
# 1) Breadth-First Search (queue)
#    Time: O(N) | Space: O(W) ≤ O(N)
# ============================================================
class SolutionBFS:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue: Deque[TreeNode] = deque([root])
        while queue:
            node = queue.popleft()
            # Swap this node's children
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root


# ============================================================
# 2) Depth-First Search (Recursive)
#    Time: O(N) | Space: O(H) recursion stack (worst O(N), balanced O(log N))
# ============================================================
class SolutionDFSRecursive:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        # Swap
        root.left, root.right = root.right, root.left
        # Recurse on (new) left and (new) right
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


# ============================================================
# 3) Depth-First Search (Iterative stack)
#    Time: O(N) | Space: O(H) ≤ O(N)
# ============================================================
class SolutionDFSIterative:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        stack: List[TreeNode] = [root]
        while stack:
            node = stack.pop()
            # Swap
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root

# -----------------------------
# Helpers: build/serialize trees (level-order with None)
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
    root_val = next(it)
    if root_val is None:
        return None

    root = TreeNode(root_val)
    q: Deque[TreeNode] = deque([root])

    # Pairwise consume (left, right)
    for v_left, v_right in zip(it, it):
        node = q.popleft()
        if v_left is not None:
            node.left = TreeNode(v_left)
            q.append(node.left)
        if v_right is not None:
            node.right = TreeNode(v_right)
            q.append(node.right)

    # If odd number of values, there’s one last left child
    remaining = list(it)
    if remaining:
        node = q.popleft()
        v_left = remaining[0]
        if v_left is not None:
            node.left = TreeNode(v_left)
            q.append(node.left)
    return root


def to_level_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    """
    Serialize a tree into level-order list with None placeholders.
    Trailing None's are trimmed for compactness.
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

    # Trim trailing None's
    while out and out[-1] is None:
        out.pop()
    return out


# -----------------------------
# Top-Down ASCII Tree Renderer (exact style you requested)
# -----------------------------
def _render_topdown_aux(node: Optional[TreeNode]) -> Tuple[List[str], int, int, int]:
    """
    Recursively build ASCII lines for a binary tree.

    Returns:
        lines: List[str]  -> the rendered lines
        width: int        -> total width of the rendering
        height: int       -> number of lines
        middle: int       -> horizontal position of the node's root label
    """
    if node is None:
        return (["·"], 1, 1, 0)  # a tiny placeholder (not usually shown)

    s = str(node.val)
    s_width = len(s)

    # Leaf node
    if node.left is None and node.right is None:
        return ([s], s_width, 1, s_width // 2)

    # Only left child
    if node.right is None:
        left_lines, left_w, left_h, left_mid = _render_topdown_aux(node.left)
        first_line = " " * (left_mid + 1) + "_" * (left_w - left_mid - 1) + s
        second_line = " " * left_mid + "/" + " " * (left_w - left_mid - 1 + s_width)
        # Pad left_lines to height
        shifted = [line + " " * s_width for line in left_lines]
        return ([first_line, second_line] + shifted,
                left_w + s_width, left_h + 2, (left_w + s_width) // 2)

    # Only right child
    if node.left is None:
        right_lines, right_w, right_h, right_mid = _render_topdown_aux(node.right)
        first_line = s + "_" * right_mid + " " * (right_w - right_mid)
        second_line = " " * (s_width + right_mid) + "\\" + " " * (right_w - right_mid - 1)
        shifted = [" " * s_width + line for line in right_lines]
        return ([first_line, second_line] + shifted,
                s_width + right_w, right_h + 2, s_width // 2)

    # Two children
    left_lines, left_w, left_h, left_mid = _render_topdown_aux(node.left)
    right_lines, right_w, right_h, right_mid = _render_topdown_aux(node.right)
    first_line = (" " * (left_mid + 1)
                  + "_" * (left_w - left_mid - 1)
                  + s
                  + "_" * right_mid
                  + " " * (right_w - right_mid))
    second_line = (" " * left_mid + "/"
                   + " " * (left_w - left_mid - 1 + s_width + right_mid)
                   + "\\"
                   + " " * (right_w - right_mid - 1))

    # Make both sides the same height
    if left_h < right_h:
        left_lines += [" " * left_w] * (right_h - left_h)
    elif right_h < left_h:
        right_lines += [" " * right_w] * (left_h - right_h)

    zipped = [l + " " * s_width + r for l, r in zip(left_lines, right_lines)]
    return ([first_line, second_line] + zipped,
            left_w + s_width + right_w,
            max(left_h, right_h) + 2,
            left_w + s_width // 2)


def render_tree_topdown(root: Optional[TreeNode], show_null: bool = False) -> str:
    """
    Render a binary tree top-down with / and \ connectors, like:

            1
           / \
          2   3
           \
            4

    If show_null=True, absent children at leaves are not printed (kept minimal),
    because the requested style omits dot placeholders.
    """
    if root is None:
        return "(empty)"
    lines, _, _, _ = _render_topdown_aux(root)

    if not show_null:
        # Replace placeholder '·' lines if any remain (should not for present nodes)
        lines = [line.replace("·", " ") for line in lines]
    return "\n".join(lines)


def visualize_before_after(arr: List[Optional[int]],
                           invert_fn,
                           title: str) -> None:
    """
    Build a tree from `arr`, show BEFORE and AFTER using the top-down renderer.
    """
    print(f"\n--- {title} ---")
    before = build_tree_level(arr)
    after = invert_fn(build_tree_level(arr))  # use a fresh build so 'before' stays intact

    print("[before]")
    print(render_tree_topdown(before))
    print("\n[after ]")
    print(render_tree_topdown(after))


# -----------------------------
# Comprehensive offline tests + optional visualizations
# -----------------------------
def _run_tests() -> None:
    impls = [
        ("BFS",     SolutionBFS().invertTree),
        ("DFS-Rec", SolutionDFSRecursive().invertTree),
        ("DFS-It",  SolutionDFSIterative().invertTree),
    ]

    TESTS: List[Tuple[List[Optional[int]], List[Optional[int]], str]] = [
        # Examples
        ([1, 2, 3, 4, 5, 6, 7], [1, 3, 2, 7, 6, 5, 4], "example-full"),
        ([3, 2, 1],             [3, 1, 2],             "example-small"),

        # Basics / edges
        ([],                    [],                    "empty"),
        ([42],                  [42],                  "single"),

        # Classic LC sample
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1], "classic-427"),

        # Left-skewed → right-skewed
        ([1, 2, None, 3, None, 4, None],
         [1, None, 2, None, 3, None, 4],              "left-skewed"),

        # Right-skewed → left-skewed
        ([1, None, 2, None, 3, None, 4],
         [1, 2, None, 3, None, 4],              "right-skewed"),

        # Mixed Nones
        ([5, 3, 8, 1, None, 7, 9], [5, 8, 3, 9, 7, None, 1], "mixed-nones"),

        # Complete-but-not-perfect
        ([2, 1, 3, None, 4, 5, None], [2, 3, 1, None, 5, 4], "complete-ish"),
    ]

    passed = 0
    total_checks = 0

    for i, (arr, expected, label) in enumerate(TESTS, 1):
        print(f"\n[{i:02d}][{label}] input={arr}")
        results = []
        for name, f in impls:
            root = build_tree_level(arr)
            inv = f(root)
            got = to_level_list(inv)
            ok = (got == expected)
            results.append((name, got, ok))
            total_checks += 1

        for name, got, ok in results:
            passed += ok
            print(f"  {name:<7} -> got={got!s:<30} expected={expected!s:<30} | {'✅' if ok else '❌'}")

        agree = len({tuple(r[1]) for r in results}) == 1
        print(f"  impls-agree: {'✅' if agree else '❌'}")

        # Visualize for selected interesting cases
        VISUALIZE_LABELS = {
            "example-small",
            "left-skewed",
            "right-skewed",
            "mixed-nones",
            "complete-ish",
        }
        if label in VISUALIZE_LABELS:
            visualize_before_after(arr, SolutionBFS().invertTree, f"viz {label} (BFS)")

    # Property: invert twice ⇒ original
    PROPS = [
        [1, 2, 3, 4, None, None, 5],
        [7, 3, 9, 1, 5, 8, 10, None, 2],
        [],
        [0],
    ]
    print("\nProperty: invert twice returns original (per implementation)")
    for name, f in impls:
        for j, arr in enumerate(PROPS, 1):
            root1 = build_tree_level(arr)
            inv1 = f(root1)
            inv2 = f(inv1)
            got = to_level_list(inv2)
            ok = (got == arr)
            total_checks += 1
            passed += ok
            print(f"  [{name:<7}][P{j}] arr={arr!s:<30} twice={got!s:<30} | {'✅' if ok else '❌'}")

    print(f"\nPassed {passed}/{total_checks} checks.")


if __name__ == "__main__":
    _run_tests()