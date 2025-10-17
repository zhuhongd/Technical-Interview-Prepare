# Week 7 — Heaps & Priority Queues (`heapq`)

> “A heap is a *half-sorted* structure: the root is always best, and fixing it is `O(log n)`.”

---

## 1. Big-Picture Concept

A **heap** is a binary tree stored in an array that guarantees the *heap property*:  
- **Min-heap (default in Python):** `heap[0]` is always the smallest element.  
- Insertions and deletions rebalance in `O(log n)` time.  

Python’s `heapq` module exposes a set of functions to use lists as min-heaps.

---

## 2. Heap Push (insert) — `heappush`

Push is `O(log n)`. The current minimum is always at `heap[0]` in `O(1)`.

```python
import heapq

heap = []                      # empty MIN-heap

heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
print(heap)                    # [1, 3]  (min at index 0)
print(heap[0])                 # 1

heapq.heappush(heap, 0)
print(heap)                    # [0, 3, 1] (heap shape, not sorted)
print(heap[0])                 # 0
```

## 3. Heap Pop (extract-min) — `heappop`

Removes and returns the **smallest element** in `O(log n)`.

```python
import heapq

heap = []
for x in [5, 2, 7, 1]:
    heapq.heappush(heap, x)

print([heapq.heappop(heap) for _ in range(len(heap))])
# [1, 2, 5, 7]
```
⚠️ A heap is not a sorted array; only the root (heap[0]) is guaranteed to be the minimum.

## 4. Heapify (build from list) — heapify

Builds a valid heap in place in O(n) time.

```python
arr = [9, 4, 7, 1, 3]
heapq.heapify(arr)
print(arr)     # e.g. [1, 3, 7, 9, 4] (valid heap shape; min at index 0)
print(arr[0])  # 1
```

👉 Use heapify if you already have all elements. It’s faster than pushing one-by-one (O(n) vs O(n log n)).

## 5. Max-Heap (top = largest) — negation trick

Python’s heapq is min-heap only. To simulate a max-heap, push negative values.

```python

maxheap = []
for x in [5, 2, 7, 1]:
    heapq.heappush(maxheap, -x)   # store negatives

print(-maxheap[0])                # 7 (largest)

print(-heapq.heappop(maxheap))    # 7
print([-heapq.heappop(maxheap) for _ in range(len(maxheap))])
# [5, 2, 1]
```

## 6. Custom Heap (order by key) — store (priority, item) tuples

heapq has no key= argument. To prioritize by custom keys, push tuples where the first element is the priority.

Example A — order words by length

```python

words = ["pear", "fig", "banana", "kiwi", "grape"]
heap = []
for w in words:
    heapq.heappush(heap, (len(w), w))   # (priority = length, item = word)

out = [heapq.heappop(heap)[1] for _ in range(len(heap))]
print(out)  # ['fig', 'kiwi', 'pear', 'grape', 'banana']

Example B — order numbers by absolute value
nums = [7, -2, 5, -1, 3]
heap = []
for x in nums:
    heapq.heappush(heap, (abs(x), x))

print([heapq.heappop(heap)[1] for _ in range(len(heap))])
# [-1, -2, 3, 5, 7]
```

💡 For a max-heap on a key, negate the priority: (-key(x), x).

## 7. heapq.nsmallest — top-k smallest

Efficient when k is small relative to n. Complexity: O(n log k).

```python

nums = [9, 4, 7, 1, 3, 6]
print(heapq.nsmallest(3, nums))          # [1, 3, 4]

people = [
    {"name":"Ana","age":29},
    {"name":"Bob","age":31},
    {"name":"Eve","age":24}
]
print(heapq.nsmallest(2, people, key=lambda p: p["age"]))
# [{'name': 'Eve', 'age': 24}, {'name': 'Ana', 'age': 29}]
```

## 8. heapq.nlargest — top-k largest

Mirror of nsmallest.

```python
nums = [9, 4, 7, 1, 3, 6]
print(heapq.nlargest(2, nums))           # [9, 7]

words = ["pear", "fig", "banana", "kiwi", "grape"]
print(heapq.nlargest(3, words, key=len))
# ['banana', 'grape', 'pear']
```

