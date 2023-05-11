class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            # base case
            if i >= len(s):
                res.append(part.copy())
                return 

            # have not reach the last index.
            for j in range(i, len(s)): # every possible substring
                if self.isPail(s, i, j):
                    part.append(s[i:j+1]) # add this current partition
                    dfs(j + 1)
                    part.pop() # clean up from our partition list

        dfs(0)
        return res

    def isPail(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True 
            