class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        minReach = []
        for d, s in zip(dist, speed):
            minute = math.ceil(d / s) # d=3, s=2, 3/2 = 1.5
            minReach.append(minute)
        
        minReach.sort()
        res = 0
        for minute in range(len(minReach)):
            if minute >= minReach[minute]:
                return res
            res += 1
        
        return res
