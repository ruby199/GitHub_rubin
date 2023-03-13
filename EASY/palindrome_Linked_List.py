# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# Solutions:
# 1. Put the items in an array then use left right pointers at each end, moving them towards each other to check for palindromes, this is O(n) space as it needs extra array
# 2. For o(1) space, keep it as linkedlist and again use two pointers, but first you have to reverse the second half of the linkedlist to be able to traverse it from the end to the middle. How do you get a pointer to the midpoint of the linkedlist? Efficient way: use fast and slow pointers, when the fast pointer reaches the end the slow pointer will be at midpoint.
# You can apply reverse linkedlist algorithm with the head being the midpoint of the linkedlist

class Solution:
    def isPalindrome(head):
        # put inside the array (using index) instead of using linked list --> we need extra memory
        # can you do it in O(n) time and O(n) space? -> meaning without using extra array

        nums = []

        while head: # not end of the ist
            nums.append(head.val) # add every single value
            head = head.next

        l, r = 0, len(nums) - 1

        while l <= r: # pointers not crossed each other
            # check palindrome
            if nums[l] != nums[r]:
                return False
            # update our pointers
            l += 1
            r -= 1


        return True

class Solution2:
    def isPalindrome(head):
        # Use Fast pointer & Slow pointer
        fast = head
        slow = head

        # find middle (slow) ***
        # while fast is not null, fast.next is not null - keep going until fast is either at the last node or has reached null
        while fast and fast.next:
            fast = fast.next.next #next's next 
            # slow pointer swifts only once
            slow = slow.next

        # reverse second half
        prev = None
        # start at slow and keep going until we reach end of the list
        while slow:
            # we are going to update our pointer so save the next val into a temp variable
            tmp = slow.next
            slow.next = prev # we want to be null
            prev = slow
            slow = tmp # which is the next node

        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True