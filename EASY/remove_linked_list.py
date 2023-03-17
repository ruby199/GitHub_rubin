# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # create a dummy node
        dummy = ListNode(next=head)

        # dummy.next node will point to the head
        prev, curr = dummy, head

        while curr:
            nxt = curr.next # temp pointer

            if curr.val == val:
                prev.next = nxt # skip the curr if it's value, no need to update prev
            else:
                pre = curr 

            curr = nxt # go on...

        return dummy.next
        