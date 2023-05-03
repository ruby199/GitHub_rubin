class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:    
        # time complexity: O(#edge + #node) = O(#prereq + #course)
        # build adjacency list of prereqs
        prereq = { c:[] for c in range(numCourses) } # for every course create an empty list
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        # a course has 3 possible states:

        # visited -> crs has been added to output

        # visiting -> crs not added to output, but added to cycle
        # unvisited -> crs not added to output or cycle

        output = []
        visit, cycle = set(), set()
        def dfs(crs):
            if crs in cycle: # we visited twice
                return False 
            if crs in visit: # we don't need to visit twice
                return True
            
            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False: # cycle
                    return False
                
            cycle.remove(crs) # no longer along the path we are going
            visit.add(crs) # if the course has been visited add!
            output.append(crs)
            
            return True
                
        # go through every single course
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        
        return output