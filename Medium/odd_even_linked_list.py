"""
Problem Link: https://leetcode.com/problems/odd-even-linked-list/description/?envType=study-plan-v2&envId=leetcode-75

Note: You must solve the problem in O(1) extra space complexity and O(n) time complexity.

Approach: using 2 pointers.


"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        
        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head # Link the end of odd indexed nodes to the start of even indexed nodes
        return head

# list to linked list
def list_to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head

    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# linked list to list
def linked_list_to_list(head):
    arr = []
    while head: 
        arr.append(head.val)
        head = head.next
    return arr

def test_oddEvenList():
    sol = Solution()

    # Text Case 1
    head = list_to_linked_list([1, 2, 3, 4, 5])
    result = sol.oddEvenList(head)
    print(linked_list_to_list(result)) # Expected output:  [1, 3, 5, 2, 4]


test_oddEvenList()