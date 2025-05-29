# Week 1 — HashMap & HashSet Fundamentals

Welcome to the **foundation week** of the study plan.  
Hash-based structures are the “Swiss-army knife” of technical interviews: they give O(1) average-time look-ups and form the backbone of classic questions like **Two Sum**, **Group Anagrams**, and **Subarray Sum = K**.

*In the Blind 75 alone, at least 7 of 75 problems (≈ 9 %) hinge on a hash map or set, and they appear in 14+ entries of LeetCode’s Top Interview 150 list.* :contentReference[oaicite:0]{index=0}  

---

## 🎯 Learning Goals
| Goal | How we’ll measure it |
|------|----------------------|
|Recall average/worst-case Big-O for hash tables|Answer quiz in `hashmap_set_notes.ipynb` |
|Choose between `set()` and `dict()` in Python on sight|Pass mini-challenge #1 |
|Refactor a brute-force O(n²) pair search to O(n) with a map|Complete **Contains Duplicate II** in under 15 min |

---

## 🗺️ Why start with Hashes?

| Strength | Limitation |
|----------|------------|
|O(1) avg. insert/lookup/delete thanks to direct indexing :contentReference[oaicite:1]{index=1}|Can degrade to O(n) with poor hash or heavy collisions :contentReference[oaicite:2]{index=2}|
|Built-in in every major language ⇒ minimal boilerplate|Higher memory overhead vs. arrays |
|Perfect for frequency counts, de-duping, memoization :contentReference[oaicite:3]{index=3}|Unordered → can’t rely on element order without extra work|

Hash maps/sets also unlock the **Two-Pointers ➜ Sliding Window ➜ Prefix Sum** ladder we’ll climb in Weeks 2-4, so mastering them early compounds your speed later.

---

## 📝 This Week’s Checklist

| File | Purpose |
|------|---------|
|`hashmap_set_notes.ipynb`|Concept recap, Big-O quiz |
|`week1_practice.ipynb`|Walk-through + code templates for: Contains Duplicate, Two Sum, Group Anagrams |
|`week1_skip_test.ipynb`|🚦 **Skip-challenge** — solve *Contains Duplicate II* (optimal O(n) / O(n)) |

If you clear the skip-challenge in < 20 min and can explain the trade-offs, jump ahead to Week 2.

---

## 🔢 Interview-Frequency Snapshot  

| Rank | Pattern / DS | Why it matters |
|------|--------------|----------------|
|1 | Array & Hashing | Hash map tricks solve Two Sum, 3Sum, etc. :contentReference[oaicite:4]{index=4}|
|2 | Two Pointers | Cuts nested loops to O(n); headline of Week 2 :contentReference[oaicite:5]{index=5}|
|3 | Sliding Window | Builds on ptr indices for sub-array problems |
|4 | Prefix / Running Sum | Fast cumulative queries |
|5 | Binary Search | Log-time divide & conquer |
|6 | Linked-List Ops | Pointers, cycles, merges |
|7 | Tree Traversals | DFS/BFS variants |
|8 | Graph BFS/DFS | Connectivity, shortest path |
|9 | 1-D DP | Knapsack, House Robber |
|10| Heap / PQ | Top-K, stream medians |

(The ranking aggregates patterns recurring in Blind 75, Grind 75, and Top Interview 150.) :contentReference[oaicite:6]{index=6}

---

## 📚 Further Reading
* Tech Interview Handbook — Hash-Table cheatsheet (practice set + pitfalls) :contentReference[oaicite:7]{index=7}  
* Geeks-for-Geeks guide to two-pointer problems (peek at Week 2) :contentReference[oaicite:8]{index=8}  
* interviewing.io article on “Hash Tables vs Arrays vs Sets” for nuanced trade-offs :contentReference[oaicite:9]{index=9}  

---

## ⏭ Up Next — Week 2: Two Pointers

We’ll reuse the hash-table tricks from this week to refactor brute-force pair scans into elegant O(n) solutions and introduce the sliding-window template.

Happy hashing! ✌️