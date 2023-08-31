class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Nested helper function to calculate x raised to the power of n
        # x^-n = 1/ x^n
        def helper(x, n):
            # Base cases
            if x == 0: return 0
            if n == 0: return 1

            # Divide and conquer: reduce the power by half and solve it first
            res = helper(x, n // 2)
            # The answer for n would be square of the answer for n/2
            res = res * res
            # If n is odd, then x^n = x^(n//2) * x^(n//2) * x
            return x * res if n % 2 else res
        
        # Calculate the absolute value of the power first
        res = helper(x, abs(n))
        
        # If n was negative, take the reciprocal of the result
        return res if n >= 0 else 1 / res