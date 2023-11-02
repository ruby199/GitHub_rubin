class Solution:
    def maxLength(self, arr: List[str]) -> int:
        max_ans = 0

        def isUnique(s):
            return len(s) == len(set(s))

        def backtrack(index, path):
            nonlocal max_ans  # Declare that max_ans is not local to this function
            if index == len(arr):
                max_ans = max(max_ans, len(path))  # Modify the outer scope max_ans
                return

            # If the path with the current string is unique, choose to include it
            if isUnique(path + arr[index]):
                backtrack(index + 1, path + arr[index])
            
            # Always choose to exclude the current string as another path
            backtrack(index + 1, path)

        backtrack(0, "")
        return max_ans
