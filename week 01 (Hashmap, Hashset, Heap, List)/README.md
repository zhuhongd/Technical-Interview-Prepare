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

| # | Problem                                                                                     | Pattern / Concept                 | Why It’s Important                                                         |
|---|---------------------------------------------------------------------------------------------|-----------------------------------|-----------------------------------------------------------------------------|
| 1 | Contains Duplicate (LC 217)                                                                 | Set membership                    | Fast duplicate check with O(1) lookups.                                    |
| 2 | Valid Anagram / Is Anagram (LC 242)                                                         | Frequency map                     | Intro to counting patterns; basis for grouping & sliding window tricks.    |
| 3 | Two Sum (LC 1)                                                                              | Hash map complement search        | Canonical O(n²) → O(n) refactor.                                           |
| 4 | Group Anagrams (LC 49)                                                                      | Mapping & grouping (canonical key)| Aggregation by key; practice hashing compound structures.                  |
| 5 | Top K Frequent Elements (LC 347)                                                            | Map + heap / bucket sort          | Frequency + selection; segue into heaps/buckets.                           |
| 6 | Products of Array Except Self (LC 238)                                                      | Prefix products + hash alt        | Shows when hashes aren’t needed vs. when they can help (contrast exercise).|
| 7 | Longest Consecutive Sequence (LC 128)                                                       | Set membership + linear scan      | Classic O(n) trick with set; reinforces “seen” + boundary checks.          |
| 8 | Subarray Sum Equals K (LC 560)                                                              | Prefix sum + hash map             | Combines running totals with O(1) lookups—foundation for harder variants.  |

---

## 4. Learning outcomes

By the end of Week 1, you can:

1. **Justify** when a hash map vs. hash set is ideal (given a problem statement).  
2. **Transform** a nested-loop (O(n²)) solution into O(n) using hashes.  
3. **Explain** why average-case operations are O(1) and what breaks that.  
4. **Apply** prefix-sum + hash technique to count subarrays with a target property.

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
