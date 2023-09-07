# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = [] # to store right side view nodes
        q = collections.deque([root]) # deque with the root node for level order traversal (BSF)

        while q: # Loop through the level of the binary tree
            rightSide = None # Variable to keep track of the right most node at each level
            qLen = len(q) # number of the current level

            for i in range(qLen): # Loop through each node from the front of the queue. 
                node = q.popleft() # dequeue the node from the front of the queue
                if node: # if the dequeued node is not None
                    rightSide = node # update the right-most node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide: # If the right-most node was found, add its value to the result list
                res.append(rightSide.val)
        return res

