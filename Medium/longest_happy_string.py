"""
Problem Link: https://leetcode.com/problems/longest-happy-string/description/

1405. Longest Happy String

Problem description:
- A string s is called happy if it satisfies the following conditions:
    s only contains the letters 'a', 'b', and 'c'.
    s does not contain any of "aaa", "bbb", or "ccc" as a substring.
    s contains at most a occurrences of the letter 'a'.
    s contains at most b occurrences of the letter 'b'.
    s contains at most c occurrences of the letter 'c'.

    Given three integers a, b, c, return the longest possible happy string.
    If there are multiple longest happy strings, return any of them.
    If there is no such string, return the empty string "".
    A substring is a contiguous sequence of characters within a string. 

[DEF] Heap: A Heap is a special Tree-based data structure in which the tree is a complete binary tree.
    - Heapify: a process of creating a heap from an array.

[DEF] Max-Heap: In a Max-Heap the key present at the root node must be greatest among the keys present at all of it's children. The same property must be recursively true for all sub-trees in that Binary Tree.

Approach: Use maxHeap and employ the greedy algorithm - keep iterating the most freq. character while checking the solution. 

Time Complexity: O(n log k) = O(n) # while n is the total number of (a + b + c) and k is the number of unique characters. Since k is constant, complexity could be simplified to O(n)
Space Complexity: O(a + b + c) = O(n) # size of the string

"""

import heapq


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
            print("count, char = ", count, char)
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
                print("What's left: ", count, char)

        return res
        






sol = Solution()
a = 1 
b = 1
c = 7

print(sol.longestDiverseString(a, b, c))





















