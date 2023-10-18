class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        count = {} # hash map to count occurrences of each ratio
        
        for w, h in rectangles:
            count[w / h] = 1 + count.get(w / h, 0)

        res = 0
                
        # Iterate through the count of rectangles for each unique width-to-height ratio.
        for c in count.values():
            if c > 1:
                res += (c * (c - 1)) // 2
    
        return res