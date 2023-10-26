import heapq


class SeatManager:
    def __init__(self, n: int):
        # At the beginning, all seats from 1 to n are unreserved. 
        self.unres = [i for i in range(1, n + 1)] # need to keep track of unreserved seats only
        # Since the list is already sorted, it implicitly forms a valid minHeap

    def reserve(self) -> int:
        # retrieves and removes the smallest-numbered unreserved seat, 
        return heapq.heappop(self.unres)

    def unreserve(self, seatNumber: int) -> None:
        # pushes a new item onto the heap.
        # It addes the saet number back to the heap, marking it as unreserved
        heapq.heappush(self.unres, seatNumber)


# Could be solved by using TreeSet (But python does not have TreeSet)