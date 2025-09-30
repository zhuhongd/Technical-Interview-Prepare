from typing import List, Deque, Tuple
from collections import deque

"""
Islands and Treasure — EECS4070 (Multiple Approaches) + Grid Visualization

Problem
-------
Given a m×n grid with:
  -1  : Water (cannot traverse)
   0  : Treasure chest (starting point)
   INF: Land (traversable, needs distance to nearest treasure)

Fill each land cell with the distance to nearest treasure.
If unreachable, leave as INF.

Key Examples
------------
Example 1:
Input: 
[
  [INF, -1,  0,  INF],
  [INF, INF, INF, -1],
  [INF, -1,  INF, -1],
  [0,   -1,  INF, INF]
]
Output:
[
  [3, -1, 0, 1],
  [2,  2, 1, -1],
  [1, -1, 2, -1],
  [0, -1, 3, 4]
]

Example 2:
Input:
[
  [0, -1],
  [INF, INF]
]
Output:
[
  [0, -1],
  [1, 2]
]

What the grader expects
-----------------------
• Modify the grid IN-PLACE
• Only move up, down, left, right (no diagonals)
• Fill distances from nearest treasure
• Leave unreachable land as INF
• Water cells remain -1

Beginner Intuition
------------------
Think of "ripples" spreading from ALL treasures simultaneously:
1) All treasure cells (0) are starting points
2) From each treasure, explore neighbors level by level
3) Each level = distance + 1 from treasure
4) Stop when no more reachable land cells

Tiny Visuals
------------
Initial:           After BFS:
  INF -1   0  INF     3  -1   0   1
  INF INF INF -1      2   2   1  -1  
  INF -1  INF -1      1  -1   2  -1
   0  -1  INF INF     0  -1   3   4

Thinking Process (step-by-step)
-------------------------------
This is a MULTI-SOURCE BFS problem:
- Put ALL treasure cells (0) in the queue with distance 0
- For each cell in queue:
  * Check its 4 neighbors
  * If neighbor is land (INF), update its distance and add to queue
  * Distance = current_distance + 1

Approaches
----------
1) Multi-Source BFS (Optimal)
   - Start from ALL treasures simultaneously
   - Time O(M×N), Space O(M×N)

2) Brute Force BFS from each land cell (Inefficient)
   - Would be O((M×N)^2) - too slow for constraints

Why Multi-Source BFS works
--------------------------
All treasures are equivalent starting points. By processing them together,
we guarantee each land cell gets the MINIMUM distance to ANY treasure.

Common Pitfalls
---------------
• Starting BFS from land cells instead of treasures
• Not using multi-source BFS (would be too slow)
• Modifying water cells (should remain -1)
• Forgetting to check bounds
• Not using a queue for BFS

Complexity Summary
------------------
Let M = rows, N = columns
• Time  : O(M×N) - each cell processed at most once
• Space : O(M×N) - for the queue in worst case
"""

INF = 2147483647


# ============================================================
# 1) Multi-Source BFS (Optimal Solution)
#    Time: O(M×N) | Space: O(M×N)
# ============================================================
class SolutionBFS:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        """
        Do not return anything, modify grid in-place.
        """
        if not grid or not grid[0]:
            return
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        
        # Step 1: Find all treasure cells (0) and add to queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        # Step 2: Multi-source BFS from all treasures
        distance = 0
        while queue:
            # Process all nodes at current distance level
            level_size = len(queue)
            print(f"BFS Level {distance}: Processing {level_size} cells")
            
            for _ in range(level_size):
                r, c = queue.popleft()
                
                # Explore neighbors
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Check if neighbor is valid and is unvisited land
                    if (0 <= nr < ROWS and 0 <= nc < COLS and 
                        grid[nr][nc] == INF):
                        # Update distance and add to queue
                        grid[nr][nc] = distance + 1
                        queue.append((nr, nc))
                        print(f"  Updated ({nr},{nc}) to distance {distance + 1}")
            
            distance += 1


