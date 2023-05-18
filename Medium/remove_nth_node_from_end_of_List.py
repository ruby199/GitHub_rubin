# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Using two pointers
        # Left, Right (shifted +2 until the right pointer is in the end of the list)
        dummy = ListNode(0, head) # value is not important, BUT the next should be set to the head
        left = dummy

        right = head # head + n, but as a loop
        while n > 0 and right:
            right = right.next
            n -= 1
        
        # until right reaches the end of the list
        # shift both pointers
        while right:
            left = left.next
            right = right.next

        # delete the node
        left.next = left.next.next
        
        return dummy.next
