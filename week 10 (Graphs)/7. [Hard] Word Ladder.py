"""
Problem: Word Ladder (shortest transformation sequence length)

------------------------------------------------------------------------------
Problem
------------------------------------------------------------------------------
Given beginWord, endWord, and a wordList (all same length, lowercase, distinct):
You can transform a word to another if they differ by exactly one character.
Return the minimum number of words in a sequence from beginWord to endWord,
or 0 if no such sequence exists.

Example 1:
    beginWord = "cat", endWord = "sag",
    wordList = ["bat","bag","sag","dag","dot"]
    Output: 4   (cat -> bat -> bag -> sag)

Example 2:
    beginWord = "cat", endWord = "sag",
    wordList = ["bat","bag","sat","dag","dot"]
    Output: 0   (endWord not present, so impossible)

Constraints:
    1 <= len(beginWord) <= 10
    1 <= len(wordList) <= 100
    All words are same length and distinct.

------------------------------------------------------------------------------
Beginner Intuition
------------------------------------------------------------------------------
This is a *shortest number of steps* problem on an *implicit graph*:
• Nodes = words (plus beginWord).
• Edge between two words if they differ by exactly one letter.
Shortest path → use BFS.

Naively checking all pairs for edges is O(N^2 * L) (N words, L length).
We can index “generic patterns” to discover neighbors in O(L) per dequeue:
  For word w and index i, replace w[i] with '*' to get a bucket key.
  All words sharing a bucket differ by 1 char at position i.

------------------------------------------------------------------------------
Approach Overview (Active Solution: BFS + Generic Pattern Buckets)
------------------------------------------------------------------------------
1) If endWord not in wordList → return 0.
2) Put all words in a set; add beginWord if absent.
3) Build dict: pattern -> list of words
     pattern is made by replacing each position with '*'
     e.g., "cat" -> "*at", "c*t", "ca*"
4) BFS from beginWord, level = 1 (sequence length counts words).
   When we pop a word, for each of its L patterns, visit all neighbors
   in that bucket that are unseen; mark visited and enqueue with level+1.
   To avoid re-visiting, clear the bucket after processing it once.

------------------------------------------------------------------------------
Complexity
------------------------------------------------------------------------------
Let N = number of words (incl. beginWord) and L = word length.
Time:  O(N * L) to build buckets + O(N * L) for BFS neighbor scans.
Space: O(N * L) for buckets + O(N) for visited/queue.

------------------------------------------------------------------------------
Common Mistakes & Gotchas
------------------------------------------------------------------------------
• Forgetting to return 0 immediately if endWord not in list.
• Returning number of *edges* instead of *words* in the sequence;
  initialize BFS level at 1 for beginWord to match the problem’s definition.
• Not marking visited early (causes duplicates in the queue).
• Re-using a bucket repeatedly; clear it after first use to keep it linear.

------------------------------------------------------------------------------
"""

from typing import List, Deque, Dict, List
from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 1) Quick fail if endWord is absent.
        if endWord not in wordList:
            return 0

        L = len(beginWord)
        words = set(wordList)
        words.add(beginWord)

        # 2) Build pattern buckets.
        buckets: Dict[str, List[str]] = defaultdict(list)
        for w in words:
            for i in range(L):
                buckets[w[:i] + "*" + w[i+1:]].append(w)

        # 3) BFS.
        q: Deque[tuple[str, int]] = deque([(beginWord, 1)])  # (word, level = sequence length)
        visited = {beginWord}

        while q:
            word, level = q.popleft()
            if word == endWord:
                return level

            for i in range(L):
                pat = word[:i] + "*" + word[i+1:]
                neighbors = buckets.get(pat, [])
                # Important: clear the bucket to avoid future redundant scans.
                buckets[pat] = []
                for nei in neighbors:
                    if nei not in visited:
                        visited.add(nei)
                        q.append((nei, level + 1))

        return 0


# ------------------------------------------------------------------------------
# Optional: Bidirectional BFS (commented)
# ------------------------------------------------------------------------------
# class SolutionBiBFS:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         if endWord not in wordList:
#             return 0
#         L = len(beginWord)
#         words = set(wordList)
#         # Build buckets once
#         buckets = defaultdict(list)
#         for w in words | {beginWord}:
#             for i in range(L):
#                 buckets[w[:i] + "*" + w[i+1:]].append(w)
#         # Frontiers
#         front = {beginWord}
#         back = {endWord}
#         visited = {beginWord, endWord}
#         level = 1
#         while front and back:
#             if len(front) > len(back):
#                 front, back = back, front
#             nxt = set()
#             for w in front:
#                 if w in back:
#                     return level
#                 for i in range(L):
#                     pat = w[:i] + "*" + w[i+1:]
#                     for nei in buckets[pat]:
#                         if nei in back:
#                             return level + 1
#                         if nei not in visited:
#                             visited.add(nei)
#                             nxt.add(nei)
#             front = nxt
#             level += 1
#         return 0


# ------------------------------------------------------------------------------
# Helpers & Offline Tests
# ------------------------------------------------------------------------------
def _run_single_case(begin: str, end: str, wordList: List[str], expected: int) -> None:
    s = Solution()
    got = s.ladderLength(begin, end, wordList)
    print(f"[TEST] {begin} -> {end} via {wordList} => {got} (exp={expected})")
    assert got == expected, f"Expected {expected}, got {got}"


if __name__ == "__main__":
    # Prompt examples
    _run_single_case("cat", "sag", ["bat", "bag", "sag", "dag", "dot"], 4)
    _run_single_case("cat", "sag", ["bat", "bag", "sat", "dag", "dot"], 0)

    # Basic variations
    _run_single_case("hit", "cog", ["hot","dot","dog","lot","log","cog"], 5)  # hit hot dot dog cog
    _run_single_case("hit", "cog", ["hot","dot","dog","lot","log"], 0)        # end missing

    # Single-step path
    _run_single_case("aaa", "baa", ["baa"], 2)
