from typing import List, Deque, Tuple
from collections import deque

"""
Max Area of Island — EECS4070 (Multiple Approaches) + Grid Visualization

Link: https://leetcode.com/problems/max-area-of-island/

Problem
-------
Given a 2D grid of 0's (water) and 1's (land), return the maximum area of an island.
An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water.

Key Examples
------------
Input: grid = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]
Output: 6
Explanation: The largest connected group of 1's has area 6.

Input: grid = [
  [1,1,0,0,0],
  [1,1,0,0,0],
  [0,0,1,0,0],
  [0,0,0,1,1]
]
Output: 4

What the grader expects
-----------------------
• Find ALL connected components of 1's
• Calculate each component's size (area)
• Return the LARGEST area found
• Return 0 if no islands exist

Beginner Intuition
------------------
Think of "flood filling" each island:
1) Scan the grid cell by cell
2) When you find land (1), explore all connected land cells
3) Count how many cells are in this island
4) Track the maximum count encountered

Tiny Visuals
------------
Grid with max area 6:

    0 1 1 0 1
    1 0 1 0 1  
    0 1 1 0 1
    0 1 0 0 1

The largest connected component has 6 cells.

Grid with max area 4:

    1 1 0 0 0
    1 1 0 0 0
    0 0 1 0 0
    0 0 0 1 1

Three islands with areas 4, 1, and 2 → max is 4.

Thinking Process (step-by-step)
-------------------------------
For each cell (r, c):
- If it's water (0) or visited → skip
- If it's land (1) and not visited:
  * Start DFS/BFS to explore entire island
  * Count all connected land cells
  * Update global maximum
  * Mark visited cells to avoid double-counting

Approaches (exactly what you asked for)
---------------------------------------
1) Depth-First Search (Recursive)
   - Natural for connected components
   - Time O(M×N), Space O(M×N) for recursion stack

2) Breadth-First Search (Queue)
   - Level-order exploration
   - Time O(M×N), Space O(min(M,N)) average

3) Iterative DFS (Stack)
   - Avoids recursion limits
   - Time O(M×N), Space O(M×N)

Why this works
--------------
We systematically explore each connected component exactly once by marking visited cells.
The area calculation is straightforward: count cells during exploration.

Common Pitfalls
---------------
• Forgetting to mark cells as visited → infinite loops
• Not checking all 4 directions
• Missing the case where no islands exist
• Counting diagonal connections (not allowed)

Complexity Summary
------------------
Let M = rows, N = columns
• Time  : O(M×N) — each cell visited once
• Space : O(M×N) for recursion/stack in worst case
           O(min(M,N)) for BFS queue on average
"""


# ============================================================
# 1) Depth First Search (Recursive) — Most Intuitive
#    Time: O(M×N) | Space: O(M×N)
# ============================================================
class SolutionDFS:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        
        def dfs(r: int, c: int) -> int:
            """Explore island and return its area"""
            # Base cases: out of bounds, water, or already visited
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                grid[r][c] == 0 or 
                (r, c) in visited):
                return 0
            
            # Mark current cell and count it
            visited.add((r, c))
            area = 1
            
            # Explore all 4 directions
            area += dfs(r + 1, c)  # down
            area += dfs(r - 1, c)  # up
            area += dfs(r, c + 1)  # right
            area += dfs(r, c - 1)  # left
            
            return area
        
        # Scan entire grid
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    current_area = dfs(r, c)
                    max_area = max(max_area, current_area)
                    
        return max_area


# ============================================================
# 2) Breadth First Search (Queue) — Level-order Exploration
#    Time: O(M×N) | Space: O(min(M,N))
# ============================================================
class SolutionBFS:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def bfs(start_r: int, start_c: int) -> int:
            """Explore island using BFS and return its area"""
            queue = deque()
            queue.append((start_r, start_c))
            visited.add((start_r, start_c))
            area = 0
            
            while queue:
                r, c = queue.popleft()
                area += 1
                
                # Check all neighbors
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and 
                        grid[nr][nc] == 1 and 
                        (nr, nc) not in visited):
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            
            return area
        
        # Scan entire grid
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    current_area = bfs(r, c)
                    max_area = max(max_area, current_area)
                    
        return max_area


