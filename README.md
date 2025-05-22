# Technical-Interview-Prepare
A structured project for Summer 2025 to prepare for technical interviews, including completing LeetCode question sets and documenting problem-solving approaches as part of EECS4070.

# Week 1 -> Week 2:

Week 1 covers `HashSet`, `HashMap`, and frequency counting — all of which are essential for implementing Two Pointer and Sliding Window problems in Week 2.

### Key Contributions from Week 1

- **HashSet for Duplicate Detection**
  - Used in sliding window problems like **Longest Substring Without Repeating Characters**
  - Helps track which characters are currently in the window
  - Supports constant-time checks for whether to shrink the window

- **HashMap for Frequency Counting**
  - Critical in problems like **Minimum Window Substring**
  - Tracks how many times a character is required vs. how many times it appears in the current window
  - Week 1's problem **Top K Frequent Elements** teaches you how to build and update frequency maps efficiently

- **Big O and Hash-Based Thinking**
  - Week 1 builds intuition for replacing O(n²) brute-force with O(n) hash-based approaches
  - These optimizations are at the core of sliding window and two-pointer patterns

### Summary

Without Week 1’s practice in using hash structures to manage state, it would be difficult to efficiently implement pointer movement, window adjustments, and dynamic condition checks in Week 2. The data structures and logic learned in Week 1 are not just helpful — they are essential building blocks for mastering Week 2 techniques.