# ============================================================
# 2) Alternative: Clear BFS with Visited Set
#    Time: O(M×N) | Space: O(M×N)
# ============================================================
class SolutionBFSClear:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        
        # Add all treasure cells to queue with distance 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))  # (row, col, distance)
        
        # BFS from all treasures
        while queue:
            r, c, dist = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if (0 <= nr < ROWS and 0 <= nc < COLS and 
                    grid[nr][nc] == INF):
                    # Found unvisited land cell
                    new_dist = dist + 1
                    grid[nr][nc] = new_dist
                    queue.append((nr, nc, new_dist))
                    print(f"Updated ({nr},{nc}) to distance {new_dist}")


# ============================================================
# Active alias
# ============================================================
class Solution(SolutionBFS):
    """LeetCode-style single-class entry; uses multi-source BFS by default."""
    pass


# -----------------------------
# Grid Visualization Helpers
# -----------------------------
def visualize_grid(grid: List[List[int]], title: str = "") -> None:
    """Display grid with nice formatting"""
    print(f"\n--- {title} ---")
    if not grid:
        print("Empty grid")
        return
    
    ROWS, COLS = len(grid), len(grid[0])
    
    # Print column indices
    print("    " + " ".join(f"{i:2}" for i in range(COLS)))
    print("   " + "---" * COLS)
    
    for r in range(ROWS):
        print(f"{r:2} |", end=" ")
        for c in range(COLS):
            cell = grid[r][c]
            if cell == -1:
                print(" ██", end="")  # Water
            elif cell == 0:
                print(" 💰", end="")  # Treasure
            elif cell == INF:
                print(" ∞ ", end="")  # Unvisited land
            else:
                print(f"{cell:2} ", end="")  # Distance
        print()

def create_fresh_grid(original: List[List[int]]) -> List[List[int]]:
    """Create a deep copy of the grid for each solver"""
    return [row[:] for row in original]


# -----------------------------
# Comprehensive Test Suite
# -----------------------------
def _run_tests() -> None:
    impls = [
        ("BFS", SolutionBFS().islandsAndTreasure),
        ("BFS-Clear", SolutionBFSClear().islandsAndTreasure),
    ]

    TESTS: List[Tuple[List[List[int]], List[List[int]], str]] = [
        # Example 1
        (
            [
                [INF, -1,  0,  INF],
                [INF, INF, INF, -1],
                [INF, -1,  INF, -1],
                [0,   -1,  INF, INF]
            ],
            [
                [3, -1, 0, 1],
                [2,  2, 1, -1],
                [1, -1, 2, -1],
                [0, -1, 3, 4]
            ],
            "example-1"
        ),
        # Example 2
        (
            [
                [0, -1],
                [INF, INF]
            ],
            [
                [0, -1],
                [1, 2]
            ],
            "example-2"
        ),
        # Single treasure
        (
            [
                [0, INF, INF],
                [INF, -1, INF],
                [INF, INF, 0]
            ],
            [
                [0, 1, 2],
                [1, -1, 1],
                [2, 1, 0]
            ],
            "two-treasures"
        ),
        # All treasures
        (
            [
                [0, 0],
                [0, 0]
            ],
            [
                [0, 0],
                [0, 0]
            ],
            "all-treasures"
        ),
        # All water
        (
            [
                [-1, -1],
                [-1, -1]
            ],
            [
                [-1, -1],
                [-1, -1]
            ],
            "all-water"
        ),
        # Unreachable land
        (
            [
                [0, -1, INF],
                [-1, -1, INF],
                [INF, INF, INF]
            ],
            [
                [0, -1, INF],
                [-1, -1, INF],
                [INF, INF, INF]
            ],
            "unreachable-land"
        ),
        # Complex case
        (
            [
                [INF, -1,  0,  INF],
                [INF, INF, INF, -1],
                [INF, -1,  INF, -1],
                [0,   -1,  INF, INF]
            ],
            [
                [3, -1, 0, 1],
                [2,  2, 1, -1],
                [1, -1, 2, -1],
                [0, -1, 3, 4]
            ],
            "complex-case"
        )
    ]

    VIS = {
        "example-1",
        "example-2",
        "two-treasures",
        "unreachable-land",
        "complex-case"
    }

    passed = 0
    total = 0

    for i, (input_grid, expected, label) in enumerate(TESTS, 1):
        print(f"\n[{i:02d}][{label}]")
        
        if label in VIS:
            visualize_grid(input_grid, f"Input: {label}")

        results = []
        for name, solver in impls:
            # Create fresh copy for each solver
            grid_copy = create_fresh_grid(input_grid)
            solver(grid_copy)
            
            ok = (grid_copy == expected)
            results.append((name, grid_copy, ok))
            
            if label in VIS:
                visualize_grid(grid_copy, f"Output ({name}): {label}")

        for name, result, ok in results:
            total += 1
            passed += ok
            status = "✅" if ok else "❌"
            print(f"  {name}: {status}")

        agree = len({str(r[1]) for r in results}) == 1
        print(f"  impls-agree: {'✅' if agree else '❌'}")

    print(f"\nPassed {passed}/{total} checks.")


