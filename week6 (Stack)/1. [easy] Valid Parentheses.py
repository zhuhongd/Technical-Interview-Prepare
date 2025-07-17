# valid_parentheses_explained.py

"""
Problem: Valid Parentheses

You are given a string s containing only the characters '(', ')', '{', '}', '[' and ']'.

A string is valid if:
1. Every open bracket has a corresponding close bracket of the same type.
2. Open brackets are closed in the correct order.
3. Every close bracket has a corresponding open bracket.

Examples:
    Input: s = "[]"         → Output: True
    Input: s = "([{}])"     → Output: True
    Input: s = "[(])"       → Output: False

Link: https://neetcode.io/problems/validate-parentheses?list=neetcode150
"""

class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to store opening brackets
        stack = []

        # Dictionary mapping closing brackets to their corresponding opening brackets
        matchdict = {')': '(', '}': '{', ']': '['}

        # Iterate through each character in the string
        for char in s:
            if char in matchdict:
                # It's a closing bracket
                # Check if the stack is not empty and the top of the stack matches the corresponding opening bracket
                if stack and stack[-1] == matchdict[char]:
                    stack.pop()  # Brackets match — remove the opening from the stack
                else:
                    # Either the stack is empty or the top doesn't match → invalid
                    return False
            else:
                # It's an opening bracket — push it to the stack
                stack.append(char)

        # After processing all characters, stack should be empty if all brackets matched
        return len(stack) == 0


# Test cases to verify correctness
if __name__ == "__main__":
    test_cases = [
        ("[]", True),
        ("([{}])", True),
        ("[(])", False),
        ("", True),           # Edge case: empty string is valid
        ("[", False),         # Single unmatched opening
        ("{[()]}", True),
        ("{[)]}", False),
        ("(((((", False),
        ("(()())", True),
        ("[{()}]{}", True)
    ]

    for s, expected in test_cases:
        result = Solution().isValid(s)
        print(f"isValid({s}) => {result} | Expected: {expected} | {'✅' if result == expected else '❌'}")

"""
Comprehensive Explanation:

We use a stack because it allows us to track the "most recent unclosed bracket".
The idea is:
- Push opening brackets onto the stack.
- When you see a closing bracket, check if it matches the top of the stack.
    * If it matches: pop the top (they're matched).
    * If not: return False immediately.
- At the end, the stack should be empty — meaning all opening brackets were matched and closed in correct order.

Time Complexity: O(n)
- We loop through the string once.

Space Complexity: O(n)
- In the worst case, all characters are opening brackets and get pushed onto the stack.
"""
