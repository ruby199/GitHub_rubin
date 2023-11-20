class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        # Sort the intervals in place based on their start times.
        intervals.sort()

        # Initialize the counter for the number of intervals to remove.
        res = 0

        # Store the end time of the first interval.
        prevEnd = intervals[0][1]

        # Iterate over the rest of the intervals, starting from the second one.
        for start, end in intervals[1:]:
            # If the start time of the current interval is not less than the end time of the previous interval,
            # it means there's no overlap, and we update prevEnd to the current interval's end time.
            if start >= prevEnd:
                prevEnd = end
            # If there is an overlap, increment the removal counter.
            # Update prevEnd to be the minimum of the current end time and the previous end time.
            # This ensures prevEnd always points to the earliest end time to minimize overlap.
            else:
                res += 1
                prevEnd = min(end, prevEnd)

        # Return the total count of intervals that need to be removed.
        return res

# class Solution:
#     def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
#         # Sort the Intervals based on their end times
#         sorted_intervals = sorted(intervals, key=lambda x: x[1])

#         # Initialize Variables
#         res = 0
#         prevEnd = intervals[0][1]

#         # Interate through the intervals
        
#         for start, end in intervals[1:]:
#             if start >= prevEnd:
#                 prevEnd = end
#             else:
#                 res += 1
#                 prevEnd = min(end, prevEnd)
#         return res



# Testing function
def test_eraseOverlapIntervals():
    solution = Solution()

    # Test cases
    test_cases = [
        ([[1,2],[2,3],[3,4],[1,3]], 1),
        ([[1,2],[1,2],[1,2]], 2),
        ([[1,2],[2,3]], 0)
    ]

    # Testing each case
    for intervals, expected in test_cases:
        result = solution.eraseOverlapIntervals(intervals)
        print(f"Test with intervals {intervals}: Expected {expected}, got {result}")

# Run the testing function
test_eraseOverlapIntervals()
