class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # do better than O(n) searching left to right
        # to log(n) by using "Binary Search"

        # Middle = (L+R)/2
        # check if the middle value is bigger/smaller than the curr

# Define the function with two parameters, a list of integers and a target integer to search for.
def binary_search(nums, target):
    # Define the left and right indices of the list.
    left_index, right_index = 0, len(nums)-1
        
    # While the left index is less than or equal to the right index.
    while left_index <= right_index:
        # Calculate the middle index of the list.
        middle_index = (left_index + right_index)//2

        # If the target is found at the middle index, return the index.
        if target == nums[middle_index]:
            return middle_index

        # If the target is greater than the middle element, search the right half of the list.
        if target > nums[middle_index]:
            left_index = middle_index + 1
        # If the target is less than the middle element, search the left half of the list.
        else:
            right_index = middle_index -1
            
        # if never reach the target
        return left_index





