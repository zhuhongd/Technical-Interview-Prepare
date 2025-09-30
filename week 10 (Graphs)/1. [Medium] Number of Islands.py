from typing import List, Deque, Tuple
from collections import deque

"""
Number of Islands — EECS4070 (3 Approaches + Step-by-Step Teaching)

Problem
-------
Given a 2D grid of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and formed by connecting adjacent lands horizontally or vertically.

Teaching Objectives
-------------------
1. Understand what constitutes an "island" in grid terms
2. Learn three different algorithmic approaches
3. See step-by-step visualizations
4. Compare time/space complexities

Key Examples
------------
Example 1 (Single Island):
[
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2 (Three Islands):
[
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""

# ============================================================
# 1) DFS Recursive Approach (Most Intuitive)
# ============================================================
class SolutionDFS:
    """
    TEACHING NOTES - DFS Approach:
    - Think of this as "sinking" islands when we find them
    - When we find land ('1'), we explore all connected land using DFS
    - We mark visited land as '0' to avoid counting it again
    - This is like a "flood fill" algorithm
    
    Time Complexity: O(M × N) where M=rows, N=columns
    Space Complexity: O(M × N) in worst case (recursion stack)
    """
    
    def numIslands(self, grid: List[List[str]]) -> int:
        # Edge case: empty grid
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        
        def dfs(r: int, c: int) -> None:
            """
            Depth-First Search helper function
            EXPLANATION: This function does three things:
            1. Checks if current position is valid land
            2. Marks it as visited (sinks it to '0')
            3. Recursively explores all four directions
            """
            # Base case: out of bounds or not land
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                grid[r][c] != '1'):
                return
            
            print(f"    DFS visiting: ({r},{c}) - Sinking this land cell")
            
            # Mark as visited by changing to '0' (sink the land)
            grid[r][c] = '0'
            
            # Explore all 4 directions (think: spreading in all directions)
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up  
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left
        
        # Main algorithm: scan every cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    print(f"🚨 Found new island at ({r},{c})! Island count: {count + 1}")
                    count += 1
                    dfs(r, c)  # Sink the entire island
                    print(f"✅ Finished sinking island {count}\n")
                    
        return count


# ============================================================
# 2) BFS Approach (Avoids Recursion Limits)
# ============================================================
class SolutionBFS:
    """
    TEACHING NOTES - BFS Approach:
    - Uses a queue instead of recursion
    - Explores islands layer by layer (like ripples in water)
    - Better for very large grids to avoid stack overflow
    - Same time complexity as DFS
    
    Time Complexity: O(M × N)
    Space Complexity: O(min(M, N)) in average case
    """
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # down, up, right, left
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    print(f"🚨 Found new island at ({r},{c})! Island count: {count}")
                    
                    # BFS: use queue to explore level by level
                    queue = deque([(r, c)])
                    grid[r][c] = '0'  # Mark as visited
                    
                    while queue:
                        curr_r, curr_c = queue.popleft()
                        print(f"    BFS processing: ({curr_r},{curr_c})")
                        
                        # Check all four neighbors
                        for dr, dc in directions:
                            nr, nc = curr_r + dr, curr_c + dc
                            
                            # If neighbor is valid land, add to queue and mark visited
                            if (0 <= nr < rows and 0 <= nc < cols and 
                                grid[nr][nc] == '1'):
                                queue.append((nr, nc))
                                grid[nr][nc] = '0'  # Mark as visited
                                print(f"      Added neighbor: ({nr},{nc})")
                    
                    print(f"✅ Finished BFS for island {count}\n")
                                
        return count


# ============================================================
# 3) Union-Find (Disjoint Set) Approach
# ============================================================
class UnionFind:
    """
    TEACHING NOTES - Union-Find Data Structure:
    - Tracks connected components efficiently
    - Each cell starts as its own component
    - When we find adjacent land, we "union" their components
    - Final count = number of unique components that are land
    
    Think of it as: "Which island does this cell belong to?"
    """
    
    def __init__(self, size: int):
        self.parent = list(range(size))  # Each node points to itself initially
        self.rank = [0] * size          # For balancing the tree
        self.count = size               # Start with each cell as separate component
    
    def find(self, x: int) -> int:
        """Find the root parent of x with path compression"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x: int, y: int) -> None:
        """Union two components"""
        root_x, root_y = self.find(x), self.find(y)
        
        if root_x != root_y:
            # Union by rank to keep tree flat
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            self.count -= 1  # We merged two components

