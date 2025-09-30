from typing import List, Deque, Tuple
from collections import deque

"""
Rotting Fruit — EECS4070 (Multiple Approaches) + Grid Visualization
"""

# ============================================================
# 1) Multi-Source BFS (Optimal Solution)
#    Time: O(M×N) | Space: O(M×N)
# ============================================================
class SolutionBFS:
    def rottingFruit(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        fresh_count = 0
        
        # Step 1: Find all rotten fruits and count fresh fruits
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        # If no fresh fruits to begin with
        if fresh_count == 0:
            return 0
        
        minutes = 0
        
        # Step 2: Multi-source BFS from all rotten fruits
        while queue and fresh_count > 0:
            level_size = len(queue)
            infected_this_minute = False
            
            for _ in range(level_size):
                r, c = queue.popleft()
                
                # Explore neighbors
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    # Check if neighbor is valid and is fresh fruit
                    if (0 <= nr < ROWS and 0 <= nc < COLS and 
                        grid[nr][nc] == 1):
                        # Infect this fresh fruit
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        fresh_count -= 1
                        infected_this_minute = True
            
            if infected_this_minute:
                minutes += 1
        
        # Step 3: Check if any fresh fruits remain
        return minutes if fresh_count == 0 else -1


# ============================================================
# 2) BFS with Explicit Minute Tracking
#    Time: O(M×N) | Space: O(M×N)
# ============================================================
class SolutionBFSClear:
    def rottingFruit(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()
        fresh_count = 0
        
        # Initialize queue with rotten fruits and count fresh fruits
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, minute)
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0
        
        max_minutes = 0
        
        # BFS from all rotten fruits
        while queue:
            r, c, minute = queue.popleft()
            max_minutes = max(max_minutes, minute)
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if (0 <= nr < ROWS and 0 <= nc < COLS and 
                    grid[nr][nc] == 1):
                    # Infect fresh fruit
                    grid[nr][nc] = 2
                    queue.append((nr, nc, minute + 1))
                    fresh_count -= 1
        
        return max_minutes if fresh_count == 0 else -1


# ============================================================
# Active alias
# ============================================================
class Solution(SolutionBFS):
    """Uses multi-source BFS by default."""
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
            if cell == 0:
                print(" ◻ ", end="")  # Empty
            elif cell == 1:
                print(" 🍎", end="")  # Fresh fruit
            elif cell == 2:
                print(" 🤢", end="")  # Rotten fruit
        print()

def create_fresh_grid(original: List[List[int]]) -> List[List[int]]:
    """Create a deep copy of the grid for each solver"""
    return [row[:] for row in original]

def analyze_grid(grid: List[List[int]]) -> dict:
    """Analyze grid composition"""
    if not grid:
        return {"empty": 0, "fresh": 0, "rotten": 0}
    
    empty_count = 0
    fresh_count = 0
    rotten_count = 0
    
    for row in grid:
        for cell in row:
            if cell == 0:
                empty_count += 1
            elif cell == 1:
                fresh_count += 1
            elif cell == 2:
                rotten_count += 1
    
    return {
        "empty": empty_count,
        "fresh": fresh_count,
        "rotten": rotten_count,
        "total": len(grid) * len(grid[0])
    }


# -----------------------------
# Corrected Test Suite
# -----------------------------
def _run_tests() -> None:
    impls = [
        ("BFS", SolutionBFS().rottingFruit),
        ("BFS-Clear", SolutionBFSClear().rottingFruit),
    ]

    TESTS: List[Tuple[List[List[int]], int, str]] = [
        # Example 1
        (
            [
                [1, 1, 0],
                [0, 1, 1],
                [0, 1, 2]
            ],
            4,
            "example-1"
        ),
        # Example 2
        (
            [
                [1, 0, 1],
                [0, 2, 0],
                [1, 0, 1]
            ],
            -1,
            "example-2-unreachable"
        ),
        # All rotten initially
        (
            [
                [2, 2],
                [2, 2]
            ],
            0,
            "all-rotten-initial"
        ),
        # All fresh (impossible)
        (
            [
                [1, 1],
                [1, 1]
            ],
            -1,
            "all-fresh-no-rotten"
        ),
        # Single rotten
        (
            [
                [2, 1, 1],
                [1, 1, 0],
                [0, 1, 1]
            ],
            4,
            "single-rotten-center"
        ),
        # Immediate completion
        (
            [
                [2, 1],
                [1, 2]
            ],
            1,
            "multiple-rotten-quick"
        ),
        # Empty grid
        (
            [
                [0, 0],
                [0, 0]
            ],
            0,
            "all-empty"
        ),
        # CORRECTED: Complex case - should take 2 minutes
        (
            [
                [2, 1, 1],
                [0, 1, 1],
                [1, 0, 2]
            ],
            2,
            "complex-case"
        ),
        # Additional test: Chain reaction
        (
            [
                [2, 1, 0],
                [1, 1, 1],
                [0, 1, 1]
            ],
            4,
            "chain-reaction"
        )
    ]

    VIS = {
        "example-1",
        "example-2-unreachable", 
        "single-rotten-center",
        "multiple-rotten-quick",
        "complex-case",
        "chain-reaction"
    }

    passed = 0
    total = 0

    for i, (input_grid, expected, label) in enumerate(TESTS, 1):
        print(f"\n[{i:02d}][{label}]")
        
        if label in VIS:
            grid_analysis = analyze_grid(input_grid)
            visualize_grid(input_grid, f"Input: {label}")
            print(f"Grid analysis: {grid_analysis['fresh']} fresh, {grid_analysis['rotten']} rotten, {grid_analysis['empty']} empty")

        results = []
        for name, solver in impls:
            # Create fresh copy for each solver
            grid_copy = create_fresh_grid(input_grid)
            result = solver(grid_copy)
            
            ok = (result == expected)
            results.append((name, result, ok))
            
            if label in VIS:
                final_analysis = analyze_grid(grid_copy)
                status = "✅ COMPLETE" if result != -1 else "❌ IMPOSSIBLE"
                print(f"  {name}: {result} minutes ({status})")
                print(f"  Final: {final_analysis['fresh']} fresh remaining")

        for name, result, ok in results:
            total += 1
            passed += ok
            status = "✅" if ok else "❌"
            print(f"  {name}: got={result} expected={expected} | {status}")

        agree = len({r[1] for r in results}) == 1
        print(f"  impls-agree: {'✅' if agree else '❌'}")

    print(f"\nPassed {passed}/{total} checks.")


# -----------------------------
# Debug the complex case
# -----------------------------
def debug_complex_case():
    """Debug the complex case step by step"""
    print("=" * 60)
    print("DEBUG: COMPLEX CASE")
    print("=" * 60)
    
    grid = [
        [2, 1, 1],
        [0, 1, 1],
        [1, 0, 2]
    ]
    
    print("Initial grid:")
    visualize_grid(grid)
    print()
    
    # Manual simulation
    current_grid = create_fresh_grid(grid)
    minutes = 0
    
    while True:
        print(f"Minute {minutes}:")
        visualize_grid(current_grid)
        
        # Find fruits that will rot next minute
        next_rotten = []
        for r in range(len(current_grid)):
            for c in range(len(current_grid[0])):
                if current_grid[r][c] == 2:
                    # Check neighbors
                    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                        nr, nc = r + dr, c + dc
                        if (0 <= nr < len(current_grid) and 
                            0 <= nc < len(current_grid[0]) and 
                            current_grid[nr][nc] == 1):
                            next_rotten.append((nr, nc))
        
        if not next_rotten:
            fresh_remaining = sum(cell == 1 for row in current_grid for cell in row)
            if fresh_remaining > 0:
                print(f"❌ Stuck with {fresh_remaining} fresh fruits remaining")
                break
            else:
                print(f"✅ All fruits rotten after {minutes} minutes!")
                break
        
        # Apply rotting
        for r, c in next_rotten:
            current_grid[r][c] = 2
            print(f"  ({r},{c}) became rotten")
        
        minutes += 1
        print()


if __name__ == "__main__":
    # First debug the problematic case
    debug_complex_case()
    
    # Then run all tests
    _run_tests()

    