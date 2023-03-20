class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Use Max Heap 
        # Time complexity: O(n log n)

        # Python does not have max heap but mean heap!
        # Use mean heap by multiplying (-1)

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first-second)
            
        stones.append(0)
        return abs(stones[0])


