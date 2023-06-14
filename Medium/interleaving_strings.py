class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:


        # dynamic sol 

        if len(s1) + len(s2) != len(s3):
            return False

        # empty, initialized by dimension of False
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)] # dimension: len(s1 + s2) + 1 since we need outside layer
        dp[len(s1)][len(s2)] = True # corner value as True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dp[i + 1][j]: # inside bound, matches
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i + j] and dp[i][j + 1]:
                    dp[i][j] = True

        return dp[0][0]


        dp = {} # cashe (hash map)
        # k = i + j
        def dfs(i, j): # pass in 2 pointers
            if i == len(s1) and j == len(s2): # base case1. out of bound -> return True
                return True
            if (i, j) in dp: # base case2. Already in the dp cashe -> return result
                return dp[(i, j)] 
            
            # recursion
            if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j): # matches wth s1 => used the character from s1
                return True
            
            if j < len(s2) and s2[i] == s3[i + j] and dfs(i, j + 1): # matches with s2 => used the character from s2
                return True

            dp[(i, j)] = False # non matches 
            return False # no need to repeat the work again. 

        return dfs(0, 0) # start at the beginning of the both string. 


"""
        # recursive solution

        if len(s1) + len(s2) != len(s3):
            return False

        # empty, initialized by dimension of False
        dp = [[False] * (len(s2) + 1) for i in range(len(s1) + 1)] # dimension: len(s1 + s2) + 1 since we need outside layer
        dp[len(s1)][len(s2)] = True # corner value as True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j): # inside bound, matches
                    dp[i][j] = True
                if j < len(s2) and s2[i] == s3[i + j] and dfs(i, j + 1):
                    dp[i][j] = True

        return dp[0][0]
"""



