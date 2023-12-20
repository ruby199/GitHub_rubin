from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks, n):
        # each task 1 unit time
        # minimize idle time

        count = Counter(tasks) # Counts the frequency of each task
        maxHeap = [-cnt for cnt in count.values()] # creates a max heap for the task frequencies.  Negate the counts as Python has min heap by default.
        heapq.heapify(maxHeap)

        time = 0

        # Each element is a pair: [task count, time when task is again available].
        q = deque() # pairs of [-cnt, idleTime] # initialize deque to store tasks in their cooldown period. 
 
        while maxHeap or q:
            time += 1

            # If there are tasks in the max heap, process the one with the highest frequency.
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap) # decrease the task count
                if cnt:
                    q.append([cnt, time + n]) # add the task to the cooldown queue. 
            
            # If the task at the front of the cooldown queue is ready to be scheduled again, move it back to the max heap.
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time

