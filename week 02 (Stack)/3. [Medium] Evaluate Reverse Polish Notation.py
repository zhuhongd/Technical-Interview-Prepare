"""
Problem: Evaluate Reverse Polish Notation

You are given a list of strings representing a valid Reverse Polish Notation (RPN) expression.
Return the result of evaluating the expression.

Operators supported: "+", "-", "*", "/"
Division should truncate toward zero.

Example:
    Input:  ["1", "2", "+", "3", "*", "4", "-"]
    Output: 5
    Explanation: ((1 + 2) * 3) - 4 = 5
"""

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                # Pop the top two numbers from the stack
                a = stack.pop()
                b = stack.pop()

                # Perform the operation based on the token
                if token == "+":
                    result = b + a
                elif token == "-":
                    result = b - a
                elif token == "*":
                    result = b * a
                elif token == "/":
                    # Division that truncates toward zero
                    result = int(b / a)

                # Push the result back onto the stack
                stack.append(result)
            else:
                # It's a number — convert to int and push
                stack.append(int(token))

        # The last remaining value is the result
        return stack[0]


# Test block to simulate the example
if __name__ == "__main__":
    tokens = ["1", "2", "+", "3", "*", "4", "-"]
    expected = 5

    result = Solution().evalRPN(tokens)
    print(f"Input: {tokens}")
    print(f"Output: {result}")
    print(f"Expected: {expected}")
    print("✅ Pass" if result == expected else "❌ Fail")

"""
🧠 How It Works:
- Reverse Polish Notation (RPN) uses a stack-based evaluation model.
- When you see a number, push it onto the stack.
- When you see an operator, pop the top two numbers, evaluate, and push the result.
- Continue until the end — the remaining item on the stack is the final answer.

Example walkthrough:
tokens = ["1", "2", "+", "3", "*", "4", "-"]

Step-by-step:
1. Push 1       → stack = [1]
2. Push 2       → stack = [1, 2]
3. '+'          → stack = [3]
4. Push 3       → stack = [3, 3]
5. '*'          → stack = [9]
6. Push 4       → stack = [9, 4]
7. '-'          → stack = [5]

✅ Final result: 5

⏱ Time Complexity: O(n) — one pass over the input list
📦 Space Complexity: O(n) — stack can grow to hold all numbers temporarily
"""
