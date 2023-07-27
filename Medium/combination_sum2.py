class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # First, sort the input array candidates
        candidates.sort()

        res = [] # combinations that we are returning
        def backtrack(cur, pos, target): # Define a recursive backtracking function to find combinations
            # If the target is achieved, add the current combination to the result list
            if target == 0:
                res.append(cur.copy())
            # If the target becomes negative or zero, terminate the recursion for this branch
            if target <= 0:
                return 
            
            prev = -1  # Used to handle duplicates efficiently

            # Iterate over the candidates starting from the given position
            for i in range(pos, len(candidates)):
                # Skip duplicates to avoid duplicate combinations
                if candidates[i] == prev:
                    continue # skip

                # Add the current candidate to the combination
                cur.append(candidates[i])
                # Recursively explore the next candidates with the updated target value and position
                backtrack(cur, i + 1, target - candidates[i])
                # Backtrack by removing the last candidate to try other combinations
                cur.pop()
                # Update prev to the current candidate for handling duplicates
                prev = candidates[i]
        # Start the backtracking process with an empty combination, starting position 0, and the target value
        backtrack([], 0, target)
        return res
