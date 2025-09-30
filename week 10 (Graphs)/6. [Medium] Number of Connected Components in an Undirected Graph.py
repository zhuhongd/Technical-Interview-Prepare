from typing import List, Deque, Set, Dict
from collections import deque

"""
Number of Connected Components in an Undirected Graph — EECS4070 (Multiple Approaches) + Graph Visualization

Problem
-------
Given n nodes numbered from 0 to n-1 and an array of edges, return the number of connected components.

Key Examples
------------
Example 1:
Input: n=3, edges=[[0,1], [0,2]]
Output: 1
Explanation: All 3 nodes are connected in one component.

Example 2:
Input: n=6, edges=[[0,1], [1,2], [2,3], [4,5]]
Output: 2
Explanation: Two connected components: [0,1,2,3] and [4,5]

What the grader expects
-----------------------
• Count the number of connected components
• Handle isolated nodes (components of size 1)
• Work with undirected edges

Beginner Intuition
------------------
Think of "exploring" each connected group:
1) Start from any unvisited node
2) Explore all reachable nodes (DFS/BFS)
3) That's one connected component
4) Repeat until all nodes are visited

Tiny Visuals
------------
Example 1:        Example 2:
  0 — 1             0 — 1 — 2 — 3
   \ /              
    2               4 — 5

1 component        2 components

Thinking Process (step-by-step)
-------------------------------
1) Build adjacency list from edges
2) Maintain visited array to track explored nodes  
3) For each unvisited node:
   - Start DFS/BFS to explore entire component
   - Mark all reachable nodes as visited
   - Increment component count

Approaches
----------
1) Depth-First Search (Recursive)
   - Natural for graph exploration
   - Time O(V+E), Space O(V+E)

2) Breadth-First Search (Queue)
   - Level-order exploration
   - Time O(V+E), Space O(V+E)

3) Union-Find (Disjoint Set)
   - Efficient for dynamic connectivity
   - Time O(V+E×α(V)), Space O(V)

Why these work
--------------
All approaches systematically explore/discover connected components.
DFS/BFS traverse each component entirely before moving to the next.

Common Pitfalls
---------------
• Forgetting graph is undirected (add both directions)
• Not handling isolated nodes (they are components too!)
• Missing the visited checks

Complexity Summary
------------------
Let V = number of vertices, E = number of edges
• Time  : O(V+E) - each node and edge processed once
• Space : O(V+E) - for adjacency list and visited array
"""


# ============================================================
# 1) Depth First Search (Recursive) — Most Intuitive
#    Time: O(V+E) | Space: O(V+E)
# ============================================================
class SolutionDFS:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * n
        components = 0
        
        def dfs(node: int) -> None:
            """Explore entire connected component using DFS"""
            visited[node] = True
            print(f"  DFS visiting node {node}")
            
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    print(f"    Exploring neighbor {neighbor} from node {node}")
                    dfs(neighbor)
        
        # Find connected components
        for node in range(n):
            if not visited[node]:
                print(f"🚨 Starting new component from node {node}")
                components += 1
                dfs(node)
                print(f"✅ Completed component {components}\n")
        
        return components


# ============================================================
# 2) Breadth First Search (Queue) — Level-order Exploration
#    Time: O(V+E) | Space: O(V+E)
# ============================================================
class SolutionBFS:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * n
        components = 0
        
        def bfs(start_node: int) -> None:
            """Explore entire connected component using BFS"""
            queue = deque([start_node])
            visited[start_node] = True
            
            while queue:
                current = queue.popleft()
                print(f"  BFS processing node {current}")
                
                for neighbor in adj[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
                        print(f"    Added neighbor {neighbor} to queue")
        
        # Find connected components
        for node in range(n):
            if not visited[node]:
                print(f"🚨 Starting new component from node {node}")
                components += 1
                bfs(node)
                print(f"✅ Completed component {components}\n")
        
        return components


# ============================================================
# 3) Union-Find (Disjoint Set) — Efficient Connectivity
#    Time: O(V+E×α(V)) | Space: O(V)
# ============================================================
class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n
    
    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]
    
    def union(self, x: int, y: int) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            # Union by rank
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            self.components -= 1

