# Week 1 — Hash Maps & Hash Sets

> “If you’re stuck, try a hash table.”  
> — common interview meme (because it often works)

---

## 1. Why start with Hash Maps and Hash Sets?

Hash maps (`dict`) and hash sets (`set`) are **core data structures** for interview prep. They appear in countless problems involving:

- **Uniqueness**: “Has this been seen before?”
- **Counting**: “How many times does X appear?”
- **Frequency/grouping**: “Group all anagrams,” “Track frequency,” etc.
- **Membership**: “Is X present?”

When you see words like *unique*, *duplicate*, *count*, *frequency*, or *seen*, a hash map or set is often the optimal solution.

**If you only had one “trick” for interviews, knowing how and when to use hashes is it!**

---

## 2. Why Hashes over Arrays or TreeMaps?

| Operation        | TreeMap (BST) | HashMap      | Array       |
|------------------|---------------|--------------|-------------|
| Insert           | O(log n)      | O(1)\*       | O(n)        |
| Remove           | O(log n)      | O(1)\*       | O(n)        |
| Search           | O(log n)      | O(1)\*       | O(n)        |
| Ordered Traversal| O(n)          | ❌ Unordered | ❌ Unordered |

\*Hash maps are **average-case O(1)**, but can degrade to O(n) with poor hash functions or heavy collisions. In interviews, assume average-case.

- **HashMap**: Fastest for lookup, insert, remove (on average).  
- **TreeMap**: Maintains order, but is slower for most tasks.  
- **Array**: Fine for static, sorted data, but slow for dynamic lookup/insert.

**Key takeaway:** For problems where order doesn’t matter but speed does, hashes are almost always best.

---

## 3. Key Concepts

- **Hash Map**: Stores key-value pairs (`{name: count}`)
- **Hash Set**: Stores unique keys only (`{name, name, ...}`)
- **No duplicates** (for keys)
- **O(1)** average-case for insert, lookup, and delete
---

## 3. Practice line-up & why these questions matter

| # | Problem                                                                                | Concept Drilled            | Why It's Important                                                                      |
| - | -------------------------------------------------------------------------------------- | -------------------------- | --------------------------------------------------------------------------------------- |
| 1 | [Contains Duplicate (LC 217)](https://leetcode.com/problems/contains-duplicate/)       | Set membership             | The fastest way to check for duplicates using O(1) lookups.                             |
| 2 | [Two Sum (LC 1)](https://leetcode.com/problems/two-sum/)                               | Hash map complement search | Turns O(n²) brute-force into O(n) elegance; the most common interview question.         |
| 3 | [Group Anagrams (LC 49)](https://leetcode.com/problems/group-anagrams/)                | Mapping and grouping       | Efficiently groups items by key, teaches aggregation with hash maps.                    |
| 4 | [Subarray Sum Equals K (LC 560)](https://leetcode.com/problems/subarray-sum-equals-k/) | Prefix sum + hash map      | Combines prefix logic and fast lookups; leads to more advanced patterns in later weeks. |


---

## 4. Learning outcomes

By the end of Week 1, you should be able to:

1. **Explain** how a hash table achieves average O(1) performance and what causes slowdowns.
2. **Decide instantly** between using a dict or set for a new problem.
3. **Refactor** a brute-force double-loop into a hash-based solution.
4. **Recognize** when a problem needs frequency counting, fast duplicate check, or key→index mapping.

---

## 5. Skip test

Solve Top K Frequent Elements (LC 347) with the optimal O(n log k) (map + heap) or O(n) (bucket sort) approach in ≤ 25 min.
https://leetcode.com/problems/top-k-frequent-elements/
---

## 6. Further reading

- [Tech Interview Handbook: Hash Table Patterns](https://www.techinterviewhandbook.org/grind75)
- [Python Sets and Dictionaries (Official Docs)](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

---

**Next up:**  
Week 2 — Two-Pointers and Slicing Windows. You’ll see how to solve pair problems and range scans more efficiently, sometimes without any extra space.

Happy hashing!
