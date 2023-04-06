class Solution:
    def arrangeCoins(self, n: int) -> int:

        # brute force solution O(n)
        '''
        left = n
        count = 0
        i = 0

        while left >= i+1:
            i += 1
            left -= i
            count += 1
        
        return count
        '''

        # better solution O(logn)

        l, r = 1, n
        res = 0

        while l <= r:
            mid = ( l + r ) // 2
            coins = (mid / 2) * (mid + 1) #  / means decimal division in python
            if coins > n:
                r = mid - 1
            else:
                l = mid + 1
                res = max(mid, res)

        return res