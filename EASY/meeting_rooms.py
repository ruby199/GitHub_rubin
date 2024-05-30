"""
Problem Link: https://leetcode.com/problems/meeting-rooms/description/

Given an array of meeting time intervals where intervals[i] = [starti, endi], determine if a person could attend all meetings.

Time Complexity: O(n log n)
Memory Complexity: O(1)

"""

class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        # sort the meetings by start time
        intervals.sort()

        if not intervals:
            return True
        
        start, end = intervals[0]

        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i]
            if end > cur_start:
                return False
            else:
                start, end = cur_start, cur_end
        
        return True

sol = Solution()

intervals1 = [[0,30],[5,10],[15,20]]
intervals2 = [[7,10],[2,4]]

print(sol.canAttendMeetings(intervals1)) # false
print(sol.canAttendMeetings(intervals2)) # true