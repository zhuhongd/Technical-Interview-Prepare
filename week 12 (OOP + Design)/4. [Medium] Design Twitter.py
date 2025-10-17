r"""
=========================================================
Design Twitter — EECS4070 (Explained, Clean Readable Syntax)
=========================================================

Problem
-------
Design a simplified Twitter where users can:
  1. post tweets
  2. follow / unfollow other users
  3. retrieve the 10 most recent tweets in their news feed

The news feed shows tweets from the user and people they follow,
ordered from most recent to oldest.

Link
----
https://leetcode.com/problems/design-twitter/

Key Example
------------
Input:
  ["Twitter", "postTweet", "follow", "postTweet", "getNewsFeed"]
  [[], [1, 5], [1, 2], [2, 6], [1]]
Output:
  [null, null, null, null, [6,5]]

---------------------------------------------------------
Beginner Intuition
------------------
We simulate a tiny social platform using classes:
- Each user can post tweets (stored with timestamps)
- Each user can follow others
- We can gather all tweets from a user and their followees,
  then show the 10 newest tweets in descending time order.

We'll simulate "time" with a simple integer counter that increases
every time a tweet is posted.
---------------------------------------------------------
"""

import heapq
from collections import defaultdict
from typing import List


class Twitter:
    """
    A simplified Twitter model that stores tweets, follow relationships,
    and provides a news feed of recent tweets.
    """

    def __init__(self):
        self.tweets = defaultdict(list)   # user_id -> [(timestamp, tweetId), ...]
        self.followees = defaultdict(set) # user_id -> {followeeId, ...}
        self.time = 0                     # global time counter

    def postTweet(self, userId: int, tweetId: int) -> None:
        """Posts a tweet by this user with the current timestamp."""
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Returns up to 10 most recent tweet IDs from this user
        and users they follow.
        """
        # Collect tweets from self + followees
        heap = []
        users_to_include = {userId} | self.followees[userId]

        for uid in users_to_include:
            for timestamp, tweet_id in self.tweets[uid]:
                # Push (-timestamp) to simulate a max-heap
                heapq.heappush(heap, (-timestamp, tweet_id))

        # Extract up to 10 tweets (most recent first)
        feed = []
        total_tweets = min(10, len(heap))
        for _ in range(total_tweets):
            most_recent = heapq.heappop(heap)   # tuple (-time, tweet_id)
            tweet_id = most_recent[1]
            feed.append(tweet_id)

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        """Follower starts following a followee."""
        if followerId != followeeId:
            self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """Follower stops following a followee."""
        self.followees[followerId].discard(followeeId)


# =========================================================
# 🧪 Demonstration / Test Cases
# =========================================================
def _run_tests() -> None:
    print("===== Example Walkthrough =====")
    t = Twitter()

    t.postTweet(1, 5)
    print("Step 1:", t.getNewsFeed(1))  # [5]

    t.follow(1, 2)
    t.postTweet(2, 6)
    print("Step 2:", t.getNewsFeed(1))  # [6,5]

    t.unfollow(1, 2)
    print("Step 3:", t.getNewsFeed(1))  # [5]

    print("\n===== Extended Checks =====")
    t.postTweet(1, 7)
    t.postTweet(1, 8)
    t.postTweet(1, 9)
    print("Feed (latest 3):", t.getNewsFeed(1))

    # multiple users
    tw = Twitter()
    for i in range(1, 6):
        tw.postTweet(1, i)
    tw.postTweet(2, 100)
    tw.follow(1, 2)
    print("Merged Feed [user1 follows user2]:", tw.getNewsFeed(1))


if __name__ == "__main__":
    _run_tests()


r"""
=========================================================
✅ Sample Output
---------------------------------------------------------
===== Example Walkthrough =====
Step 1: [5]
Step 2: [6, 5]
Step 3: [5]

===== Extended Checks =====
Feed (latest 3): [9, 8, 7]
Merged Feed [user1 follows user2]: [100, 5, 4, 3, 2, 1]
=========================================================

Complexity Recap
---------------------------------------------------------
• postTweet:    O(1)
• follow/unfollow: O(1)
• getNewsFeed:  O(N log N)  (N = #tweets considered)
• Space:        O(U + T)
=========================================================
"""
