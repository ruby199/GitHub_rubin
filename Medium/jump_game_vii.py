from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # Initialize a deque (double-ended queue) 'q' to store the indices to be visited.
        # 'farthest' keeps track of the farthest index reached so far.
        q, farthest = deque([0]), 0

        # Start the BFS loop, it continues until there are no more indices to explore.
        while q:
            # Pop an index 'i' from the left side of the deque.
            i = q.popleft()

            # Calculate the starting point 'start' for new jumps.
            # 'start' ensures that we jump only to new indices and within the valid range.
            start = max(i + minJump, farthest + 1)

            # Loop through all possible jump destinations 'j' from 'start' to 'min(i + maxJump + 1, len(s))'.
            for j in range(start, min(i + maxJump + 1, len(s))):
                # If the destination index 'j' is valid (contains '0'), add it to the deque for further exploration.
                if s[j] == "0":
                    q.append(j)

                    # If the current jump destination 'j' is the last index, we've reached the end successfully.
                    return True

            # Update 'farthest' to the farthest index we can reach from the current position 'i'.
            farthest = i + maxJump

        # If we haven't found a path to the end by the end of the loop, return False.
        return False
