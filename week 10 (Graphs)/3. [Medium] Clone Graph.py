from typing import Optional, Dict, List
from collections import deque

"""
Clone Graph — EECS4070 (Multiple Approaches) + Graph Visualization

Problem
-------
Given a reference node in a connected undirected graph, return a deep copy of the entire graph.
Each node in the graph contains:
- val: integer value
- neighbors: list of neighboring Node objects

Key Examples
------------
Example 1:
Input: adjList = [[2],[1,3],[2]]
Output: [[2],[1,3],[2]]
Explanation: 
  1 —— 2 —— 3
  ↻     ↻

Example 2:
Input: adjList = [[]]
Output: [[]]
Explanation: Single node with no neighbors

Example 3:
Input: adjList = []
Output: []
Explanation: Empty graph

What the grader expects
-----------------------
• Create entirely new Node objects (deep copy)
• Preserve the exact graph structure and connections
• Handle empty graph and single node cases
• Maintain the same neighbor relationships

Beginner Intuition
------------------
Think of "mapping" each original node to its copy:
1) When we encounter a new node, create its copy
2) When we encounter a node we've seen, use the existing copy
3) Connect the copies in the same pattern as originals

Tiny Visuals
------------
Original Graph:     Cloned Graph:
   1 —— 2              1'—— 2'
    ↻    ↻             ↻     ↻
          3                   3'

Thinking Process (step-by-step)
-------------------------------
We need to traverse the entire graph while creating copies:
- Use a dictionary to map original nodes → copied nodes
- For each node we visit:
  * If we haven't seen it, create a copy and add to dictionary
  * Copy all neighbors (creating them if necessary)
  * Connect the copies appropriately

Approaches (exactly what you asked for)
---------------------------------------
1) Depth-First Search (Recursive)
   - Natural for graph traversal
   - Time O(V+E), Space O(V) for recursion + dictionary

2) Breadth-First Search (Queue)
   - Level-order exploration
   - Time O(V+E), Space O(V) for queue + dictionary

Why this works
--------------
The dictionary ensures each original node maps to exactly one copy,
preventing duplicates and maintaining the graph structure.

Common Pitfalls
---------------
• Forgetting to handle the empty graph case
• Creating multiple copies of the same node
• Not properly connecting the neighbor relationships
• Missing the circular references in undirected graphs

Complexity Summary
------------------
Let V = number of vertices (nodes), E = number of edges
• Time  : O(V+E) — we visit each node and each edge once
• Space : O(V) — for the dictionary mapping original→copy
"""


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List['Node']] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __repr__(self) -> str:
        return f"Node({self.val})"

    def __hash__(self):
        return id(self)

    def __eq__(self, other):
        return id(self) == id(other)


# ============================================================
# 1) Depth First Search (Recursive) — Most Intuitive
#    Time: O(V+E) | Space: O(V)
# ============================================================
class SolutionDFS:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        old_to_new: Dict[Node, Node] = {}
        
        def dfs(original: Node) -> Node:
            """Recursive DFS that clones the graph"""
            # If we've already cloned this node, return the clone
            if original in old_to_new:
                return old_to_new[original]
            
            print(f"DFS: Creating copy of Node({original.val})")
            
            # Create copy of current node
            copy = Node(original.val)
            old_to_new[original] = copy
            
            # Recursively clone all neighbors
            for neighbor in original.neighbors:
                copy.neighbors.append(dfs(neighbor))
                print(f"  Node({copy.val}) connected to Node({neighbor.val})")
            
            return copy
        
        return dfs(node)


