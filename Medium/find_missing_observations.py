class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # n: missing values, m: given values (length of the rolls)
        # Calculate the total sum of missing rolls
        m = len(rolls)
        nTotal = (mean * (n + m)) - sum(rolls)

        # Check if the solution is possible
        if nTotal < n or nTotal > n * 6: # range of the smallest / largest total value
            return []
        
        res = []

        # Distribute the sum among the missing rolls
        while nTotal:
            dice = min(nTotal - n + 1, 6)
            res.append(dice)
            nTotal -= dice
            n -= 1
        
        return res
