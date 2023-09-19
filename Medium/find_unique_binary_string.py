class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # Convert the list of binary strings into a set for O(1) lookup time.
        strSet = { s for s in nums }

        # Define a recursive function (backtracking) to explore all possible binary strings.
        def backtrack(i, cur):
            # Base case: If we've reached the end of the binary string we're building.
            if i == len(nums):
                # Convert the current list of characters to a string.
                res = "".join(cur)
                # Check if the built string exists in the nums set.
                # If it does, return None, indicating it's not a unique solution.
                # If it doesn't, return the string, indicating a unique solution.
                return None if res in strSet else res
            
            # Try keeping the current bit at position i as "0" and move to the next position.
            res = backtrack(i + 1, cur)
            # If the recursive call found a solution (a unique binary string), return it.
            if res: return res

            # Change the current bit at position i to "1".
            cur[i] = "1"
            # Try with the current bit as "1" and move to the next position.
            res = backtrack(i + 1, cur)
            # If the recursive call found a solution (a unique binary string), return it.
            if res: return res
        
        # Start the backtracking from position 0, with an initial binary string filled with "0"s.
        return backtrack(0, ["0" for s in nums])