# ============================================================
# 3) Iterative DFS (Stack) — Avoids Recursion Limits
#    Time: O(M×N) | Space: O(M×N)
# ============================================================
class SolutionDFSIter:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        max_area = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs_iterative(start_r: int, start_c: int) -> int:
            """Explore island using iterative DFS and return its area"""
            stack = [(start_r, start_c)]
            visited.add((start_r, start_c))
            area = 0
            
            while stack:
                r, c = stack.pop()
                area += 1
                
                # Check all neighbors
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and 
                        grid[nr][nc] == 1 and 
                        (nr, nc) not in visited):
                        stack.append((nr, nc))
                        visited.add((nr, nc))
            
            return area
        
        # Scan entire grid
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    current_area = dfs_iterative(r, c)
                    max_area = max(max_area, current_area)
                    
        return max_area


# ============================================================
# Active alias (optional): pick DFS by default
# ============================================================
class Solution(SolutionDFS):
    """LeetCode-style single-class entry; uses recursive DFS by default."""
    pass


# -----------------------------
# Grid Visualization Helper
# -----------------------------
def visualize_grid(grid: List[List[int]], title: str = "") -> None:
    """Display grid with nice ASCII formatting"""
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
            if cell == 1:
                print("▓▓", end=" ")  # Land
            else:
                print("░░", end=" ")  # Water
        print()

def visualize_grid_with_areas(grid: List[List[int]], areas: List[Tuple[int, int, int]], title: str = "") -> None:
    """Display grid with area annotations"""
    print(f"\n--- {title} ---")
    if not grid:
        print("Empty grid")
        return
    
    ROWS, COLS = len(grid), len(grid[0])
    
    # Create a copy to mark areas
    display_grid = [row[:] for row in grid]
    
    # Mark each island with its area (for visualization)
    area_map = {}
    for area_id, (start_r, start_c, area) in enumerate(areas, 1):
        # Simple BFS to mark this island
        queue = deque([(start_r, start_c)])
        visited = set([(start_r, start_c)])
        
        while queue:
            r, c = queue.popleft()
            # We'll use negative numbers to represent different islands for display
            display_grid[r][c] = -area_id
            
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if (0 <= nr < ROWS and 0 <= nc < COLS and 
                    grid[nr][nc] == 1 and 
                    (nr, nc) not in visited):
                    queue.append((nr, nc))
                    visited.add((nr, nc))
    
    # Print the grid with area indicators
    print("    " + " ".join(f"{i:2}" for i in range(COLS)))
    print("   " + "---" * COLS)
    
    for r in range(ROWS):
        print(f"{r:2} |", end=" ")
        for c in range(COLS):
            cell = display_grid[r][c]
            if cell == 0:
                print("░░", end=" ")  # Water
            elif cell < 0:
                area_id = -cell
                area_size = [a[2] for a in areas if a[0] == r and a[1] == c][0]
                print(f"A{area_size}", end="")  # Island with area
            else:
                print("▓▓", end=" ")  # Land (shouldn't happen)
        print()

def analyze_grid_areas(grid: List[List[int]]) -> List[Tuple[int, int, int]]:
    """Find all islands and their areas for visualization"""
    if not grid or not grid[0]:
        return []
    
    ROWS, COLS = len(grid), len(grid[0])
    visited = set()
    areas = []
    
    def dfs_area(r: int, c: int) -> int:
        if (r < 0 or r >= ROWS or c < 0 or c >= COLS or 
            grid[r][c] == 0 or (r, c) in visited):
            return 0
        
        visited.add((r, c))
        area = 1
        area += dfs_area(r + 1, c)
        area += dfs_area(r - 1, c)
        area += dfs_area(r, c + 1)
        area += dfs_area(r, c - 1)
        return area
    
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1 and (r, c) not in visited:
                area = dfs_area(r, c)
                areas.append((r, c, area))
    
    return areas


