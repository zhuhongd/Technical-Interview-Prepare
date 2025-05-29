# Week 1 — Hash Maps & Hash Sets

> “If you’re stuck, try a hash table.”  
> — common interview meme (because it often works)

---

## 1. Why start with hashes?

- **Speed:**  
  Hash tables offer average-case O(1) lookup, insert, and delete. That means you can solve many brute-force problems in a single pass instead of nested loops.  
  [What is a Hash Table? (Interview Cake)](https://www.interviewcake.com/concept/python/hash-table)

- **Coverage:**  
  Out of Blind 75’s 75 most common interview questions, 8 are directly in the "Arrays & Hashing" category, which is over 10%.  
  [Blind 75: Arrays & Hashing](https://blind75.vercel.app/)  
  [NeetCode 150 - Arrays & Hashing](https://neetcode.io/practice)

- **Foundation for future weeks:**  
  Mastery here makes it easier to:
  - Use two-pointers in sorted arrays (Week 2)
  - Build sliding window techniques (Week 2)
  - Tackle prefix sum problems (this Week)  
  Hash maps and sets are used in most optimized solutions later.

---

## 2. Core properties & trade-offs

| Aspect        | Hash Map (`dict`)                 | Hash Set (`set`)            |
|---------------|-----------------------------------|-----------------------------|
| Stores        | key → value pairs                 | unique keys only            |
| Avg. ops      | **O(1)**                          | **O(1)**                    |
| Worst-case    | O(n) if heavy collisions occur    | O(n) if heavy collisions    |
| Strengths     | fast lookup, frequency counts, memoization | de-duping, membership tests  |
| Limitations   | higher memory, unordered          | unordered, no associated value |

*More: [Hash Tables in Python (Real Python)](https://realpython.com/python-hash-table/)*

---

## 3. Practice line-up & why these questions matter

| # | Problem (LeetCode)                  | Concept drilled         | Why interviewers love it                                                |
|---|-------------------------------------|------------------------|--------------------------------------------------------------------------|
| 1 | [Contains Duplicate (217)](https://leetcode.com/problems/contains-duplicate/) | set membership         | Teaches O(1) lookups and fast duplicate check, core to many interview warmups. |
| 2 | [Two Sum (1)](https://leetcode.com/problems/two-sum/)                       | map complement search  | Probably the most famous hash map question—used as an opener at FAANG interviews. |
| 3 | [Group Anagrams (49)](https://leetcode.com/problems/group-anagrams/)         | mapping & aggregation  | Shows real-world use of composite keys and collecting results by bucket.  |
| 4 | [Subarray Sum Equals K (560)](https://leetcode.com/problems/subarray-sum-equals-k/) | prefix sum + hash map  | Key bridge to advanced topics, combines cumulative sum with fast lookup.  |

---

## 4. Learning outcomes

By the end of Week 1, you should be able to:

1. **Explain** how a hash table achieves average O(1) performance and what causes slowdowns.
2. **Decide instantly** between using a dict or set for a new problem.
3. **Refactor** a brute-force double-loop into a hash-based solution.
4. **Recognize** when a problem needs frequency counting, fast duplicate check, or key→index mapping.

---

## 5. Skip test

Open `week1_skip_test.ipynb`.  
If you can solve [Contains Duplicate II (219)](https://leetcode.com/problems/contains-duplicate-ii/) in under 20 minutes with O(n) time and space, you can move to Week 2 early.

---

## 6. Further reading

- [NeetCode “Arrays & Hashing” playlist (YouTube)](https://www.youtube.com/playlist?list=PLot-Xpze53ldVwtstag2TL4HQhAnC8ATC)
- [Tech Interview Handbook: Hash Table Patterns](https://www.techinterviewhandbook.org/grind75)
- [Python Sets and Dictionaries (Official Docs)](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

---

**Next up:**  
Week 2 — Two-Pointers. You’ll see how to solve pair problems and range scans more efficiently, sometimes without any extra space.

Happy hashing!
