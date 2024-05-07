"""
Problem Link: https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/description/?envType=daily-question&envId=2024-05-07

Problem Description:
You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.
Return the head of the linked list after doubling it.

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def doubleIt(self, head):
        # Convert linked list to integer
        num = 0
        current = head
        while current:
            num = num * 10 + current.val
            current = current.next
        
        # Double the number
        num *= 2
        
        # Convert integer back to linked list
        # Handle the special case where the number is 0
        if num == 0:
            return ListNode(0)
        
        # Create a dummy node to simplify insertion logic
        dummy = ListNode(0)
        current = dummy

        while num > 0:
            current_digit = num % 10
            new_node = ListNode(current_digit)
            current.next = new_node
            current = new_node
            num //= 10
        
        # Reverse the linked list starting from dummy.next
        prev = None
        current = dummy.next
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev
    
    def doubleIt_stack(self, head):
        values = []
        val = 0

        while head is not None: # traverses the linked list
            values.append(head.val)
            head = head.next
        
        new_tail = None # to create a new linked list in reverse order

        while values or val != 0:
            new_tail = ListNode(0, new_tail)

            if values:
                val += values.pop() * 2
            new_tail.val = val % 10 # set to the last digit of val
            val //= 10 # to handle the carry
            
        return new_tail




# Testing the function
def test_doubleIt():
    def createLinkedList(values):
        dummy = ListNode()
        current = dummy
        for value in values:
            current.next = ListNode(value)
            current = current.next
        return dummy.next
    def linkedListToList(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        return result

    solution = Solution()
    
    # Test case 1
    head = createLinkedList([1, 8, 9])
    expected = [3, 7, 8]
    result = solution.doubleIt(head)
    assert linkedListToList(result) == expected, f"Test 1 failed: {linkedListToList(result)} != {expected}"

    # Test case 2
    head = createLinkedList([9, 9, 9])
    expected = [1, 9, 9, 8]
    result = solution.doubleIt(head)
    assert linkedListToList(result) == expected, f"Test 2 failed: {linkedListToList(result)} != {expected}"
    
    print("All tests passed!")

# Run tests
test_doubleIt()
