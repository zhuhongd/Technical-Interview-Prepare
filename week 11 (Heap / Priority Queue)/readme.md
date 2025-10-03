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

## 8. heapq.nlargest — top-k largest

Mirror of nsmallest.

nums = [9, 4, 7, 1, 3, 6]
print(heapq.nlargest(2, nums))           # [9, 7]

words = ["pear", "fig", "banana", "kiwi", "grape"]
print(heapq.nlargest(3, words, key=len))
# ['banana', 'grape', 'pear']

## 9. Bonus One-Liners

Peek min: heap[0]

Push then pop (optimized): heapq.heappushpop(heap, x)

Pop then push (replace top): heapq.heapreplace(heap, x)

heap = [1, 3, 5]; heapq.heapify(heap)

print(heapq.heappushpop(heap, 2))  # returns 1, heap = [2, 3, 5]
print(heapq.heapreplace(heap, 4))  # pops 2, pushes 4 → returns 2, heap = [3, 4, 5]
```