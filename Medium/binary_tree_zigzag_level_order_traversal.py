"""
Problem Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/?envType=study-plan-v2&envId=top-interview-150

Description:
- Given the root of a binary tree, return the zigzag level order traversal of its nodes' values(i.e. from left to right, then right to left for the next level and alternate between)
 
Approach: BFS (Breadth-First Search)


"""

# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        
        result = []
        q = deque([root])
        left_to_right = True # flag to keep track left->right / right->left

        while q:
            level_size = len(q)
            level_values = []

            for _ in range(level_size):
                node = q.popleft()
                level_values.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if not left_to_right:
                level_values.reverse()

            result.append(level_values)
            left_to_right = not left_to_right

        return result







# For testing the function
def build_tree_from_list(values):
    if not values:
        return None
    
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root


sol = Solution()

root = build_tree_from_list([3,9,20,None,None,15,7])

# Perform the zigzag level order traversal
print(sol.zigzagLevelOrder(root))