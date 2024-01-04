"""
Problem Link: https://leetcode.com/problems/reorganize-string/

Frequency Counting: Count the frequency of each character in the string.
Max Heap: Use a max heap (priority queue to arrange the characters by their frequency. (in python use minHeap with neg value)

Greedy Approach: while heap is not empty, pop the most frequent character and append to the result.
If prevous is not None, push it back onto the heap so that it could be used again.
Update prevous with the current character and its updated count unless the count reaches zero. 

Time Complexity: O(n log n) primarily due to heap operations


"""

from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s):
        count = Counter(s)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)  # Turn it into a heap; O(n) time

        prev = None  # Store the previous character we used
        res = ""

        if prev and not maxHeap:
            return ""

        while maxHeap:
            # Most frequent, except prev
            cnt, char = heapq.heappop(maxHeap)  # Pop out the most freq char
            res += char
            cnt += 1  # Decrease the count (since it's a negative count)

            if prev:  # If prev is not null
                heapq.heappush(maxHeap, prev)
                prev = None  # Set prev back to null
            
            # Add back to the heap only if count is not equal to 0
            if cnt != 0:
                prev = [cnt, char]
        
        # If the length of the result is not equal to the length of the input,
        # it means the string cannot be reorganized to meet the condition
        if len(res) != len(s):
            return ""