"""
Problem Link: https://leetcode.com/problems/the-kth-factor-of-n/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

Description:
    You are given two positive integers n and k. 
    A factor of an integer n is defined as an integer i where n % i == 0.

    Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.

1) Brute Force Solution : iterate from 1 to N to figure out all divisors.

2) Heap: iterate from 1 to sqart(N) and push each divisor and its pair into a max heap of size k 

3) Math: return N / divisors[len(divisors) - k] if k <= len(divisors) and -1 otherwise

"""

from heapq import heappop, heappush


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # Brute Force Solution
        # Find all factors
        factors = []

        for i in range(1, n + 1):
            if i in factors:
                break            
            if n % i == 0:
                factors.append(i)

        if len(factors) < k:
            return -1
        
        return factors[k-1]

    def kthFactor_Heap(self, n: int, k: int) -> int:
        def heappush_k(num):
            heappush(heap, - num)
            if len(heap) > k:
                heappop(heap)
        
        heap = []
        for x in range(1, int(n**0.5) + 1):
            if n % x == 0:
                heappush_k(x)
                if x != n // x:
                    heappush_k(n // x)

        return -heappop(heap) if k == len(heap) else -1



n = 7
k = 2
sol = Solution()

print(sol.kthFactor(n, k))