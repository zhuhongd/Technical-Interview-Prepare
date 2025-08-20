"""
LeetCode 1475: Final Prices With a Special Discount in a Shop

You are given an array 'prices' where prices[i] is the price of the ith item.

For each item, if there is a later item j (j > i) such that prices[j] <= prices[i],
you get a discount of prices[j].

Return a new list 'answer' where answer[i] = prices[i] - discount (if found), or just prices[i] otherwise.

Examples:
Input:  prices = [8, 4, 6, 2, 3]
Output: [4, 2, 4, 2, 3]

Input:  prices = [1, 2, 3, 4, 5]
Output: [1, 2, 3, 4, 5]

Input:  prices = [10, 1, 1, 6]
Output: [9, 0, 1, 6]

link: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/
"""

from typing import List

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        result = prices[:]
        stack = []

        # Monotonic stack (non-increasing) — stores indices
        for i in range(n):
            # Check if the current price is less than or equal to the top of the stack
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                result[idx] = prices[idx] - prices[i]
            stack.append(i)

        return result


# Test block
if __name__ == "__main__":
    prices = [8, 4, 6, 2, 3]
    expected = [4, 2, 4, 2, 3]

    output = Solution().finalPrices(prices)
    print(f"Input:    {prices}")
    print(f"Output:   {output}")
    print(f"Expected: {expected}")
    print("✅ Pass" if output == expected else "❌ Fail")

"""
🧠 How It Works:

We use a monotonic stack to track unresolved prices. For each price:
- While the current price is less than or equal to the top of the stack, we found a discount!
- Pop from stack and apply the discount to that previous index.
- Push the current index to the stack.

Stack stores indices, not values, so we can modify 'result' directly when we find a valid discount.

⏱ Time Complexity: O(n)
- Each index is pushed/popped from the stack at most once.

📦 Space Complexity: O(n)
- Stack stores up to n indices in the worst case.
"""
