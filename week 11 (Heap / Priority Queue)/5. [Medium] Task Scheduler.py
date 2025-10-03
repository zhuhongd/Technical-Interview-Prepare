r"""
Task Scheduler — EECS4070 (Explained, Multiple Approaches)

Problem
-------
You are given an array of CPU tasks `tasks` (each is 'A'..'Z') and a non-negative integer `n`.
Each CPU cycle completes a single task (or is idle). **Identical tasks** must be separated by
at least `n` cycles (cooldown). Return the **minimum number of CPU cycles** needed to finish all tasks.

Link
----
https://leetcode.com/problems/task-scheduler/

Key Examples
------------
Example 1
Input : tasks = ["X","X","Y","Y"], n = 2
Output: 5
One optimal schedule: X → Y → idle → X → Y

Example 2
Input : tasks = ["A","A","A","B","C"], n = 3
Output: 9
One optimal schedule: A → B → C → idle → A → idle → idle → idle → A

Constraints
-----------
• 1 <= len(tasks) <= 1000
• 0 <= n <= 100

Beginner Intuition
------------------
If a task (say 'A') appears very often, its copies must be *spaced out* by at least `n` slots.
The most frequent tasks control the skeleton of the schedule. Fill remaining slots with other
tasks or idles. The answer is the larger of:
1) The raw number of tasks (no need to idle if variety is enough), and
2) The length of the *frame* forced by the most frequent tasks.

Two Ways to Solve
-----------------
1) **Math Formula (Greedy Count) — O(26)**
   Let `f_max` be the maximum frequency among all tasks, and `m` be how many tasks have frequency `f_max`.
   Then:
       frames = (f_max - 1) * (n + 1) + m
   Answer = max(len(tasks), frames)

   Why it works:
   - You lay out `f_max - 1` full groups; each group is size `n + 1` (one slot for a most-frequent task + `n` cooldown).
   - Finally, place the last occurrences of all `m` most-frequent tasks.
   - If there are enough other tasks to fill cooldown spaces, you won't need idles and the total time is just `len(tasks)`.

2) **Simulation (Max-Heap + Cooldown Queue) — O(T log 26)**
   Use a max-heap of remaining counts; each time unit you pick the most frequent available task,
   and put it into a cooldown queue for `n` steps before it can be used again. Counts are small (≤1000),
   alphabet is small (≤26), so this is fast in practice. Good for understanding dynamics.

Common Pitfalls
---------------
• Miscounting `m` (the number of tasks with frequency `f_max`).  
• Forgetting that if there are enough different tasks, you may **never idle** (answer = `len(tasks)`).  
• Off-by-one in `(f_max - 1) * (n + 1) + m`.

"""

from __future__ import annotations
from collections import Counter, deque
import heapq
from typing import List, Tuple


# ============================================================
# 1) Math Formula — O(26) time, O(1) space
#    Answer = max( len(tasks), (f_max - 1) * (n + 1) + m )
# ------------------------------------------------------------
class SolutionMath:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        freq = Counter(tasks)
        f_max = max(freq.values())
        m = sum(1 for c in freq.values() if c == f_max)

        frames = (f_max - 1) * (n + 1) + m
        return max(len(tasks), frames)


# ============================================================
# 2) Simulation — Max-Heap + Cooldown Queue
#    Time: O(T log 26) ~ O(T), Space: O(26)
# ------------------------------------------------------------
class SolutionSim:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        # Max-heap by counts → store negatives because Python heap is min-heap.
        freq = Counter(tasks)
        heap = [-cnt for cnt in freq.values()]
        heapq.heapify(heap)

        time = 0
        # cooldown queue elements: (ready_time, neg_count_remaining)
        cool: deque[Tuple[int, int]] = deque()

        while heap or cool:
            time += 1

            # If some task's cooldown is over, push it back to the heap
            if cool and cool[0][0] == time:
                _, negcnt = cool.popleft()
                heapq.heappush(heap, negcnt)

            if heap:
                negcnt = heapq.heappop(heap)      # run a task with largest remaining count
                negcnt += 1                       # we used one instance (since negcnt is negative)
                if negcnt != 0:
                    # Put back after cooldown
                    cool.append((time + n + 1, negcnt))
            # else: idle (no available task this cycle)

        return time


# ============================================================
# 3) Chunked Simulation (Optional) — Greedy Blocks of (n+1)
#    Often seen variant; included for completeness
# ------------------------------------------------------------
class SolutionChunked:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)

        freq = Counter(tasks)
        heap = [-cnt for cnt in freq.values()]
        heapq.heapify(heap)

        time = 0
        while heap:
            used_this_round = []
            # Try to schedule up to (n+1) tasks in this block
            for _ in range(n + 1):
                if heap:
                    negcnt = heapq.heappop(heap)
                    negcnt += 1              # used one
                    if negcnt != 0:
                        used_this_round.append(negcnt)
                time += 1
                if not heap and not used_this_round:
                    break  # no more work; trim trailing idles

            # Push back remaining counts after a block
            for negcnt in used_this_round:
                heapq.heappush(heap, negcnt)

        return time


# ============================================================
# Choose your active submission class
# (Math is clean and optimal; switch to Sim/Chunked for teaching)
# ------------------------------------------------------------
class Solution(SolutionMath):
    """Default to formula solution."""
    pass


# ============================================================
# Walkthrough + Tests
# ------------------------------------------------------------
def _walkthrough_examples() -> None:
    print("Walkthroughs:")
    ex1 = ["X","X","Y","Y"]; n1 = 2
    ex2 = ["A","A","A","B","C"]; n2 = 3
    print("  Ex1 Math:", SolutionMath().leastInterval(ex1, n1), " (expect 5)")
    print("  Ex1 Sim :", SolutionSim().leastInterval(ex1, n1),  " (expect 5)")
    print("  Ex2 Math:", SolutionMath().leastInterval(ex2, n2), " (expect 9)")
    print("  Ex2 Sim :", SolutionSim().leastInterval(ex2, n2),  " (expect 9)")


def _run_tests() -> None:
    impls = [
        ("Math",     SolutionMath().leastInterval),
        ("Sim",      SolutionSim().leastInterval),
        ("Chunked",  SolutionChunked().leastInterval),
        ("Active",   Solution().leastInterval),
    ]

    TESTS = [
        (["X","X","Y","Y"], 2, 5),
        (["A","A","A","B","C"], 3, 9),
        (["A"], 0, 1),
        (["A","A","A","A"], 2, 10),   # A _ _ A _ _ A _ _ A → 10
        (["A","A","A","B","B","B"], 2, 8),  # A B _ A B _ A B
        (["A","A","A","B","B","B"], 0, 6),
        (["A","B","C","D"], 3, 4),    # no repeats → no idle needed
        (["A","A","A","B","B","C","C"], 2, 7),
    ]

    all_ok = True
    for i, (tasks, n, exp) in enumerate(TESTS, 1):
        print(f"\n[{i:02d}] tasks={tasks}, n={n}, expect={exp}")
        for name, fn in impls:
            got = fn(tasks[:], n)
            ok = (got == exp)
            all_ok &= ok
            print(f"  {name:<7} -> {got}  {'✅' if ok else '❌'}")
    print("\nALL PASS ✅" if all_ok else "\nSome failures ❌")


if __name__ == "__main__":
    _walkthrough_examples()
    _run_tests()
