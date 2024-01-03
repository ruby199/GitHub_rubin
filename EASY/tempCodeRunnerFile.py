        def dfs(node):
            # Base case:
            if not node:
                return True
            
            # Recursively check left & right subtrees
            left_balanced, left_height = dfs(node.left)
            right_balanced, right_height = dfs(node.right)

            # Check if the current node is balanced
            is_balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1

            # Calculate the height of the current node
            height = max(left_height, right_height) + 1

            return is_balanced, height

        return dfs(root)[0]