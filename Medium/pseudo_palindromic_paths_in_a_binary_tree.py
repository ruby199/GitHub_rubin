"""
Problem Link: https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/description/?envType=daily-question&envId=2024-01-24


variable 'path' is used to track the current state ofthe path from the root node to the current node in a binary tree. 

The XOR operation (^) toggles the bit at this position in path: 
    - if the bit was 0, it becomes 1 (indicating an odd occurrence of that value)
    - if it was 1, it becomes 0 (indicating an even occurrence).
    A path is considered pseudo-palindromic if at most one of the values in the path occurs an odd number of times. 

 path & (path - 1) == 0 is a clever bit manipulation trick to check if at most one bit in path is set to 1


Example:
'path traversed in the tree: [1, 2, 2, 3]

    path = 0 (binary: 0000)

after node 1:
    path = 2 (binary: 0010)

after node 2:
    path = 6 (binary: 0110)

after node 2:
    path = 2 (binary 0010)

after node 3:
    path = 10 (binary 1010)

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths_list (self, root):
        # Time complexity: O(N * K), N is the number of nodes, K is the length of path
        # Space complexity: O(H), H is the tree height

        def isPseudoPalindromic(path):
            counts = {}
            for val in path:
                counts[val] = counts.get(val, 0) + 1
            
            odd_count = sum(count % 2 for count in counts.values())
            return odd_count <= 1

        def dfs(node, path):
            if not node:
                return 0
            
            # Append the current node's value to the path
            path.append(node.val)

            count = 0

            # If it's a leaf node, check if the path is pseudo-palindromic
            if not node.left and not node.right:
                if isPseudoPalindromic(path):
                    count = 1
            else:
                count += dfs(node.left, path)
                count += dfs(node.right, path)

            path.pop()

        return dfs(root, [])



    def pseudoPalindromicPaths_bit (self, root):
        # Time complexity: O(N), N is the number of nodes
        # Space complexity: O(H), H is the tree height
            # If tree is balanced: O(long(N)) space complexity but in worse case: O(N)
        count = 0
        
        stack = [(root, 0) ]
        while stack:
            node, path = stack.pop()
            if node:
                # Toggle the bit corresponding to the current node's value
                path = path ^ (1 << node.val)
                # Check if the current node is a leaf
                if not node.left and not node.right:
                    # Verify if the current path is pseudo-palindromic
                    # A path is pseudo-palindromic if at most one digit has an odd frequency
                    if path & (path - 1) == 0:
                        count += 1
                else:
                    # If not a leaf node, continue DFS traversal
                    # Add the right child to the stack if it exists
                    if node.right:
                        stack.append((node.right, path))
                    # Add the left child to the stack if it exists
                    if node.left:
                        stack.append((node.left, path))
        
        return count
    


    # Creating a simple binary tree
#       2
#      / \
#     3   1
# tree = TreeNode(2)
# tree.left = TreeNode(3)
# tree.right = TreeNode(1)

# Testing the function
# print(Solution().pseudoPalindromicPaths(tree))  # Expected output: 0



# Creating a more complex binary tree
#       2
#      / \
#     3   1
#    /   / \
#   3   1   1
tree = TreeNode(2)
tree.left = TreeNode(3)
tree.left.left = TreeNode(3)
tree.right = TreeNode(1)
tree.right.left = TreeNode(1)
tree.right.right = TreeNode(1)

# Testing the function
print(Solution().pseudoPalindromicPaths_bit(tree))  # Expected output: 3