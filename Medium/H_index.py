"""
Problem Link: https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150

Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.

h-index: the max value of h s.t. given researcher has published at least h papers that have each been cited at least h times. 

"""

class Solution:
    def hIndex1(self, citations) -> int:
        citations.sort(reverse=True)
        
        h_index = 0

        for i, citation in enumerate(citations):
            if i + 1 <= citation:
                h_index = i + 1
            else:
                break

        return h_index

    def hIndex(self, citations) -> int:
        n = len(citations)
        papers = [0] * (n + 1)

        for c in citations:
            papers[min(n, c)] += 1
        
        # find the h-inex
        k = n
        s = papers[n]
        while k > s:
            k -= 1
            s += papers[k]
        
        return k


sol = Solution()
citations1 = [3,0,6,1,5]
citations2 = [1,3,1]
print(sol.hIndex(citations1)) # Expected Output:  3
print(sol.hIndex(citations2)) # Expected Output:  1