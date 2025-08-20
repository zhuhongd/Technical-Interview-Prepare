# Week 6 — Stacks

> “When the solution depends on remembering what you've recently seen, reach for a stack.”  
> — Essential LeetCode insight

---

## 1. Why Stacks?

Stacks are powerful because they're simple and intuitive. They operate on the **LIFO (Last In, First Out)** principle — the last item added is the first one removed. This structure is ideal for solving problems involving:

- **Matching symbols** (valid parentheses, HTML tags)
- **Undo sequences** (backspace string problems)
- **Monotonic sequences** (next greater/smaller element)
- **Reversing order** (strings, tree traversal)
- **Expression evaluation** (RPN, infix → postfix)

In many languages, stacks are implemented using dynamic arrays or lists. In Python, a list with `.append()` and `.pop()` does the job.

---

## 2. Stack Operations

| Operation | Purpose                      | Time Complexity | Python Example       |
|----------:|------------------------------|----------------:|----------------------|
| `push()`  | Add element to top           | O(1)            | `stack.append(x)`    |
| `pop()`   | Remove top element           | O(1)            | `stack.pop()`        |
| `peek()`  | Look at top element (optional) | O(1)            | `stack[-1]`          |
| `empty()` | Check if stack is empty      | O(1)            | `not stack`          |

---

## 3. Practice Problem Line-Up & Why Each Matters

| # | Problem | File | Concept | Why It Matters |
|---|---------|------|---------|----------------|
| 1 | [Valid Parentheses (LC 20)](https://leetcode.com/problems/valid-parentheses/) | `1. [easy] Valid Parentheses.py` | Stack (matching pairs) | Classic use of stack to track opening/closing characters |
| 2 | [Final Prices With Discount (LC 1475)](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/) | `2. [easy] Final Prices With a Special Discount.py` | Stack (next smaller element) | Real-world problem using monotonic stack logic |
| 3 | [Evaluate Reverse Polish Notation (LC 150)](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | `3. [Medium] Evaluate Reverse Polish Notation.py` | Stack (expression evaluation) | Great for learning stack-based math evaluation |
| 4 | [Daily Temperatures (LC 739)](https://leetcode.com/problems/daily-temperatures/) | `4. [Medium] Daily Temperatures.py` | Monotonic stack | Teaches “next greater element” technique |
| 5 | [Car Fleet (LC 853)](https://leetcode.com/problems/car-fleet/) | `5. [Medium] Car Fleet.py` | Stack (reverse traversal) | Combines sorting, greedy, and stack for fleet merging |
| 6 | [Min Stack (LC 155)](https://leetcode.com/problems/min-stack/) | `6. [Medium] Minimum Stack.py` | Stack with min tracking | Shows how to maintain extra state in parallel stacks |
| 7 | [Largest Rectangle in Histogram (LC 84)](https://leetcode.com/problems/largest-rectangle-in-histogram/) | `7. [Hard] Largest Rectangle in Histogram.py` | Stack (area calculation) | One of the most advanced and essential monotonic stack problems |

---

## 4. Learning Goals for Week 6

By the end of this week, you should be able to:

- ✅ Recognize stack-friendly problem patterns  
- ✅ Simulate stacks using arrays/lists  
- ✅ Implement monotonic stacks for next greater/smaller problems  
- ✅ Evaluate expressions and solve max-area problems using stacks  
- ✅ Layer logic like greedy/sorting on top of stack-based techniques

---

## 5. Skip Test 🚦

If you can solve [Largest Rectangle in Histogram (LC 84)](https://leetcode.com/problems/largest-rectangle-in-histogram/)  
using a **monotonic stack** approach in under **30 minutes**, you’re ready to move on!

---

## 6. Further Reading & Practice

- 📘 [LeetCode Stack Explore Card](https://leetcode.com/explore/learn/card/queue-stack/)
- 🎯 [NeetCode Stack Practice](https://neetcode.io/practice)
- 📚 [GeeksforGeeks Stack Overview](https://www.geeksforgeeks.org/stack-data-structure/)
- 🐍 [Python Lists as Stacks (Official Docs)](https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks)

---

**Next up:**  
**Week 7 — Trees**  
You'll learn BFS, DFS

**Happy stacking! 🥞**
