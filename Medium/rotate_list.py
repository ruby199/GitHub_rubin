# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=Node):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # linear time complexity
        
        if not head:
            return head
        
        # Get length
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1
        
        k = k % length
        if k == 0:
            return head
        
        # Move to the pivot and rotate
        cur = head
        for i in range(length - k - 1):
            cur = cur.next
        newHead = cur.next
        cur.next = None # pivot position
        tail.next = head
        return newHead