class SolutionUnionFind:
    """
    TEACHING NOTES - Union-Find Approach:
    - Map 2D coordinates to 1D indices: index = row * cols + col
    - Only check right and down to avoid duplicate unions
    - Subtract water cells from final count
    
    Time Complexity: O(M × N × α(M×N)) where α is inverse Ackermann (very slow growing)
    Space Complexity: O(M × N)
    """
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        uf = UnionFind(rows * cols)
        
        # Only check right and down to avoid duplicate unions
        directions = [(1, 0), (0, 1)]
        
        land_count = 0
        
        print("Union-Find Approach:")
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    land_count += 1
                    curr_idx = r * cols + c
                    print(f"  Land at ({r},{c}) -> index {curr_idx}")
                    
                    # Check adjacent cells to the right and down
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (0 <= nr < rows and 0 <= nc < cols and 
                            grid[nr][nc] == '1'):
                            neighbor_idx = nr * cols + nc
                            print(f"    Union: ({r},{c}) with ({nr},{nc})")
                            uf.union(curr_idx, neighbor_idx)
                else:
                    # Water cells don't form islands
                    uf.count -= 1
        
        print(f"  Final calculation: {uf.count} islands")
        return uf.count


# ============================================================
# Visualization Helper (For Teaching)
# ============================================================
def visualize_grid(grid: List[List[str]], title: str = "") -> None:
    """Display grid with nice formatting for teaching"""
    print(f"\n{title}")
    if not grid:
        print("Empty grid")
        return
    
    rows, cols = len(grid), len(grid[0])
    
    # Print column indices
    print("    " + " ".join(f"{i:2}" for i in range(cols)))
    print("   " + "---" * cols)
    
    for r in range(rows):
        print(f"{r:2} |", end=" ")
        for c in range(cols):
            cell = grid[r][c]
            if cell == '1':
                print("▓▓", end=" ")  # Land
            else:
                print("░░", end=" ")  # Water
        print()

def create_fresh_grid(original: List[List[str]]) -> List[List[str]]:
    """Create a deep copy of the grid for each solver"""
    return [row[:] for row in original]


# ============================================================
# Step-by-Step Teaching Examples
# ============================================================
def teach_with_small_example():
    """Walk through a small example step by step"""
    print("=" * 70)
    print("STEP-BY-STEP TEACHING: SMALL EXAMPLE")
    print("=" * 70)
    
    small_grid = [
        ["1", "1", "0"],
        ["0", "1", "0"],
        ["1", "0", "1"]
    ]
    
    visualize_grid(small_grid, "Our Teaching Grid:")
    print("\nThis grid has 3 islands:")
    print("1. Top-left 2x2 block")
    print("2. Bottom-left single cell")  
    print("3. Bottom-right single cell")
    
    # Test DFS with verbose output
    print("\n" + "="*50)
    print("DEMONSTRATING DFS APPROACH")
    print("="*50)
    
    grid_copy = create_fresh_grid(small_grid)
    solver = SolutionDFS()
    result = solver.numIslands(grid_copy)
    print(f"\n🎯 FINAL RESULT: {result} islands found")

