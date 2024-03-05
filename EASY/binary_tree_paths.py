"""
Problem Link: https://leetcode.com/problems/binary-tree-paths/description/

Topics:
- Backtracking, Tree, Depth-First Search, Binary Tree

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        paths = []

        def dfs(cur, path):
            if not cur.left and not cur.right: # leaf node
                paths.append(path + str(cur.val))
                return

            path = path + str(cur.val) + "->"            
            
            if cur.left:
                # path = path + str(cur.left.val) + "->"
                dfs(cur.left, path)

            if cur.right:
                # path = path + str(cur.right.val) + "->"
                dfs(cur.right, path)

        dfs(root, "")
        return paths

def build_tree(nodes):
    """
    Builds a binary tree from a list of values ordered by level.
    None values represent missing nodes.
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
nodes1 = [1, 2, 3, None, 5]
root1 = build_tree(nodes1)
expected1 = ["1->2->5", "1->3"]

print(sol.binaryTreePaths(root1))