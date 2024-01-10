"""
Problem Link: https://leetcode.com/problems/find-k-closest-elements/

* Solution1. 

Binary Search for closest position:
    O(log n) time complexity, O(1) space complexity

Two-Pointer Technique:
    O(1) space complexity


Total time & space complexity:
    Time Complexity: O(log n + k)
    Space Complexity: O(k)

    
* Solution2. 

For solution2, the condition if x - arr[m] > arr[m + k] - x is crucial. 
It's comparing two distances:
    The distance from x to the start of the current window (arr[m]).
    The distance from x to the end of the current window (arr[m + k]).
This comparison determines whether the window should move to the right (if x is closer to arr[m + k]) or stay/move to the left (if x is closer to arr[m]).

Time Complexity: O(log(n - k))
Space Complexity: O(1)
"""

class Solution:
    # Runtime: Beats 90.06%of users with Python3
    # Memory: Beats 14.19%of users with Python3
    def findClosestElements(self, arr, k, x):
        # Edge cases
        # If target is bigger than the greatest element of the arrary
        if x > arr[-1]:
            return arr[-k:]

        # If target is smaller than the smallest element of the array
        if x < arr[0]:
            return arr[:k]

        # binary search to nevigate to the target position
        left, right = 0, len(arr) - 1
        
        while left < right:
            mid = (left + right) // 2
            if arr[mid] < x:
                left = mid + 1
            else:
                right = mid
                        
        # Initialize two pointers
        left, right = left - 1, left
        
        # Finding the k closest elements 
        res = []

        while k > 0:
            if left < 0: # No mre elemnts on the left
                res.append(arr[right])
                right += 1
            elif right >= len(arr) or (x - arr[left] <= arr[right] - x):
                res.append(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1
            k -= 1
        
        return sorted(res)

    # Runtime: Beats 92.97%of users with Python3
    # Memory: Beats 22.57%of users with Python3
    def findClosestElements_2(self, arr, k, x):
        l, r = 0, len(arr) - k

        while l < r:
            m = (l + r) // 2
            if x - arr[m] > arr[m + k] - x:
                l = m + 1
            else:
                r = m
        return arr[l:l+k]



sol = Solution()
print(sol.findClosestElements([1,2,3,4,5], 4, -1))