# ============================================================
# 2) Breadth First Search (Queue) — Level-order Exploration
#    Time: O(V+E) | Space: O(V)
# ============================================================
class SolutionBFS:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        old_to_new: Dict[Node, Node] = {}
        
        # Create copy of the starting node
        old_to_new[node] = Node(node.val)
        queue = deque([node])
        
        print(f"BFS: Starting with Node({node.val})")
        
        while queue:
            current = queue.popleft()
            print(f"BFS: Processing Node({current.val})")
            
            # Clone all neighbors
            for neighbor in current.neighbors:
                if neighbor not in old_to_new:
                    # First time seeing this neighbor - create copy
                    print(f"  Creating copy of Node({neighbor.val})")
                    old_to_new[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
                # Connect the copies
                old_to_new[current].neighbors.append(old_to_new[neighbor])
                print(f"  Node({old_to_new[current].val}) connected to Node({old_to_new[neighbor].val})")
        
        return old_to_new[node]


# ============================================================
# Active alias (optional): pick DFS by default
# ============================================================
class Solution(SolutionDFS):
    """LeetCode-style single-class entry; uses recursive DFS by default."""
    pass


# -----------------------------
# Graph Building & Visualization Helpers
# -----------------------------
def build_graph_from_adjacency(adj_list: List[List[int]]) -> Optional[Node]:
    """
    Build a graph from adjacency list representation.
    Nodes are 1-indexed: node with val=1 is at index 0, etc.
    """
    if not adj_list:
        return None
    
    # Create all nodes first
    nodes = {}
    for i in range(1, len(adj_list) + 1):
        nodes[i] = Node(i)
    
    # Connect neighbors
    for i, neighbors in enumerate(adj_list, 1):
        for neighbor_val in neighbors:
            nodes[i].neighbors.append(nodes[neighbor_val])
    
    return nodes[1]  # Return the first node (val=1)

def graph_to_adjacency(node: Optional[Node]) -> List[List[int]]:
    """
    Convert graph back to adjacency list representation.
    """
    if not node:
        return []
    
    visited = set()
    adjacency_dict = {}
    
    def dfs(current: Node):
        if current in visited:
            return
        
        visited.add(current)
        adjacency_dict[current.val] = [neighbor.val for neighbor in current.neighbors]
        
        for neighbor in current.neighbors:
            dfs(neighbor)
    
    dfs(node)
    
    # Convert to sorted adjacency list
    max_val = max(adjacency_dict.keys())
    adjacency_list = [[] for _ in range(max_val)]
    
    for val, neighbors in adjacency_dict.items():
        adjacency_list[val-1] = sorted(neighbors)
    
    return adjacency_list

def visualize_graph(node: Optional[Node], title: str = "") -> None:
    """Display graph structure with ASCII visualization"""
    print(f"\n--- {title} ---")
    if not node:
        print("Empty graph")
        return
    
    visited = set()
    edges = set()
    
    def collect_info(current: Node):
        if current in visited:
            return
        visited.add(current)
        
        for neighbor in current.neighbors:
            # Store edges in sorted order to avoid duplicates in undirected graph
            edge = tuple(sorted([current.val, neighbor.val]))
            edges.add(edge)
            collect_info(neighbor)
    
    collect_info(node)
    
    print("Graph Structure:")
    nodes_sorted = sorted([node.val for node in visited])
    print(f"Nodes: {nodes_sorted}")
    print(f"Edges: {sorted(edges)}")
    
    # Simple ASCII visualization
    print("\nASCII Representation:")
    for edge in sorted(edges):
        if len(edge) == 2:
            if edge[0] == edge[1]:
                print(f"  {edge[0]} —— {edge[1]} (self-loop)")
            else:
                print(f"  {edge[0]} —— {edge[1]}")
        else:
            print(f"  {edge[0]} (isolated)")

def compare_graphs(original: Optional[Node], clone: Optional[Node]) -> bool:
    """Compare if two graphs have the same structure"""
    if not original and not clone:
        return True
    if not original or not clone:
        return False
    
    original_adj = graph_to_adjacency(original)
    clone_adj = graph_to_adjacency(clone)
    
    return original_adj == clone_adj


# -----------------------------
# Comprehensive Test Suite
# -----------------------------
def _run_tests() -> None:
    impls = [
        ("DFS", SolutionDFS().cloneGraph),
        ("BFS", SolutionBFS().cloneGraph),
    ]

    TESTS: List[Tuple[List[List[int]], List[List[int]], str]] = [
        # Example 1: 1-2-3
        (
            [[2], [1, 3], [2]],
            [[2], [1, 3], [2]],
            "linear-3-nodes"
        ),
        # Example 2: Single node
        (
            [[]],
            [[]],
            "single-node"
        ),
        # Example 3: Empty graph
        (
            [],
            [],
            "empty-graph"
        ),
        # Cycle: 1-2-3-1
        (
            [[2, 3], [1, 3], [1, 2]],
            [[2, 3], [1, 3], [1, 2]],
            "triangle-cycle"
        ),
        # Star: 1 connected to 2,3,4
        (
            [[2, 3, 4], [1], [1], [1]],
            [[2, 3, 4], [1], [1], [1]],
            "star-graph"
        ),
        # Two disconnected components (shouldn't happen in connected graph, but good test)
        (
            [[2], [1], [4], [3]],
            [[2], [1], [4], [3]],
            "two-components"
        ),
        # Complex graph
        (
            [[2, 3], [1, 4], [1, 4], [2, 3]],
            [[2, 3], [1, 4], [1, 4], [2, 3]],
            "complex-4-node"
        )
    ]

    VIS = {
        "linear-3-nodes",
        "triangle-cycle", 
        "star-graph",
        "complex-4-node"
    }

    passed = 0
    total = 0

    for i, (input_adj, expected_adj, label) in enumerate(TESTS, 1):
        print(f"\n[{i:02d}][{label}]")
        
        if label in VIS and input_adj:
            original_graph = build_graph_from_adjacency(input_adj)
            visualize_graph(original_graph, f"Original: {label}")

        results = []
        for name, solver in impls:
            # Build original graph and clone it
            original_graph = build_graph_from_adjacency(input_adj)
            cloned_graph = solver(original_graph)
            
            # Convert back to adjacency list for comparison
            result_adj = graph_to_adjacency(cloned_graph) if cloned_graph else []
            
            ok = (result_adj == expected_adj)
            results.append((name, result_adj, ok))
            
            if label in VIS and input_adj and ok:
                print(f"\n{name} cloned graph:")
                visualize_graph(cloned_graph, f"Clone ({name}): {label}")

        for name, result_adj, ok in results:
            total += 1
            passed += ok
            status = "✅" if ok else "❌"
            print(f"  {name} -> got={result_adj} expected={expected_adj} | {status}")

        agree = len({str(r[1]) for r in results}) == 1
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
    
    # Create a simple graph: 1 - 2 - 3
    print("Creating graph: 1 —— 2 —— 3")
    
    node1 = Node(1)
    node2 = Node(2) 
    node3 = Node(3)
    
    node1.neighbors = [node2]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2]
    
    visualize_graph(node1, "Original Graph")
    
    print("\n" + "="*40)
    print("DFS APPROACH DEMONSTRATION")
    print("="*40)
    dfs_clone = SolutionDFS().cloneGraph(node1)
    print("DFS cloning completed!")
    
    print("\n" + "="*40)
    print("BFS APPROACH DEMONSTRATION") 
    print("="*40)
    bfs_clone = SolutionBFS().cloneGraph(node1)
    print("BFS cloning completed!")
    
    # Verify both approaches produce correct results
    original_adj = graph_to_adjacency(node1)
    dfs_adj = graph_to_adjacency(dfs_clone)
    bfs_adj = graph_to_adjacency(bfs_clone)
    
    print(f"\nVerification:")
    print(f"Original: {original_adj}")
    print(f"DFS Clone: {dfs_adj}")
    print(f"BFS Clone: {bfs_adj}")
    print(f"DFS correct: {original_adj == dfs_adj}")
    print(f"BFS correct: {original_adj == bfs_adj}")


# -----------------------------
# Advanced: Graph Analysis
# -----------------------------
def analyze_graph_properties(node: Optional[Node]) -> Dict:
    """Analyze various properties of the graph"""
    if not node:
        return {"nodes": 0, "edges": 0, "is_connected": True}
    
    visited = set()
    edges = set()
    nodes = set()
    
    def dfs(current: Node):
        if current in visited:
            return
        visited.add(current)
        nodes.add(current.val)
        
        for neighbor in current.neighbors:
            edge = tuple(sorted([current.val, neighbor.val]))
            edges.add(edge)
            dfs(neighbor)
    
    dfs(node)
    
    return {
        "nodes": len(nodes),
        "edges": len(edges),
        "is_connected": len(visited) == len(nodes),
        "node_values": sorted(nodes),
        "edge_pairs": sorted(edges)
    }


if __name__ == "__main__":
    _demonstrate_approaches()
    _run_tests()