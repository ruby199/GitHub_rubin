"""
Problem Link: https://leetcode.com/problems/remove-covered-intervals/description/

Correct Approach:
[1] Sort the intervals based on their starting points & by their ending points in descending order if the starting points are the same
[2] Iterate through the sorted intervals & compar each intervals to its successor

Time Complexity: Sorting alg + iterating through the intervals = 
O(nlogn) + O(n)  = O(nlogn), where n is number of intervals. 

Space Complexity: Sorting alg + variables for iteration:
O(n) + O(1) = O(n)
"""

class Solution:
    def removeCoveredIntervals_wrong(self, intervals) -> int:
        """
        Wrong Solution. This solution does not pass all test cases. 
        Failing test case; intervals = [[0,10],[5,12]]
        """
        # 1. find the smallest intervals[i][0]
        # 2. find the largest intervals[j][1]
        # 3. remove intervals if smallest < intervals[i][0] and largest > intervals[j][1] 

        smallest = float("inf")
        largest = float("-inf")
        
        for i in range(len(intervals)):
            if intervals[i][0] < smallest:
                smallest = intervals[i][0]
        
        for j in range(len(intervals)):
            if intervals[j][1] > largest:
                largest = intervals[j][1]

        for interval in intervals:
            if smallest <= interval[0] and largest >= interval[1]:
                intervals.remove(interval)
        
        
        return len(intervals)
    
    def removeCoveredIntervals_fixed(self, intervals) -> int:
        # Time Complexity:B eats 39.93% of users with Python3
        # Space Complexity: Beats 87.89% of users with Python3

        # Sort intervals by start time
        intervals.sort(key=lambda x: (x[0], -x[1]))
        # print(intervals)

        count = 0
        prev_end = 0
        for _, end in intervals:
            if end > prev_end: # if the current interval's end is greater than the previous recorded end it is not fully covered by any interval seen so far
                count += 1
                prev_end = end
        return count



# Test the function with the provided examples
sol = Solution()
test_cases = [
    ([[1,4],[3,6],[2,8]], 2),
    ([[1,4],[2,3]], 1),
    ([[0,10],[5,12]], 2)
]

results = {str(case[0]): sol.removeCoveredIntervals_fixed(case[0]) == case[1] for case in test_cases}
print(results)