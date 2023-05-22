"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None : None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        
        return oldToCopy[head]

"""
In summary, this algorithm creates a deep copy of a linked list with random pointers by iterating through the original list twice. 

In the first iteration, it creates copies of each node and maps the original nodes to their copies using a dictionary. 

In the second iteration, it updates the next and random pointers of the copied nodes based on the mappings in the dictionary. 

This ensures that the copied list represents the same list state as the original list, and none of the pointers in the copied list point to nodes in the original list.

"""
