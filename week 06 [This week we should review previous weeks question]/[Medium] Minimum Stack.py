"""
Problem: Minimum Stack

Design a stack that supports:
- push(int val)
- pop()
- top()
- getMin()

All operations must run in O(1) time.

Example:

Input: ["MinStack", "push", 1, "push", 2, "push", 0, "getMin", "pop", "top", "getMin"]

Output: [null,null,null,null,0,null,2,1]

Explanation:
MinStack minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(0);
minStack.getMin(); // return 0
minStack.pop();
minStack.top();    // return 2
minStack.getMin(); // return 1

Approach:
Use two stacks:
1. store: the actual values
2. minstack: the minimum value at each level
"""

class MinStack:
    def __init__(self):
        # Main stack to store values
        self.store = []
        # Auxiliary stack to store current minimum at each level
        self.minstack = []

    def push(self, val: int) -> None:
        self.store.append(val)
        # Determine new minimum: either the incoming value or the previous min
        if self.minstack:
            val = min(val, self.minstack[-1])
        self.minstack.append(val)

    def pop(self) -> None:
        # Remove top element from both stacks
        self.store.pop()
        self.minstack.pop()

    def top(self) -> int:
        # Return the top of the main stack
        return self.store[-1]

    def getMin(self) -> int:
        # Return the current minimum (top of minstack)
        return self.minstack[-1]



# Simulate the example
if __name__ == "__main__":
    commands = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
    values = [None, 1, 2, 0, None, None, None, None]
    
    output = []
    minStack = None

    for command, val in zip(commands, values):
        if command == "MinStack":
            minStack = MinStack()
            output.append(None)
        elif command == "push":
            minStack.push(val)
            output.append(None)
        elif command == "pop":
            minStack.pop()
            output.append(None)
        elif command == "top":
            output.append(minStack.top())
        elif command == "getMin":
            output.append(minStack.getMin())

    print("Final Output:", output)
    # Expected: [None, None, None, None, 0, None, 2, 1]
