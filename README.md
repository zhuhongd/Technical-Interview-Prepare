# Technical-Interview-Prepare
A structured project for Summer 2025 to prepare for technical interviews, including completing LeetCode question sets and documenting problem-solving approaches as part of EECS4070.

# Week 1 -> Week 2:

In Week 1, you practiced using `HashSet`, `HashMap`, and counting frequencies. These skills are very useful for solving Two Pointer and Sliding Window problems in Week 2. Here's how they connect:

---

### 1. HashSet → Used in Two Pointer problems

- In **"Longest Substring Without Repeating Characters"**, you need to check if a character is already in your current substring.
- You can use a `HashSet` to store characters in the current window.
- If the character is already in the set, move the left pointer forward and remove characters until the duplicate is gone.
- This only works well if you're comfortable with using `set.add()`, `set.remove()`, and checking membership with `in`, which you practiced in Week 1.

---

### 2. HashMap → Used in Sliding Window with character counts

- In **"Minimum Window Substring"**, you need to find a substring that contains all the characters from another string.
- You build a `HashMap` with the frequency of each required character.
- Then, as you slide the window, you update another `HashMap` for the current window and compare the counts.
- In Week 1, the **"Top K Frequent Elements"** problem helped you get used to counting frequencies and updating maps as you go.

---

### 3. Time complexity and avoiding brute force

- In Week 1, you learned to use `HashMap` and `HashSet` to avoid unnecessary loops.
- For example, instead of checking every possible substring, you learned to process the input once using a set or map.
- This idea is exactly what Sliding Window does — you move two pointers instead of looping over everything.

---

### Example Summary:

| Concept from Week 1 | How it's used in Week 2                          | Example Problem                            |
|---------------------|--------------------------------------------------|--------------------------------------------|
| `HashSet`           | Track seen characters to avoid duplicates        | Longest Substring Without Repeating Characters |
| `HashMap`           | Count required characters and match them         | Minimum Window Substring                   |
| Frequency Counting  | Track how many times each element appears        | Top K Frequent Elements → used in sliding window too |

---

### TLDR:

The set and map problems in Week 1 are not just warm-ups — they give you the tools you need to write fast and clean solutions using two pointers and sliding windows in Week 2.

