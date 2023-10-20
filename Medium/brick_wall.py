from ast import List
from collections import defaultdict


# class Solution:
#     def leastBricks(self, wall: List[List[int]]) -> int:
#         if not wall:
#             return 0
        
#         prefix_sum_freq = defaultdict(int)
        
#         for row in wall:
#             prefix_sum = 0
#             # We iterate to len(row) - 1 to avoid the rightmost edge
#             for brick in row[:-1]:
#                 prefix_sum += brick
#                 prefix_sum_freq[prefix_sum] += 1
        
#         # If no valid positions are found (i.e. all rows have only one brick), default to 0
#         max_frequency = max(prefix_sum_freq.values(), default=0)
        
#         # Return the total number of rows minus the most frequent prefix sum
#         return len(wall) - max_frequency
    

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        countGap = {0 : 0}

        for r in wall:
            total = 0
            for b in r[:-1]:
                total += b
                countGap[total] = 1 + countGap.get(total, 0)
        
        return len(wall) - max(countGap.values())
    