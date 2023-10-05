class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, comb): # starting value, current comb we have
            if len(comb) == k: # height k
                res.append(comb.copy()) # comb is a list (object) thus before adding it, should add copy
                return
            
            for i in range(start, n + 1): # values from start to n (including n)
                comb.append(i) # add to the current comb
                backtrack(i + 1, comb)
                comb.pop()
            
        backtrack(1, [])
        return res






