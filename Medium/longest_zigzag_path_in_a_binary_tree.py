"""
Problem Link: https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root) -> int:
        self.max_length = 0

        def dfs(node, is_left, length):
            # Base case: 
            if not node:
                return
            
            self.max_length = max(self.max_length, length)
            
            if is_left:
                dfs(node.left, False, length + 1)
                dfs(node.right, True, 1)
            
            else:
                dfs(node.right, True, length + 1)
                dfs(node.left, False, 1)
            
            return self.max_length

        
        dfs(root, False, 0)
        return self.max_length


# For testing
def build_tree(nodes):
    """
    Builds a binary tree from a list of values ordered by level. None values represent missing nodes. 
    """
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    front = 0
    index = 1
    while index < len(nodes):
        node = queue[front]
        front += 1

        if nodes[index] is not None:
            node.left = TreeNode(nodes[index])
            queue.append(node.left)
        index += 1

        if index < len(nodes) and nodes[index] is not None:
            node.right = TreeNode(nodes[index])
            queue.append(node.right)
        index += 1

    return root



sol = Solution()
root = build_tree([1,None,1,1,1,None,None,1,1,None,1,None,None,None,1])
print(sol.longestZigZag(root)) # output: 3
