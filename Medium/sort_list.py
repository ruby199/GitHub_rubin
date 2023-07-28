# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return head

        sorted_list = []
        pt = head


        while pt:
            sorted_list.append(pt.val)
            pt = pt.next

        sorted_list.sort()

        pt = head

        print(sorted_list)

        for k in range(len(sorted_list)):
            pt.val = sorted_list[k]
            pt = pt.next
        
        return head


    def sortList_2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time Complexity: O(n logn)
        # Memory Complexity: O(1) 

        if not head or not head.next:
            return head

        # split the list into two halves
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
            tail = tail.next

        if list1:
            tail.next = list1

        if list2:
            tail.next = list2

        return dummy.next


    

# Test the function

def create_linked_list(values):
    # Create a singly-linked list from a list of values
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head            
def print_linked_list(head):
    # Helper function to print the linked list
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

def is_sorted_linked_list(head):
    # Helper function to check if the linked list is sorted
    current = head
    while current and current.next:
        if current.val > current.next.val:
            return False
        current = current.next
    return True

def test_sortList():
    test_cases = [
        [],                     # Empty list
        [1],                    # Single element
        [3, 1, 2, 4],           # Unsorted list
        [6, 4, 2, 7, 8, 5, 3],  # Another unsorted list
        [1, 2, 3, 4, 5],        # Already sorted list
    ]

    solution = Solution()
    for values in test_cases:
        head = create_linked_list(values)
        print("Original linked list:")
        print_linked_list(head)

        sorted_head = solution.sortList(head)
        print("Sorted linked list:")
        print_linked_list(sorted_head)

        assert is_sorted_linked_list(sorted_head), "Linked list not sorted correctly."

        print("Test passed.\n")

if __name__ == "__main__":
    test_sortList()