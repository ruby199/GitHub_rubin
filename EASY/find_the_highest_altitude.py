"""
Problem Link: https://leetcode.com/problems/find-the-highest-altitude/description/?envType=study-plan-v2&envId=leetcode-75


"""

class Solution:
    def largestAltitude(self, gain) -> int:
        cur = 0
        highest = cur

        for altitude_gain in gain:
            cur += altitude_gain
            highest = max(highest, cur)
        
        return highest




sol = Solution()
gain = [-5,1,5,0,-7]
print(sol.largestAltitude(gain)) # Expected output: 1