"""
Problem Link: https://leetcode.com/problems/course-schedule/?envType=study-plan-v2&envId=top-interview-150


DFS.


"""

class Solution:
    def canFinish(self, numCourses, prerequisites):
        preMap = {i:[] for i in range(numCourses)}

        for pre, crs in prerequisites:
            preMap[crs].append(pre)
        
        visitSet = set()
        
        def dfs(crs):
            if crs in visitSet:
                return False
            
            if preMap[crs] == []:
                return True
            
            visitSet.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre): return False
            
            visitSet.remove(crs)
            preMap[crs] = []
            return True


        for crs in range(numCourses):
            if not dfs(crs): return False
            
        return True


sol = Solution()
numCourses = 2
prerequisites = [[1, 0]]
print(sol.canFinish(numCourses, prerequisites))




