"""
Problem Link: https://leetcode.com/problems/merge-k-sorted-lists/description/

Description: You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.


Approach 1: Brute Force
- merge everything and sort the list

Approach 2: Compare one by one (divide and conquer)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists_bruteForce(self, lists): 
        # edge case
        if not lists:
            return None
        
        nodes = []
        head = point = ListNode(0)

        for l in lists:
            while l != None:
                nodes.append(l.val)
                l = l.next

        nodes.sort()

        for x in nodes:
            point.next = ListNode(x)
            point = point.next
        
        return head.next


    def mergeKLists_optim(self, lists): # divide and conquer

        def mergeTwoLists(l1, l2):
            dummy = ListNode(0)
            tail = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next

                else:
                    tail.next = l2
                    l2 = l2.next

                tail = tail.next
            tail.next = l1 or l2

            return dummy.next
        

        n = len(lists)
        interval = 1

        while interval < n:
            for i in range(0, n - interval, interval * 2):
                lists[i] = mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        
        return lists[0] if n > 0 else None
    




# sol = Solution()
# lists = [[1,4,5],[1,3,4],[2,6]]
# print(sol.mergeKLists(lists)) # expected output: [1,1,2,3,4,4,5,6]
        
#### Testing function for the mergeKLists created by the GPT ###
def array_to_linked_list(arr):
    """ Helper function to convert array to linked list """
    head = point = ListNode(0)
    for num in arr:
        point.next = ListNode(num)
        point = point.next
    return head.next

def linked_list_to_array(node):
    """ Helper function to convert linked list back to array """
    array = []
    while node:
        array.append(node.val)
        node = node.next
    return array

def test_mergeKLists():
    # Test setup
    sol = Solution()
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    linked_lists = [array_to_linked_list(lst) for lst in lists]

    # Function call
    merged_list = sol.mergeKLists_optim(linked_lists)

    # Convert result back to array to compare
    result = linked_list_to_array(merged_list)
    
    # Expected result
    expected = [1, 1, 2, 3, 4, 4, 5, 6]
    
    # Assertion
    assert result == expected, f"Test failed: Expected {expected}, got {result}"
    print("Test passed!")

test_mergeKLists()