"""
Problem Link: https://leetcode.com/problems/online-stock-span/description/

Approach: Monotonic Stack Solution
- Use stack and store the pair of the price and its span.
- Time Complexity: O(n) // Because the operation only includes adding to the list or removing from the list.

"""


# 1st approach: Time Limit Exceeded
# Stored the price value and used pointer to compare every single value from the stored prices
# 'next' method's memory complexity: O(n), Runtime Complexity: O(n) time per call. However, the complexity accumulates with each call
# If 'next' is called 'n' times, the total time complexity over all calls is O(n^2) as it iterate through all the elements added so far. 
class StockSpanner1:

    def __init__(self):
        self.prices = []
        
    def next(self, price: int) -> int:
        self.span = 0 
        self.prices.append(price)
        
        for left in range(len(self.prices) - 1, -1, -1):
            if self.prices[left] <= price:
                self.span += 1
            else:
                break
        return self.span


# 2nd approach: Using Stack
# Runtime:Beats 92.83% of users with Python3
# Memory: Beats 42.92% of users with Python3
class StockSpanner2:

    def __init__(self):
        self.prices = [] # stack of pairs of: (price, span)

    def next(self, price: int) -> int:
        span = 1  # Initial span for the current price
        # Pop from the stack as long as the stack is not empty and the top price is less than or equal to the current price
        while self.prices and self.prices[-1][0] <= price:
            span += self.prices.pop()[1] # Add the span of the popped prices to the current span
        self.prices.append((price, span)) # Push the current price and its span to the stack
        return span


        



# obj = StockSpanner()
# param_1 = obj.next(price)

