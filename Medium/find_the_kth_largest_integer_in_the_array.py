class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        # Heapify O(n)
        # k log(n)
        
        # Convert each string number to its negative integer equivalent.
        # This is done to emulate a max-heap using Python's min-heap.
        maxHeap = [-int(n) for n in nums]  # Using negative values to work with a min-heap as if it's a max-heap

        # Transform the list 'maxHeap' into a heap in-place. After this operation, 
        # the smallest item (i.e., the largest item in negative form) can be accessed using maxHeap[0].
        heapq.heapify(maxHeap)

        # Pop the smallest item (i.e., the largest in negative form) k-1 times
        # so that the kth largest item ends up at the root of the heap.
        while k > 1:
            heapq.heappop(maxHeap)  # Remove and return the smallest element from the heap.
            k -= 1  # Decrement k by 1 after each pop.

        # At this point, maxHeap[0] holds the kth largest number in negative form.
        # We negate it to get the actual kth largest number and return it as a string.
        return str(-maxHeap[0])