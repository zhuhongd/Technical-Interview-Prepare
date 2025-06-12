"""
Problem: Sliding Window Maximum

You are given an array of integers `nums` and an integer `k`. There is a sliding window of size `k` that moves from left to right,
one element at a time.

Return a list of the **maximum element** in the window at each step.

Examples:
Input: nums = [1, 2, 1, 0, 4, 2, 6], k = 3
Output: [2, 2, 4, 4, 6]

Explanation:
Sliding windows and max values:
[1  2  1] 0  4  2  6  → max = 2  
 1 [2  1  0] 4  2  6  → max = 2  
 1  2 [1  0  4] 2  6  → max = 4  
 1  2  1 [0  4  2] 6  → max = 4  
 1  2  1  0 [4  2  6] → max = 6

Constraints:
- 1 <= nums.length <= 1000
- -1000 <= nums[i] <= 1000
- 1 <= k <= nums.length

Link: https://leetcode.com/problems/sliding-window-maximum/
"""

# -----------------------------
# Optimized Deque Approach:
# -----------------------------
# Use a deque to store indices of useful elements in the current window.
# Elements in the deque are always in decreasing order of their values.
# Time complexity: O(n)
# Space complexity: O(k)

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        result = []          # List to store max of each window
        q = deque()          # Stores indices, not values
                             # Elements in q are always in decreasing value order
        left = 0             # Start of the current window

        for right in range(len(nums)):
            # Step 1: Remove smaller elements from the back
            # They cannot be max if a bigger number has arrived
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            # Step 2: Add current index to the deque
            q.append(right)

            # Step 3: Remove indices that are outside the current window
            if q[0] < left:
                q.popleft()

            # Step 4: If the window has hit size k, record the max
            if right - left + 1 >= k:
                result.append(nums[q[0]])  # The max is always at the front
                left += 1  # Slide window to the right

        return result

"""
Sliding Window Summary:

- Type: Fixed-size sliding window
- Goal: Track the max efficiently in each window of size k
- Data Structure: Monotonic deque (decreasing order)
    - Maintain only useful elements
    - Remove all elements smaller than current from the back
    - Remove front element if it's outside the window

Why it works:
- Deque always keeps the largest element's index at the front
- When a new element is added, we pop out all smaller elements behind it since they won't be useful anymore

Visual Example (nums = [1,2,1,0,4,2,6], k = 3):

Window        Deque (indices)    Max
[1 2 1]       [1,2]              nums[1] = 2
[2 1 0]       [1,2,3] → [2,3]    nums[2] = 2
[1 0 4]       [4]                nums[4] = 4
[0 4 2]       [4,5]              nums[4] = 4
[4 2 6]       [6]                nums[6] = 6

This is a high-value pattern for real-time sliding aggregation with optimization!
"""
