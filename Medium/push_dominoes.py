"""
Problem Link: https://leetcode.com/problems/push-dominoes/description/
Topics: Two Pointers, String, Dynamic Programming

Note:
- Anything that starts out as L or R is always going to stay in that state.
- How about the remaining ones? -> pay attention to the direction in which they lean

Approach:
- Brute Force/Simulation (+ queue):
    - Consider the state of our dominoes after each second
    - Each sec we are going to have a queue. (should be in order L->R or R->L)

Time and Space Complexity: O(N), where N is the length of dominoes
"""
from collections import deque


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dom = list(dominoes) # what we are returning
        q = deque() # double ended queue

        for i, d in enumerate(dom):
            # we want to add all the dominos that are not standing straight
            if d != ".": q.append((i, d)) # index to check the neightbors

        # Order: L -> R (making the left simplier to track)
        # continue until queue is completely empty
        while q:
            i, d = q.popleft()

            if d == "L" and i > 0 and dom[i - 1] == ".":
                q.append((i - 1, "L"))
                dom[i - 1] = "L"
            elif d == "R":
                if i + 1 < len(dom) and dom[i + 1] == ".": # should be valid index
                    if i + 2 < len(dom) and dom[i + 2] == "L": # exists another domino in the right "L" -> cannot knock if over
                        q.popleft()
                    else:                    
                        # Tip it over and append it
                        q.append((i + 1, "R"))
                        dom[i + 1] = "R"
        
        return "".join(dom)







sol = Solution()
test_cases = ["RR.L", ".L.R...LR..L.."] # should be: "RR.L" and "LL.RR.LLRRLL.."


for test_case in test_cases:
    print(f"{test_case}: {sol.pushDominoes(test_case)}")