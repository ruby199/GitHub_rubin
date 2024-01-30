"""
Problem Link: https://leetcode.com/problems/insertion-sort-list/description/

Insertion Sort for singly-linked list. 

Time Complexity: O(n^2) # worse-case complexity, while best-case complexity is O(n)

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head):
        dummy = ListNode(0, head) # dummy -> head

        # prev is the last node in the sorted part of the list.
        # cur is the node to be inserted into the sorted part of the list.
        prev, cur = head, head.next 

        while cur:
            # cur is already in the correct position. Move prev, cur forward.
            if cur.val >= prev.val: 
                prev, cur = cur, cur.next 
                continue
            

            # Find the right place to insert cur. 
            tmp = dummy # tmp is the node after which cur should be inserted. 
            while cur.val > tmp.next.val:
                tmp = tmp.next
            
            prev.next = cur.next # remove cur from the current posiiton

            # insert cur between tmp and tmp.next
            cur.next = tmp.next 
            tmp.next = cur

            # Move cur to the next node in the unsorted part of the list
            cur = prev.next

        return dummy.next


##########################################################################

# Function to print the linked list
def printList(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

# Helper function to create a linked list from a list of values
def createList(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Test the code
lst = [4, 2, 1, 3]
head = createList(lst)
sorted_head = Solution().insertionSortList(head)
printList(sorted_head)  # Expected output: 1 2 3 4