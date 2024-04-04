"""
Problem Link: https://leetcode.com/problems/average-of-levels-in-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

Topics: Tree, DFS, BFS, Binary Tree


Breadth First Search 

1. Initialization: Enqueue the starting node into a queue & mark as visited
2. Exploration: While the queue is not empty
    - Dequeue a node from the queue and visit it(print the value)
    - For each unvisited neighbor of the dequeued node:
        - Enqueue the neighbor of the dequeued node:
            - Enqueue the neighbor into the queue
            - Mark the neighbor as visited
3. Termination: repeat exploration until the queue is empty

"""

# Definition for a binary tree node.
from cmath import log10
from collections import deque
from math import floor


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels_BFS(self, root):
        # Beats 93.88% of users with Python3
        # Time & memory complexity: O(n) since we are traversing each node once

        if not root:
            return []

        queue = deque([root])
        averages = []

        while queue:
            level_sum = 0
            level_count = len(queue)

            for _ in range(level_count):
                node = queue.popleft() # pop a node from the front of the queue

                # Add this node's value to the level sum
                level_sum += node.val
            
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
            average = level_sum/level_count
            averages.append(average)

        return averages


    def averageOfLevels_DFS(self, root):
        # Beats 75.29% of users with Python3
        if not root:
            return []
        
        def dfs(node, level, count, sums):
            if node is None:
                return 
            
            if level < len(sums):
                sums[level] += node.val
                count[level] += 1
            else:
                sums.append(node.val)
                count.append(1)
            
            dfs(node.left, level + 1, count, sums)
            dfs(node.right, level + 1, count, sums)
        
        counts = []
        sums = []
        
        dfs(root, 0, counts, sums)

        return [sums[i] / counts[i] for i in range(len(sums))]



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
root = build_tree([3,9,20,None,None,15,7])

print(sol.averageOfLevels_BFS(root)) # expected output: [3.00000,14.50000,11.00000]
print(sol.averageOfLevels_DFS(root)) # expected output: [3.00000,14.50000,11.00000]