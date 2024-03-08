
            # Base case
            if not cur.left and not cur.right and remaining_sum == cur.val:
                paths.append(path)
                return

            # append current node's value
            path.append(cur.val)

            dfs(cur.left, path, remaining_sum = cur.val)
            dfs(cur.right, path, remaining_sum = cur.val)

