"""
Problem Link: https://leetcode.com/problems/number-of-days-between-two-dates/?envType=study-plan-v2&envId=google-spring-23-high-frequency

Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

Topics: Math, string
"""
from datetime import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        # Convert the date strings to datetime.date objects
        d1 = datetime.strptime(date1, "%Y-%m-%d").date()
        d2 = datetime.strptime(date2, "%Y-%m-%d").date()
        
        # Calculate the absolute difference in days
        return abs((d2 - d1).days)

sol = Solution()
date1 = "2019-06-29"
date2 = "2019-06-30"
print(sol.daysBetweenDates(date1, date2)) # Expected Output: 1

date1 = "2020-01-15"
date2 = "2019-12-31"
print(sol.daysBetweenDates(date1, date2)) # Expected Output: 15