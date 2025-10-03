# Week 10 — Graphs (DFS / BFS / Union-Find)

> “Graphs are just nodes + edges — but the patterns unlock whole worlds: maps, networks, scheduling, connectivity.”

---

## 1. Big-Picture Concept

A **graph** is a collection of **vertices (nodes)** connected by **edges**.  
Edges can be:

- **Directed** (one-way link, like a Twitter follow).
- **Undirected** (two-way link, like a Facebook friendship).
- **Weighted** (edge carries a cost, distance, or capacity).
- **Unweighted** (edge = existence of connection only).

Graphs are represented in three main ways:

1. **Adjacency List**  
   ```python
   graph = {
       0: [1, 2],
       1: [0, 3],
       2: [0],
       3: [1]
   }
    ```
→ Compact, good for sparse graphs.

2. **Adjacency Matrix**
    ```python
    # 4 nodes, undirected
    M = [
    [0,1,1,0],
    [1,0,0,1],
    [1,0,0,0],
    [0,1,0,0]
    ]
    ```
→ Easy edge lookup, but O(n²) space.

3. **Edge List**
```python
edges = [(0,1), (0,2), (1,3)]
```
→ Simple storage, often used in union-find.

## 2. Core Traversal Patterns

| Pattern              | Description                                       | Use-cases                                              |
|----------------------|---------------------------------------------------|--------------------------------------------------------|
| **DFS (Depth-First)** | Dive deep via recursion/stack before backtracking. | Connected components, cycle detection, path existence. |
| **BFS (Breadth-First)** | Explore level by level using a queue.             | Shortest path in unweighted graph, spreading processes.|
| **Union-Find (DSU)**   | Disjoint Set Union with path compression.         | Detect cycles, connected components, Kruskal’s MST.    |

### DFS Recursive
```python
def dfs(node, visited, graph):
    if node in visited: 
        return
    visited.add(node)
    for nei in graph[node]:
        dfs(nei, visited, graph)
```

### BFS Iterative
```python
from collections import deque

def bfs(start, graph):
    q = deque([start])
    visited = {start}
    while q:
        node = q.popleft()
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)
```

## 3. Classic Interview Problems

- **Islands** → Grid problems (2D matrix) are implicit graphs: each cell is a node, neighbors = up/down/left/right.  
- **Cloning** → Copying structures while tracking visited nodes.  
- **Rotting Oranges / Spread** → BFS simulates time-based spreading.  
- **Connectivity** → Count connected components (Union-Find or DFS).  
- **Word Ladder** → Shortest path in an implicit word-graph.  

---

## 4. Complexity Cheat-Sheet

- **DFS/BFS Traversal** → `O(V + E)` (vertices + edges)  
- **Union-Find** → ~`O(α(n))` per operation (inverse Ackermann; nearly constant)  
- **Grid DFS/BFS** → `O(m*n)` for `m × n` matrix  
- **Adjacency Matrix BFS/DFS** → `O(V²)`  

---

## 5. Practice Line-up & Why These Matter (✅ mapped to your folder)

| #  | Problem (LeetCode)                                       | Pattern              | Interview Takeaway |
|----|----------------------------------------------------------|----------------------|--------------------|
| 1  | **Number of Islands** (#200)                             | DFS/BFS on grid      | Basic flood-fill; template for grid traversal. |
| 2  | **Max Area of Island** (#695)                            | DFS with area count  | Extend flood-fill with aggregation logic. |
| 3  | **Clone Graph** (#133)                                   | DFS/BFS with hashmap | Avoid infinite loops by memoizing clones. |
| 4  | **Islands and Treasure** (#286)                          | Multi-source BFS     | BFS from all gates at once; shortest distance fill. |
| 5  | **Rotting Fruit (Oranges)** (#994)                       | BFS with time layers | “Multi-round BFS” simulates spreading over time. |
| 6  | **Number of Connected Components in an Undirected Graph** (#323) | DFS / Union-Find  | Count CCs; builds intuition for network problems. |
| 7  | **Word Ladder** (#127)                                   | BFS on word graph    | Classic shortest transformation path; implicit edges. |

## 6. Learning Outcomes

By the end of this module, you will be able to:

- Translate **matrices into graphs** (e.g., islands, rotting fruit).  
- Implement **DFS/BFS templates** for connectedness, traversal, and shortest path.  
- Recognize when to use **Union-Find** for connectivity problems.  
- Apply **multi-source BFS** for simultaneous spread simulations.  
- Handle **implicit graphs** (e.g., Word Ladder edges aren’t explicitly listed).  

---

## 7. Skip Test ✅

You can safely skip this module if you can confidently:

- Implement **Number of Islands** with both DFS and BFS.  
- Explain why **Word Ladder requires BFS** (not DFS).  
- Choose between **Union-Find vs DFS** for Connected Components.  

👉 If yes, you’ve mastered the **core graph toolkit**.

---

## 8. Further Reading & Visualizers 📚

- [Tech Interview Handbook — Graph Patterns](https://www.techinterviewhandbook.org/algorithms/graph)  
- [VisuAlgo — Graph Traversals](https://visualgo.net/en/dfsbfs)  
- [Union-Find DSU Explained](https://cp-algorithms.com/data_structures/disjoint_set_union.html)  
- [MIT 6.006 — Graphs and Shortest Paths Notes](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/pages/lecture-notes/)  

---

## 👉 Next: Week 11 — Heaps & Priority Queues

We now **shift from exploring connections (graphs)** to **ranking priorities (heaps)**.
