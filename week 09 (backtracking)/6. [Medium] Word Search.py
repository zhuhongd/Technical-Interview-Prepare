"""
Word Search (LeetCode 79) — EECS4070 Version

Problem
-------
Given a 2D board and a string word, return True iff word exists in the grid by
moving horizontally/vertically to neighbors without reusing a cell in the same path.

Link
----
https://leetcode.com/problems/word-search/

Key Examples
------------
board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
]
"CAT" -> True     (e.g., C(0,2) -> A(1,2) -> T(1,3))
"BAT" -> False

Beginner Intuition
------------------
Try every starting cell that matches word[0]. From there, DFS with backtracking:
mark the cell as used, try 4 neighbors for the next character, then unmark.

Approach Overview
-----------------
Backtracking (in-place mark/restore):
- If board[r][c] != word[k] -> fail
- If k == len(word)-1 and matches -> success
- Temporarily mark board[r][c] = "#" to avoid reuse; restore on return

Complexity
----------
Let R*C = N and L = len(word).
Time  ~ O(N * 3^(L-1)) worst-case; Space ~ O(L) recursion stack.
"""

from typing import List

# ============================================================
# ✅ Active Solution: Backtracking (in-place)
# ============================================================
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board or not board[0]:
            return False
        R, C = len(board), len(board[0])

        def dfs(r: int, c: int, k: int) -> bool:
            if k == len(word):                    # matched all chars
                return True
            if r < 0 or r >= R or c < 0 or c >= C:
                return False
            if board[r][c] != word[k]:
                return False

            ch = board[r][c]
            board[r][c] = "#"                     # mark used
            found = (dfs(r-1, c, k+1) or
                     dfs(r+1, c, k+1) or
                     dfs(r, c-1, k+1) or
                     dfs(r, c+1, k+1))
            board[r][c] = ch                      # restore
            return found

        for i in range(R):
            for j in range(C):
                if dfs(i, j, 0):
                    return True
        return False


# -----------------------------
# Tiny helpers + tests
# -----------------------------
def ascii_board(board: List[List[str]]) -> str:
    return "\n".join(" ".join(row) for row in board)

def _run_tests() -> None:
    board = [
      ["A","B","C","D"],
      ["S","A","A","T"],
      ["A","C","A","E"]
    ]
    tests = [
        (board, "CAT", True,  "example-1"),
        (board, "BAT", False, "example-2"),
        ([["A"]], "A", True,  "single-yes"),
        ([["A"]], "B", False, "single-no"),
    ]
    sol = Solution()
    passed = 0
    for b, w, exp, name in tests:
        import copy
        got = sol.exist(copy.deepcopy(b), w)
        ok = (got == exp)
        passed += ok
        print(f"[{name}] word={w!r} -> {got} | expected={exp} | {'✅' if ok else '❌'}")
    print(f"Passed {passed}/{len(tests)} tests.")

if __name__ == "__main__":
    _run_tests()