class SolutionUnionFind:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        
        print(f"Initial: {n} components (each node isolated)")
        
        for u, v in edges:
            print(f"Processing edge ({u}, {v})")
            before = uf.components
            uf.union(u, v)
            after = uf.components
            if after < before:
                print(f"  Merged components! Components: {before} → {after}")
        
        print(f"Final: {uf.components} connected components")
        return uf.components


# ============================================================
# Active alias
# ============================================================
class Solution(SolutionDFS):
    """Uses DFS by default."""
    pass


# -----------------------------
# Graph Visualization Helpers
# -----------------------------
def build_adjacency_list(n: int, edges: List[List[int]]) -> List[List[int]]:
    """Build adjacency list from edges"""
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj

def visualize_graph(n: int, edges: List[List[int]], title: str = "") -> None:
    """Display graph structure with ASCII visualization"""
    print(f"\n--- {title} ---")
    
    # Build adjacency list for visualization
    adj = build_adjacency_list(n, edges)
    
    print(f"Graph with {n} nodes and {len(edges)} edges:")
    
    # Find connected components for visualization
    visited = [False] * n
    components = []
    
    def dfs_vis(node: int, component: List[int]) -> None:
        visited[node] = True
        component.append(node)
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs_vis(neighbor, component)
    
    for node in range(n):
        if not visited[node]:
            component = []
            dfs_vis(node, component)
            components.append(sorted(component))
    
    print(f"Connected Components: {len(components)}")
    for i, comp in enumerate(components):
        print(f"  Component {i+1}: {comp}")
    
    # Simple ASCII graph representation
    print("\nGraph Structure:")
    for i, comp in enumerate(components):
        if len(comp) == 1:
            print(f"  Component {i+1}: {comp[0]} (isolated)")
        else:
            # Show connections within component
            connections = set()
            for u in comp:
                for v in adj[u]:
                    if v in comp and u < v:  # Avoid duplicates in undirected graph
                        connections.add((u, v))
            
            if connections:
                edges_str = " — ".join([f"{u}-{v}" for u, v in sorted(connections)])
                print(f"  Component {i+1}: {edges_str}")
            else:
                print(f"  Component {i+1}: {comp} (disconnected?)")

def compare_approaches(n: int, edges: List[List[int]]) -> None:
    """Compare all three approaches on the same input"""
    print("\n" + "=" * 50)
    print("COMPARING ALL APPROACHES")
    print("=" * 50)
    
    approaches = [
        ("DFS", SolutionDFS().countComponents),
        ("BFS", SolutionBFS().countComponents),
        ("Union-Find", SolutionUnionFind().countComponents)
    ]
    
    for name, solver in approaches:
        print(f"\n{name} Approach:")
        print("-" * 30)
        result = solver(n, edges)
        print(f"Result: {result} components")