# -----------------------------
# Educational Demonstration
# -----------------------------
def _demonstrate_bfs_step_by_step():
    """Show BFS process step by step"""
    print("=" * 60)
    print("EDUCATIONAL DEMONSTRATION: BFS STEP BY STEP")
    print("=" * 60)
    
    demo_grid = [
        [INF, -1,  0,  INF],
        [INF, INF, INF, -1],
        [INF, -1,  INF, -1],
        [0,   -1,  INF, INF]
    ]
    
    visualize_grid(demo_grid, "Initial Grid")
    
    print("\nBFS Process:")
    print("1. Find all treasure cells (0) and add to queue")
    print("2. For each cell in queue, explore neighbors")
    print("3. Update land cells (INF) with current distance + 1")
    print("4. Continue until queue is empty\n")
    
    # Manually demonstrate first few steps
    print("Step 0: Treasures at (0,2) and (3,0)")
    print("Step 1: Update neighbors of treasures to distance 1")
    print("Step 2: Update their neighbors to distance 2")
    print("Step 3: Continue until all reachable land is updated")
    
    # Run the actual algorithm
    solver = SolutionBFS()
    grid_copy = create_fresh_grid(demo_grid)
    solver.islandsAndTreasure(grid_copy)
    
    visualize_grid(grid_copy, "Final Result")


# -----------------------------
# Algorithm Analysis
# -----------------------------
def analyze_algorithm():
    """Explain why multi-source BFS is optimal"""
    print("\n" + "=" * 60)
    print("ALGORITHM ANALYSIS: WHY MULTI-SOURCE BFS?")
    print("=" * 60)
    
    print("""
COMPLEXITY COMPARISON:

1) Multi-Source BFS (Our Solution):
   - Start from ALL treasure cells
   - Time: O(M×N) - each cell processed once
   - Space: O(M×N) - for the queue

2) BFS from Each Land Cell (Naive):
   - For each land cell, BFS to find nearest treasure
   - Time: O((M×N)²) - 100×100 grid → 10,000×10,000 = 100M operations!
   - Space: O(M×N) - but way too slow

3) BFS from Each Treasure (Also Bad):
   - For each treasure, BFS to update all land cells
   - Keep minimum distance
   - Time: O(T×M×N) where T = number of treasures
   - Still worse than multi-source BFS

WHY MULTI-SOURCE BFS WORKS:
- All treasures are equivalent starting points
- BFS naturally finds shortest paths
- By starting from ALL treasures, we guarantee each land cell
  gets the minimum distance to ANY treasure
- Like multiple ripples spreading simultaneously
""")


if __name__ == "__main__":
    _demonstrate_bfs_step_by_step()
    analyze_algorithm()
    _run_tests()