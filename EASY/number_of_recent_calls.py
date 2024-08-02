"""
Problem Link: https://leetcode.com/problems/number-of-recent-calls/description/?envType=study-plan-v2&envId=leetcode-75

- data structure: since we need to add/remove elements from both ends, we use queue. 
- We need to keep track of all requests within the last 3000 milliseconds.
- When a new request comes in, remove all requests that are older than t - 3000.

e.g.
Input:  ["RecentCounter", "ping", "ping", "ping", "ping"]
        [[], [1], [100], [3001], [3002]]
Output: [null, 1, 2, 3, 3]

"""

# Sliding window
from collections import deque


class RecentCounter:

    def __init__(self):
        self.slide_window = deque()

    def ping(self, t: int) -> int:
        # 1. apend the current cell
        self.slide_window.append(t)

        # 2. invalidate the outdated pings
        while self.slide_window[0] < t - 3000:
            self.slide_window.popleft()
        
        return len(self.slide_window)


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
param_1 = obj.ping(1)
param_2 = obj.ping(100)
param_3 = obj.ping(3001)
param_4 = obj.ping(3002)
