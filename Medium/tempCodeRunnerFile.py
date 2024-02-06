class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Since python does not have maxHeap - we can use neg value & minHeap instead. 
        res, maxHeap = "", []

        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]: 
            # print(count, char)
            if count != 0: # edge case: We don't want to add "count = 0" to the heap
                heapq.heappush(maxHeap, (count, char)) # [(-7, 'c'), (-1, 'b'), (-1, 'a')]
        
        while maxHeap:
        #### Adding the most common characters - until our maxHeap becomes empty
            # We want to add character to the res and decrement the count (only if it satisfies the conditions)
            count, char = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap: # If we don't have the second most character does not exist
                    break
                count2, char2 = heapq.heappop(maxHeap)
                print("count2, char2 = ", count2, char2)
                res += char2
                count2 += 1
                if count2:
                    heapq.heappush(maxHeap, (count2, char2))
                print("res = ", res)
            else:
                res += char
                count += 1
            
        #### Of count is left, we want to add it back to the maxHeap
            if count: # single character left
                heapq.heappush(maxHeap, (count, char))

        return res