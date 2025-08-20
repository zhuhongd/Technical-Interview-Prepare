"""
Problem: Find the Duplicate Number

You're given an array of `n + 1` integers where:
- Each integer is between [1, n] (inclusive)
- Only one number is duplicated, but it may appear multiple times

Your task:
- Return the duplicate number
- **You must NOT** modify the input array
- You must use **O(1)** space
- You must run in **less than O(n^2)** time

Examples:
---------

Input: nums = [1, 2, 3, 2, 2]  
Output: 2

Input: nums = [1, 2, 3, 4, 4]  
Output: 4

Constraints:
------------
- 1 <= n <= 10,000
- len(nums) == n + 1
- 1 <= nums[i] <= n

Follow-Up:
----------
Can you solve this using:
- ❌ No extra space
- ❌ No modification to array
- ✅ O(n) time

Link: https://leetcode.com/problems/find-the-duplicate-number/
"""

# 🧠 Intuition:
# Treat the array as a linked list where:
#   - The index is the node
#   - nums[i] is the "next" pointer
#
# Since there's a duplicate, there must be a cycle (like in a linked list).
# Use Floyd’s Tortoise and Hare Cycle Detection to find the start of the cycle,
# which corresponds to the duplicate number.

# 🎤 Interview Tip:
# - “This is a beautiful reduction: instead of brute-force or counting,
#    we treat the array as a pointer structure and detect a cycle.”
# - “It’s like Linked List Cycle Detection, but instead of ListNode.next,
#    we use nums[i] as a pointer to the next index.”

# Time:  O(n)
# Space: O(1)

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Step 1: Detect intersection point using slow & fast pointers
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Step 2: Move one pointer to start; find entrance to cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


"""
🧪 Dry Run:

Input: nums = [1, 3, 4, 2, 2]

Index → Value
 0     → 1
 1     → 3
 2     → 4
 3     → 2
 4     → 2

Path: 0 → 1 → 3 → 2 → 4 → 2 ... (cycle)

Floyd’s Algo finds the start of this cycle = duplicate = 2

✅ Handles:
- Multiple repetitions of the duplicate
- Arrays of any valid length (n + 1)
- Constant space and in-place traversal
"""
