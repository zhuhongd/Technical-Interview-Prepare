# Week 9 — Palindrome Partitioning & Backtracking

> “Backtracking is like exploring a maze—you try a path, mark your steps, and backtrack when you hit a wall.”

---

## 1. Big-Picture Concept

**Palindrome Partitioning** asks us to split a string into substrings so that *each substring is a palindrome*.  
Instead of a single answer, we must collect **all possible partitions**.

Example:  
`s = "aab"`
["a","a","b"]
["aa","b"]


This problem is a canonical use of **backtracking**, where we explore every cut position, accept only palindromic substrings, and backtrack when needed.

---

## 2. Quick-Reference Terminology

| Term             | What it means & why you care                                                                |
| ---------------- | ------------------------------------------------------------------------------------------- |
| **Palindrome**   | A string that reads the same forwards & backwards (e.g., `aba`).                            |
| **Partition**    | A sequence of substrings that together concatenate to the original string.                  |
| **Cut**          | A decision point between characters: either “cut here” (end substring) or “keep going”.     |
| **Backtracking** | DFS-style exploration: try a choice, recurse, then undo (pop) and try another path.         |
| **Search Space** | All 2^(n−1) possible cut patterns in a string of length n.                                  |

---

## 3. Backtracking Playbook

(*How to think about cutting the string*)

At index `i`:

1. Try all substrings `s[i:j]` where `j ≥ i`.
2. If `s[i:j]` is a palindrome:
   - Add it to the path.
   - Recurse from `j+1`.
   - Pop it after recursion (backtrack).
3. Stop when `i == len(s)`; record the path.

```python
def partition(s: str):
    ans, path = [], []

    def is_pal(sub: str) -> bool:
        return sub == sub[::-1]

    def dfs(i: int):
        if i == len(s):
            ans.append(path.copy())
            return
        for j in range(i, len(s)):
            if is_pal(s[i:j+1]):
                path.append(s[i:j+1])
                dfs(j+1)
                path.pop()

    dfs(0)
    return ans
    ```
Time: O(n · 2^n) — explore all cuts, check palindromes.
Space: O(n) recursion depth + output.

## 4. Example Walkthrough

`s = "aab"`

Recursion tree:

Start
├── "a" → dfs("ab")
│ ├── "a" → dfs("b")
│ │ └── "b" → ["a","a","b"]
│ └── "ab" (not palindrome)
└── "aa" → dfs("b")
└── "b" → ["aa","b"]

Final Answer:  
`[["a","a","b"], ["aa","b"]]`

---

## 5. Optimizations Cheat-Sheet

| Technique                       | Why it helps                               | Complexity Impact    |
| ------------------------------- | ------------------------------------------ | -------------------- |
| **On-the-fly palindrome check** | Simple, check each substring with 2-ptrs   | O(n) per check       |
| **DP table (isPal[i][j])**      | Precompute palindromes in O(n²)            | O(1) per check       |
| **Memoized DFS**                | Cache partitions from suffix index i       | Avoids recomputation |

```python
# Precompute palindrome table
n = len(s)
isPal = [[False]*n for _ in range(n)]
for i in range(n):
    isPal[i][i] = True
for i in range(n-1):
    isPal[i][i+1] = (s[i]==s[i+1])
for length in range(3,n+1):
    for i in range(n-length+1):
        j = i+length-1
        isPal[i][j] = (s[i]==s[j]) and isPal[i+1][j-1]
```
---

## 6. Practice Line-up & Why These Matter

| # | Problem (LeetCode)                | Theme                    | Interview Takeaway                       |
| - | --------------------------------- | ------------------------ | ---------------------------------------- |
| 1 | Palindrome Partitioning (#131)    | Backtracking basics      | Classic partitioning pattern              |
| 2 | Palindrome Partitioning II (#132) | Min cuts, DP             | Transforms enumeration into optimization  |
| 3 | Restore IP Addresses (#93)        | Backtracking + pruning   | Shows cut-based search with constraints   |
| 4 | Word Break II (#140)              | Memoized DFS             | Generalizes partitioning with dictionary  |
| 5 | Subsets (#78)                     | Backtracking vs. bitmask | Same skeleton, but no palindrome check    |

---

## 7. Learning Outcomes

By the end of this chapter you will be able to:

1. **Recognize** backtracking patterns in partitioning problems.  
2. **Implement** palindrome partitioning using recursive DFS.  
3. **Optimize** using DP tables or memoized DFS.  
4. **Analyze** complexity of cut-based search problems.  
5. **Apply** the same strategy to related problems (Word Break, Restore IP).  

---

## 8. Skip Test

If you can solve **Palindrome Partitioning II** (LC 132) in ≤ 40 min, explaining how you reduce brute force with DP, you’re ready to move on.

---

## 9. Further Reading & Visualizers

- [Tech Interview Handbook – Backtracking Patterns](https://www.techinterviewhandbook.org/grind75)  
- [MIT 6.006 – Dynamic Programming](https://ocw.mit.edu)  
- [Visualgo – String Algorithms](https://visualgo.net/en)  

---

**Next:** Week 10 — Word Break & String DP. From palindromes to dictionaries, we generalize partitioning with constraints.