# -----------------------------
# Comprehensive Test Suite
# -----------------------------
def _run_tests() -> None:
    impls = [
        ("DFS", SolutionDFS().countComponents),
        ("BFS", SolutionBFS().countComponents),
        ("Union-Find", SolutionUnionFind().countComponents),
    ]

    TESTS: List[Tuple[int, List[List[int]], int, str]] = [
        # Example 1: Single component
        (
            3,
            [[0,1], [0,2]],
            1,
            "triangle-3-nodes"
        ),
        # Example 2: Two components
        (
            6,
            [[0,1], [1,2], [2,3], [4,5]],
            2,
            "two-chains"
        ),
        # All isolated nodes
        (
            5,
            [],
            5,
            "all-isolated"
        ),
        # Single node
        (
            1,
            [],
            1,
            "single-node"
        ),
        # Complex: Multiple components of different sizes
        (
            7,
            [[0,1], [1,2], [3,4], [4,5], [5,6]],
            2,
            "two-components-different-sizes"
        ),
        # Star pattern
        (
            5,
            [[0,1], [0,2], [0,3], [0,4]],
            1,
            "star-pattern"
        ),
        # Cycle
        (
            4,
            [[0,1], [1,2], [2,3], [3,0]],
            1,
            "cycle-4-nodes"
        ),
        # Mixed: isolated + connected
        (
            5,
            [[0,1], [2,3]],
            3,
            "mixed-isolated-connected"
        )
    ]

    VIS = {
        "triangle-3-nodes",
        "two-chains", 
        "two-components-different-sizes",
        "star-pattern",
        "mixed-isolated-connected"
    }

    passed = 0
    total = 0

    for i, (n, edges, expected, label) in enumerate(TESTS, 1):
        print(f"\n[{i:02d}][{label}]")
        
        if label in VIS:
            visualize_graph(n, edges, f"Graph: {label}")

        results = []
        for name, solver in impls:
            result = solver(n, edges)
            ok = (result == expected)
            results.append((name, result, ok))

        for name, result, ok in results:
            total += 1
            passed += ok
            status = "✅" if ok else "❌"
            print(f"  {name}: got={result} expected={expected} | {status}")

        agree = len({r[1] for r in results}) == 1
        print(f"  impls-agree: {'✅' if agree else '❌'}")

    print(f"\nPassed {passed}/{total} checks.")


# -----------------------------
# Educational Demonstration
# -----------------------------
def _demonstrate_approaches():
    """Show how each approach works step by step"""
    print("=" * 60)
    print("EDUCATIONAL DEMONSTRATION")
    print("=" * 60)
    
    # Simple example to demonstrate
    n = 6
    edges = [[0,1], [1,2], [2,3], [4,5]]
    
    visualize_graph(n, edges, "Demo Graph")
    
    print("\n" + "="*40)
    print("DFS APPROACH DEMONSTRATION")
    print("="*40)
    dfs_result = SolutionDFS().countComponents(n, edges)
    
    print("\n" + "="*40)
    print("BFS APPROACH DEMONSTRATION")
    print("="*40)
    bfs_result = SolutionBFS().countComponents(n, edges)
    
    print("\n" + "="*40)
    print("UNION-FIND APPROACH DEMONSTRATION") 
    print("="*40)
    uf_result = SolutionUnionFind().countComponents(n, edges)
    
    print(f"\nFinal Results:")
    print(f"DFS: {dfs_result}, BFS: {bfs_result}, Union-Find: {uf_result}")
    print(f"All agree: {dfs_result == bfs_result == uf_result}")


# -----------------------------
# Algorithm Analysis
# -----------------------------
def analyze_algorithms():
    """Compare the three approaches"""
    print("\n" + "=" * 60)
    print("ALGORITHM COMPARISON")
    print("=" * 60)
    
    print("""
DFS (Depth-First Search):
- Natural recursive exploration
- Follows paths as deep as possible before backtracking
- Good for: Simple implementation, low constant factors
- Watch out: Recursion depth for large graphs

BFS (Breadth-First Search):
- Level-order exploration  
- Explores all neighbors before going deeper
- Good for: Finding shortest paths, avoiding deep recursion
- Uses: Queue data structure

Union-Find (Disjoint Set):
- Efficient for dynamic connectivity queries
- Uses path compression and union by rank
- Good for: Incremental edge addition, very efficient
- Time: O(α(n)) per operation (inverse Ackermann)

WHEN TO USE WHICH:
- DFS/BFS: When you need to traverse the graph
- Union-Find: When you only care about connectivity
- DFS: Simpler code, less memory for deep graphs
- BFS: Better for finding shortest paths
""")


if __name__ == "__main__":
    _demonstrate_approaches()
    analyze_algorithms()
    _run_tests()