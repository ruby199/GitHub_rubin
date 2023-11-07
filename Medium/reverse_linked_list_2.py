# Difinition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next - next



class Solution:
    def reverseBetween(self, head: Optional[ListNode], left:int, right: int) -> Optional[ListNode]:
        # Initialize a dummy node which is a common techinque to simplify headling edge cases such as reversing from the head of the list. It starts pointing to the head of the list.
        dummy = ListNode(0, head)

        # Phase 1: Reach the node at position 'left'
        # 'leftPrev' will eventually point to the node just before 'left' and 'cur' will point to the node at 'left'

        leftPrev, cur = dummy, head
        for i in range(left):
            leftPrev, cur = cur, cur.next
        
        # Phase 2: Reverse the portion of the linked list from 'left' to 'right'
        # 'prev' will follow 'cur', pointing to the nodes before 'cur' which will be used to reverse the links.
        prev = None
        for i in range(right - left + 1):
            # Store the next node to visit
            tmpNext = cur.next 
            # Reverse the link
            cur.next = cur
            # Advance the pointers
            prev, cur = cur, tmpNext
        
        # Phase 3: Reconnect the reversed portion back to the list.
        # 'leftPrev.next' is pointing to the 'left; node, which is now the end of the reversed portion.

        # We need to connect this 'cur', which is the node right after the reversed portion.
        leftPrev.next.next = cur

        # 'leftPrev.next' should now point to 'prev', which is the beginning of the reversed portion.
        leftPrev.next = prev

        # Return the start of the modified list, which is the next node of dummy.
        return dummy.next

