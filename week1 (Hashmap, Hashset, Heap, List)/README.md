# Week 1 – Hash Maps & Hash Sets

> “If you get stuck, throw a hash map at it.”  
> — common interview meme (because it often works)

## 1. Why start with hashes?

* **Speed** Average‐case lookup / insert / delete is **O(1)**, thanks to direct indexing via a hash function. :contentReference[oaicite:0]{index=0}  
* **Coverage** The *Arrays & Hashing* category alone holds **8 of 75** problems in the Blind 75 list (~11 %). :contentReference[oaicite:1]{index=1}  
* **Foundation for later weeks**  
  * **Two-Pointers** (Week 2) – when an array is sorted, `Two Sum` can be refactored from a hash-map solution to two pointers.  
  * **Sliding Window** (Week 3) – a set tracks “currently-seen” elements to maintain a window with no repeats.  
  * **Prefix Sum + HashMap** (Week 4) – uses a map of *prefix→index* for constant-time range queries.

---

## 2. Core properties

| Aspect | Hash Map (`dict`) | Hash Set (`set`) |
|--------|------------------|------------------|
| Stores | key → value pairs | unique keys only |
| Avg. ops | O(1) | O(1) |
| Worst case | O(n) if many collisions | same |
| Strengths | direct lookup, counting, memo-cache | deduping, membership tests |
| Limitations | higher memory; unordered | unordered; no values |

---

## 3. Practice problems & **why** they were picked

| # | Problem (LeetCode ID) | Concept it drills | Why it matters | Citations |
|---|-----------------------|-------------------|----------------|-----------|
| 1 | **Contains Duplicate** (217) | set membership | Simplest “do I see this again?” check—introduces `set()` syntax and O(1) lookups | :contentReference[oaicite:2]{index=2} |
| 2 | **Two Sum** (1) | map complement search | Classic interview opener; shows how a hash map drops brute-force from O(n²) → O(n) | :contentReference[oaicite:3]{index=3} |
| 3 | **Group Anagrams** (49) | map of canonical key → list | Demonstrates building composite keys and aggregation with a map | :contentReference[oaicite:4]{index=4} |
| 4 | **Subarray Sum = K** (560) | prefix-sum + map | Bridges to Week 4; illustrates storing prefix frequencies to count ranges in O(n) | :contentReference[oaicite:5]{index=5} |

*(Solve these in `week1_practice.ipynb`.  Each file has a starter template and walkthrough.)*

---

## 4. Learning outcomes

By Friday you should be able to:

1. **Explain** how a hash table achieves amortised O(1) and when it degrades to O(n).  
2. **Choose** between `dict` and `set` instantly.  
3. **Refactor** a double-loop search to a one-pass map solution (e.g., `Two Sum`).  
4. **Write** frequency-count, deduping, and prefix-sum patterns from memory.  

---

## 5. Skip-test

Open **`week1_skip_test.ipynb`**.  
If you can solve *Contains Duplicate II* (LC 219) in < 20 minutes with an optimal O(n) / O(n) solution **and** justify the complexity, you may jump to Week 2.

---

Next up → **Week 2: Two Pointers.**  You’ll see how sorting plus dual indices can replace a hash map for range searches, and how that leads naturally into the Sliding Window pattern.

Happy hashing! 🗝️
