# Beats 72.71% of users with Python3
# Beats 17.58% of users with Python3
class Solutio1n:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        l, r = 0, len(x) - 1
        while l < r:
            if x[l] == x[r]:
                l += 1
                r -= 1
            else:
                return False
        return True



# Beats 86.84% of users with Python3
# Beats 17.58% of users with Python3
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
            
        x = list(str(x))
        l, r = 0, len(x) - 1
        while l < r:
            if x[l] == x[r]:
                l += 1
                r -= 1
            else:
                return False
        return True