"""
Problem Link: https://leetcode.com/problems/divide-two-integers/

Approach 1: Repeated Subtraction
Approach 2: Repeated Exponential Searches

"""

class Solution:
    def divide_1(self, dividend: int, divisor: int) -> int:
        """
        Time Complexity: O(n)

        Time Limit Exceeded 11 / 994 testcases passed
        Last Executed Input
        dividend = 2147483647, divisor = 1
        """

        # Constants. (to handle overflow)
        MAX_INT = 2147483647  # 2**31 - 1
        MIN_INT = -2147483648  # -2**31

        # Special case; overflow case where the result would exceed the 32-bit signed integer range
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        
        if divisor > 0:
            negatives -= 1
            divisor = -divisor
        
        quotient = 0
        
        # Subtract divisor from dividend repeatedly until the dividend is less than the divisor
        while dividend <= divisor:
            dividend -= divisor
            quotient -= 1
        
        return -quotient if negatives != 1 else quotient
    
    def divide_2(self, dividend: int, divisor: int) -> int:
     # Constants.
        MAX_INT = 2147483647  # 2**31 - 1
        MIN_INT = -2147483648  # -2**31
        HALF_MIN_INT = -1073741824  # MIN_INT // 2

        # Special case: overflow.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        quotient = 0

        while divisor >= dividend:
            powerOfTwo = -1
            value = divisor
            # Check if double the current value is too big. If not, continue doubling.
            # If it is too big, stop doubling and continue with the next step */
            while value >= HALF_MIN_INT and value + value >= dividend:
                value += value
                powerOfTwo += powerOfTwo
            quotient += powerOfTwo
            dividend -= value

        return -quotient if negatives != 1 else quotient

def test_solution():
    solution = Solution()

    # Test cases
    test_cases = [
        (10, 3, 3),
        (7, -3, -2),
        (0, 1, 0),
        (1, 1, 1),
        (-1, -1, 1),
        (-10, 3, -3),
        (10, -3, -3),
        (-2147483648, -1, 2147483647),  # overflow case
        (-2147483648, 1, -2147483648),
        (2147483647, 1, 2147483647),
    ]

    for dividend, divisor, expected in test_cases:
        result = solution.divide_2(dividend, divisor)
        assert result == expected, f"Test failed for dividend={dividend}, divisor={divisor}. Expected={expected}, got={result}"

    print("All test cases passed!")

# Run the test function
test_solution()