import unittest
from typing import List
import heapq

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in count: 
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertTrue(self.solution.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))

    def test_example2(self):
        self.assertFalse(self.solution.isNStraightHand([1, 2, 3, 4, 5], 4))

    def test_example3(self):
        self.assertTrue(self.solution.isNStraightHand([1, 2, 3, 4], 2))

    def test_example5(self):
        self.assertFalse(self.solution.isNStraightHand([5, 1], 2))

if __name__ == '__main__':
    unittest.main()
