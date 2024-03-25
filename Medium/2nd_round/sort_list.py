"""
Problem Link: https://leetcode.com/problems/sort-list/description/?envType=study-plan-v2&envId=top-interview-150

Description: Given the head of a linked list, return the list after sorting it in ascending order.


Merge Sort (Divide and Conquer) - Top Down Merge Sort
- recursively splits the original list into two halves
- The split continues until there is only one node in the linked list(Divide phase)
- To spilt the list into two halves, we find the middle of the linked list using the Fast and Slow pointer approach as mentioned in Find Middle of Linked List/ 

- Recursively sort each sublist and combine it into a single sorted list (Merge Phase)


"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head):
        if not head or not head.next:
            return head
        
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp 

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)


    def getMid(self, head):
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


    def merge(self, list1, list2):
        tail = dummy = ListNode()
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(arr):
    dummy = ListNode(0)
    tail = dummy
    for val in arr:
        tail.next = ListNode(val)
        tail = tail.next
    return dummy.next

# Helper function to convert linked list to list
def linked_list_to_list(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

# Testing function
def test_sort_list(input_list, expected_output):
    sol = Solution()
    head = create_linked_list(input_list)
    sorted_head = sol.sortList(head)
    output_list = linked_list_to_list(sorted_head)
    if output_list == expected_output:
        print("Test Passed")
    else:
        print("Test Failed. Expected:", expected_output, "Got:", output_list)


# Example test
test_sort_list([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5])
test_sort_list([], [])