# -----------------------------
# Comprehensive Test Suite
# -----------------------------
def _run_tests() -> None:
    impls = [
        ("DFS-Rec", SolutionDFS().maxAreaOfIsland),
        ("BFS    ", SolutionBFS().maxAreaOfIsland),
        ("DFS-It ", SolutionDFSIter().maxAreaOfIsland),
    ]

    TESTS: List[Tuple[List[List[int]], int, str]] = [
        # Main examples
        (
            [
                [0,1,1,0,1],
                [1,0,1,0,1],
                [0,1,1,0,1],
                [0,1,0,0,1]
            ],
            6,
            "example-1-area-6"
        ),
        (
            [
                [1,1,0,0,0],
                [1,1,0,0,0],
                [0,0,1,0,0],
                [0,0,0,1,1]
            ],
            4,
            "example-2-area-4"
        ),
        
        # Edge cases
        (
            [],
            0,
            "empty-grid"
        ),
        (
            [[0,0,0],[0,0,0]],
            0,
            "all-water"
        ),
        (
            [[1]],
            1,
            "single-cell"
        ),
        (
            [[1,1,1],[1,1,1],[1,1,1]],
            9,
            "all-land"
        ),
        
        # Various shapes
        (
            [
                [1,0,1,0,1],
                [0,1,0,1,0],
                [1,0,1,0,1]
            ],
            1,
            "checkerboard"
        ),
        (
            [
                [1,1,1,0],
                [0,0,1,0],
                [1,1,1,1],
                [0,1,0,0]
            ],
            8,
            "complex-shape"
        ),
        (
            [
                [1,1,0,0,1],
                [1,0,0,0,0],
                [0,0,1,1,1],
                [1,0,0,1,1]
            ],
            5,
            "multiple-islands"
        )
    ]

    VIS = {
        "example-1-area-6",
        "example-2-area-4", 
        "all-land",
        "complex-shape",
        "multiple-islands"
    }

    passed = 0
    total = 0

    for i, (grid, expected, label) in enumerate(TESTS, 1):
        print(f"\n[{i:02d}][{label}]")
        
        if label in VIS and grid:
            visualize_grid(grid, f"Grid: {label}")
            areas = analyze_grid_areas(grid)
            if areas:
                max_a = max(area for _, _, area in areas)
                print(f"Found {len(areas)} islands with areas: {[area for _, _, area in areas]}")
                print(f"Maximum area: {max_a}")

        results = []
        for name, f in impls:
            # Create fresh grid for each solver
            grid_copy = [row[:] for row in grid] if grid else []
            got = f(grid_copy)
            ok = (got == expected)
            results.append((name, got, ok))

        for name, got, ok in results:
            total += 1
            passed += ok
            print(f"  {name} -> got={got:<2} expected={expected:<2} | {'✅' if ok else '❌'}")

        agree = len({r[1] for r in results}) == 1
        print(f"  impls-agree: {'✅' if agree else '❌'}")

    print(f"\nPassed {passed}/{total} checks.")


# -----------------------------
# Educational Examples
# -----------------------------
def _demonstrate_approaches():
    """Show how each approach works on a simple example"""
    print("=" * 60)
    print("EDUCATIONAL DEMONSTRATION")
    print("=" * 60)
    
    demo_grid = [
        [1, 1, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 1, 1]
    ]
    
    visualize_grid(demo_grid, "Demo Grid")
    areas = analyze_grid_areas(demo_grid)
    print(f"\nIsland analysis: {len(areas)} islands found")
    for i, (r, c, area) in enumerate(areas, 1):
        print(f"  Island {i}: starts at ({r},{c}), area = {area}")
    
    print(f"\nMaximum area: {max(area for _, _, area in areas)}")
    
    # Test all approaches
    print("\nApproach Results:")
    for name, solver in [("DFS", SolutionDFS()), ("BFS", SolutionBFS()), ("DFS-Iter", SolutionDFSIter())]:
        grid_copy = [row[:] for row in demo_grid]
        result = solver.maxAreaOfIsland(grid_copy)
        print(f"  {name}: {result}")


if __name__ == "__main__":
    _demonstrate_approaches()
    _run_tests()