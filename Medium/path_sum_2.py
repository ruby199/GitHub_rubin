"""
Problem Link: https://leetcode.com/problems/path-sum-ii/description/


Problem Description:

    Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

    A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.


Topics: #backtracking #Tree #Depth-First Search #Binary Tree
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root, targetSum):

        if not root:
            return []

        paths = []

        def backtrak(cur, path, remaining_sum):
            if cur is None:
                return

            # append current node's value
            path.append(cur.val)            

            # Base case
            if not cur.left and not cur.right and remaining_sum == cur.val:
                paths.append(path.copy()) #  create a shallow copy of the current path list
                return

            backtrak(cur.left, path, remaining_sum - cur.val)
            backtrak(cur.right, path, remaining_sum - cur.val)
            
            path.pop()

            
        backtrak(root, [], targetSum)
        return paths



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
root = build_tree([5,4,8,11,None,13,4,7,2,None,None,5,1])


targetSum = 22
print(sol.pathSum(root, targetSum)) # Expected: [[5,4,11,2],[5,8,4,5]]


