class Solution:
    def merge(nums1, m, nums2, n):
        # get the last index of nums1
        last = m + n - 1

        # merge in reverse order
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1

            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1 
        
        # take the remaining elements in nums2 and fill the rest
        while n > 0:
            nums1[last] = nums2[n-1]
            n, last = m - 1, last - 1
        
        print(nums1)


Solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)