## 9. Bonus One-Liners

```python
Peek min: heap[0]

Push then pop (optimized): heapq.heappushpop(heap, x)

Pop then push (replace top): heapq.heapreplace(heap, x)

heap = [1, 3, 5]; heapq.heapify(heap)

print(heapq.heappushpop(heap, 2))  # returns 1, heap = [2, 3, 5]
print(heapq.heapreplace(heap, 4))  # pops 2, pushes 4 → returns 2, heap = [3, 4, 5]
```

---

## 10. When to Use a Heap vs. Alternatives

| Goal                          | Best Tool                                | Why                                                                 |
|-------------------------------|------------------------------------------|---------------------------------------------------------------------|
| **kth largest / smallest**    | Min-heap of size k / Max-heap of size k  | O(n log k), works well in streaming scenarios.                      |
| **Top-k items**               | Heap (`nsmallest` / `nlargest`)          | Built-in helpers support custom key functions efficiently.           |
| **Streaming kth largest**     | Min-heap of size k                       | Each new element updates in O(log k).                               |
| **Pick next by priority**     | Heap                                     | Every extraction in O(log n); ideal for scheduling and simulations. |
| **Single kth selection**      | Quickselect (avg O(n))                   | Faster than heap if you only need one result.                       |
| **Just need overall min/max** | Built-in `min` / `max`                   | O(n) once; no need for extra structure.                             |

---

## 11. Problem Patterns (Mapped to Week 11 Files)

| #  | File                                   | Pattern               | Key Idea                                                             |
|----|----------------------------------------|-----------------------|----------------------------------------------------------------------|
| 1  | **Kth Largest Element in a Stream**    | k-size min-heap       | Maintain top-k; the root is the kth largest after each insertion.    |
| 2  | **Last Stone Weight**                  | max-heap (negation)   | Pop two heaviest, push back difference if nonzero.                   |
| 3  | **Closest Points to Origin**           | k-size max-heap OR QS | Compare squared distances; keep k closest or Quickselect once.       |
| 4  | **Kth Largest Element in an Array**    | Quickselect / k-heap  | One-shot query → Quickselect preferred; heap if multiple queries.    |
| 5  | **Task Scheduler**                     | math frame OR heap sim| Frames formula `(f_max-1)*(n+1)+m` vs simulate with heap & cooldown. |
| 6  | **Car Pooling**                        | diff array / sweep    | Use +p at start, −p at end; or min-heap sorted by drop-off time.     |

---

## 12. Complexity Recap

| Operation                  | Time Complexity |
|-----------------------------|-----------------|
| **`heapq.heapify(list)`**  | O(n)            |
| **`heappush` / `heappop`** | O(log n)        |
| **`heappushpop` / `heapreplace`** | O(log n) |
| **`nsmallest` / `nlargest`** | O(n log k)   |

---

## 13. Learning Outcomes

By the end of this Heap / Priority Queue module, you should be able to:

1. **Recognize** when to use a heap over alternatives (quickselect, sort, min/max).  
2. **Implement** heap-based solutions with Python’s `heapq` (push, pop, heapify, nlargest/nsmallest).  
3. **Simulate** max-heaps and custom priority queues using negation or decorated tuples.  
4. **Apply** heap patterns to real interview problems like:
   - **Top-k elements** (streaming or batch).  
   - **Greedy scheduling** (Task Scheduler).  
   - **Simulation** (Last Stone Weight).  
   - **Resource allocation** (Car Pooling).  
5. **Analyze** trade-offs:  
   - Heaps = great for *repeated priority access*.  
   - Quickselect = great for *one-time kth query*.  
   - Sort = simplest when you need full order.

---

## 14. Skip Test

You’re ready to move on if you can:  

- Implement **Kth Largest Element in a Stream** using a k-size min-heap.  
- Explain why `heapify` is O(n) while repeated `heappush` is O(n log n).  
- Derive the **Task Scheduler frame formula** and validate it with a heap-based simulation.  

If you can solve these in ≤ 40 minutes with clear reasoning, heaps are in your toolkit.

---

**Next:** Week 12 — OOP Design Patterns. We’ll shift gears from data structures to **class design and extensibility**.
