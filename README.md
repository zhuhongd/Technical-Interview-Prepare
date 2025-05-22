# Technical-Interview-Prepare
A structured project for Summer 2025 to prepare for technical interviews, including completing LeetCode question sets and documenting problem-solving approaches as part of EECS4070.

# Week 1 -> Week 2:

In Week 1, learning how to use HashMap and HashSet lays the groundwork for implementing both two-pointer and sliding window techniques in Week 2. For example, in the problem "Longest Substring Without Repeating Characters", a HashSet is used to track characters in the current window. As you move the right pointer to expand the window, you check if the character already exists in the set. If it does, the left pointer is moved forward while removing characters from the set until the window becomes valid again. Without mastering HashSet usage in Week 1, this kind of logic would be hard to implement efficiently.

Similarly, in problems like "Minimum Window Substring", HashMap is used to store the frequency of required characters. As you slide the window using two pointers, you compare the current window’s frequency map to the target map. This relies on the ability to count characters accurately and update counts dynamically — a skill practiced through Week 1’s hashmap-heavy problems like "Top K Frequent Elements".

In short, Week 1 teaches you how to track occurrences and manage element presence quickly using hashing, which directly powers the logic behind when to expand or shrink the window in Week 2’s problems.