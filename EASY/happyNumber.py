class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set() # hash set 

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True

        return False


    def sumOfSquares(self, n: int) -> int:
        # ToDo:

        # 19 --> 1^2+9^2=82, 19%10=9^2, 19/10=1^2
        # 1%10=0^2, 1/10=1

        output = 0

        while n:
            # take each digits and check
            digit = n % 10
            digit = digit ** 2 # square in python
            output += digit
            n = n // 10 # int division
        return output