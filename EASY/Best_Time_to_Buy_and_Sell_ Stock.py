class Solution:
    def maxProfit(prices):
        # Buy Low and Sell High
        # Two pointer (left & Right) 
        # Left: Day we buy, Right: Day we sell
        # memory O(1), Time O(n)

        l, r = 0, 1 # left = buy, right = sell
        maxProfit = 0
        
        while r < len(prices):
            # profitable ? 
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1
        return maxProfit

print(Solution.maxProfit([7,1,5,3,6,4]))