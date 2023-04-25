class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute Force
        """
        res = 0

        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                area = (r - l) * min(height[l], height[r])
                res = max(res, area)
        return res
        """

        max_area = 0
        l, r = 0, len(height) - 1


        # Lineawr time solution: O(n)
        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area



