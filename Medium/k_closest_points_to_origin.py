class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = [] # A minimum heap (min heap) is used to efficiently keep track of the k smallest distances. In a min heap, the element with the smallest value is kept at the root.


        for x, y in points:
            dist = (x ** 2) + (y**2)
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res