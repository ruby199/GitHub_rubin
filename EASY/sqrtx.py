class Solution:
    def mySqrt(self, x):
        if x < 2:
            return x
        
        l, r = 0, x

        while l <= r:
            mid = (l + r) // 2
            square = mid * mid
            if square > x:
                r = mid - 1
            elif square < x:
                l = mid + 1
            else:
                return mid
        
        return r # return r because when the loop ends, r is the largest number whose square is less than or eqaul to x


def test_mySqrt():
    solution = Solution()
    test_cases = [
        (4, 2),    # Square root of 4
        (8, 2),    # Square root of 8 (rounded down)
        (1, 1),    # Square root of 1
        (0, 0),    # Square root of 0 (edge case)
        (16, 4),   # Square root of 16
        (25, 5),   # Square root of 25
        (26, 5),   # Square root of 26 (rounded down)
        (100, 10), # Square root of 100
        (144, 12), # Square root of 144
        (99, 9),   # Square root of 99 (rounded down)
        (123456, 351), # Random larger number
    ]

    for x, expected in test_cases:
        result = solution.mySqrt(x)
        assert result == expected, f"Failed for {x}: Expected {expected}, got {result}"
    
    print("All tests passed!")

# Run the test function
test_mySqrt()