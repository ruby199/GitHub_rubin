class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # Using two pointers

        """
        left, right = 0, len(s) - 1

        while left <= right:
            temp = s[left]            
            s[left] = s[right]
            s[right] = temp

            left += 1
            right -= 1

        """
        # using stack
        # Time: O(n) Space(n)

        """
        stack = []
        for c in s:
            stack.append(c)
        i = 0
        while stack:
            s[i] = stack.pop()
            i += 1
        """

        # reversive method (using l, r pointer)
        def reverse(l, r):
            if l < r:
                s[l], s[r] = s[r], s[l]
                reverse(l+1, r-1)
        reverse(0, len(s) - 1)










