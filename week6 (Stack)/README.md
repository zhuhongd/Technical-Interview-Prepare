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

| # | Problem | File | Concept | Why it matters |
|---|---------|------|---------|----------------|
| 1 | [Valid Parentheses (LC 20)](https://leetcode.com/problems/valid-parentheses/) | `valid_parentheses.py` | Stack (matching pairs) | Classic use of stack to track opening/closing characters |
| 2 | [Min Stack (LC 155)](https://leetcode.com/problems/min-stack/) | `min_stack.py` | Stack with auxiliary min tracking | Teaches how to maintain extra info using a parallel stack |
| 3 | [Evaluate Reverse Polish Notation (LC 150)](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | `eval_rpn.py` | Expression evaluation | Shows how stacks model math expression evaluation |
| 4 | [Daily Temperatures (LC 739)](https://leetcode.com/problems/daily-temperatures/) | `daily_temperatures.py` | Monotonic stack | Important pattern for solving \"next greater element\" problems |
| 5 | [Car Fleet (LC 853)](https://leetcode.com/problems/car-fleet/) | `car_fleet.py` | Stack (backward traversal) | Simulates group behavior with time-to-goal calculations |
| 6 | [Final Prices With Discount (LC 1475)](https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/) | `final_prices_with_discount.py` | Stack (next smaller element) | Classic discount-pricing logic with monotonic stack |
| 7 | [Largest Rectangle in Histogram (LC 84)](https://leetcode.com/problems/largest-rectangle-in-histogram/) | `largest_rectangle_histogram.py` | Stack (area calculation) | One
