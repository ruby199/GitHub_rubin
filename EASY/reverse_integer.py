import math


class Solution:
    def reverse(x):
        # Integer.MAX_VALUE = 214748647 ( end with 7)
        # Integer.MIN_VALUE = -214748648 (end with -8)

        MIN = -214748648
        MAX = 214748647

        res = 0
        while x: #x not 0
            digit = int(math.fmod(x,10)) # because python computes -1 % 10 as 9
            x = int(x/10)

            # "//" : Integer Division 

            # test if overflow
            # case 1: Max/10 because we don't want to look at the last digit yet until we look at the every other digit
            if (res > MAX // 10 or (res == MAX // 10 and digit >= MAX % 10)): 
                return 0
            
            # case 2: if the result is exactly equal MAX / 10 && if the digit is greater than 7 (why 7? because if MAX%10 is 7) same with the MIN
            if (res < MIN // 10 or (res == MIN // 10 and digit <= MIN % 10)):
                return 0
            # add the digit and add it to the result
            res = (res * 10) + digit

        return res


result = Solution.reverse(1534239)
print(result)