def compare_all_approaches():
    """Compare all three approaches on the same grid"""
    print("\n" + "=" * 70)
    print("COMPARING ALL THREE APPROACHES")
    print("=" * 70)
    
    test_grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    
    visualize_grid(test_grid, "Test Grid for Comparison:")
    
    approaches = [
        ("DFS Recursive", SolutionDFS()),
        ("BFS Queue    ", SolutionBFS()),
        ("Union-Find   ", SolutionUnionFind())
    ]
    
    for name, solver in approaches:
        print(f"\n{'='*40}")
        print(f"APPROACH: {name}")
        print('='*40)
        
        grid_copy = create_fresh_grid(test_grid)
        result = solver.numIslands(grid_copy)
        print(f"✅ {name} found: {result} islands")


# ============================================================
# Comprehensive Test Suite
# ============================================================
def run_comprehensive_tests():
    """Test all approaches on various grid configurations"""
    print("\n" + "=" * 70)
    print("COMPREHENSIVE TEST SUITE")
    print("=" * 70)
    
    test_cases = [
        # (grid, expected, description)
        (
            [  # Single island
                ["1","1","1","1","0"],
                ["1","1","0","1","0"],
                ["1","1","0","0","0"],
                ["0","0","0","0","0"]
            ],
            1,
            "Single Large Island"
        ),
        (
            [  # Three islands
                ["1","1","0","0","0"],
                ["1","1","0","0","0"],
                ["0","0","1","0","0"],
                ["0","0","0","1","1"]
            ],
            3,
            "Three Separate Islands"
        ),
        (
            [  # All water
                ["0","0","0"],
                ["0","0","0"],
                ["0","0","0"]
            ],
            0,
            "All Water (No Islands)"
        ),
        (
            [  # All land (one big island)
                ["1","1"],
                ["1","1"]
            ],
            1,
            "All Land (Single Island)"
        ),
        (
            [  # Single cell
                ["1"]
            ],
            1,
            "Single Cell Land"
        )
    ]
    
    approaches = [
        ("DFS", SolutionDFS()),
        ("BFS", SolutionBFS()), 
        ("Union-Find", SolutionUnionFind())
    ]
    
    print("\nSUMMARY RESULTS:")
    print("-" * 50)
    
    for grid, expected, description in test_cases:
        print(f"\n📋 {description}:")
        visualize_grid(grid, "Grid Layout")
        print(f"Expected: {expected} islands")
        
        for name, solver in approaches:
            grid_copy = create_fresh_grid(grid)
            result = solver.numIslands(grid_copy)
            status = "✅ PASS" if result == expected else "❌ FAIL"
            print(f"  {name}: {result} islands {status}")


# ============================================================
# Complexity Analysis Section
# ============================================================
def explain_complexity():
    """Explain time and space complexity for each approach"""
    print("\n" + "=" * 70)
    print("COMPLEXITY ANALYSIS")
    print("=" * 70)
    
    print("""
DFS Recursive:
- Time: O(M × N) - We visit each cell once
- Space: O(M × N) worst case - Recursion stack for a spiral island

BFS Approach:  
- Time: O(M × N) - Same as DFS, each cell visited once
- Space: O(min(M, N)) - Queue size for a balanced BFS

Union-Find:
- Time: O(M × N × α(M×N)) - α is inverse Ackermann (very slow growing)
- Space: O(M × N) - For parent and rank arrays

WHICH TO CHOOSE?
- DFS: Most intuitive, good for interviews
- BFS: Avoids stack overflow for huge grids  
- Union-Find: Good for dynamic connectivity problems
""")


# ============================================================
# Main Execution - Run All Teaching Sections
# ============================================================
if __name__ == "__main__":
    # Start with basic concepts
    print("🌴 NUMBER OF ISLANDS - COMPLETE TEACHING GUIDE 🌴")
    print("\nKEY CONCEPT: An 'island' is a group of '1's connected horizontally or vertically.")
    print("Water ('0') separates islands. Diagonal connections don't count!\n")
    
    # Run all teaching sections
    teach_with_small_example()
    compare_all_approaches() 
    explain_complexity()
    run_comprehensive_tests()
