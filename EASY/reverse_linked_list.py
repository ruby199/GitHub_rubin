# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(head):
        # Use two pointers (curr, prev)
        # prev -> curr, curr -> next
        prev, curr = None, head
        temp = ListNode()
        while curr:
            nxt = curr.next # temp variable to store current next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
                
# memory complexity: O(1)
# time complexity: O(n)

# Solution #2

# class Solution:
#     def reverseList(self, head:ListNode) -> ListNode:
#         # recursive: T O(n), < O(n)

#         if not head:
#             return None
        
#         newHead = head
#         if head.next:
#             newHead = self.reverseList(head.next)
#             head.next.next = head
#         head.next = None

#         return newHead
