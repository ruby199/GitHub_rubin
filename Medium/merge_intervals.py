class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Time complexity: O(nLogn) as we are going through the whole input

        intervals.sort(key = lambda i : i[0]) # sort by start value only

        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1] # end value of the most recent interval
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        
        return output

            

