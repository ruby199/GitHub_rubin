class Solution:
    # Function to determine if matchsticks can form a square
    def makesquare(self, matchsticks: List[int]) -> bool:
        # Calculate the length of each side of the square
        length = sum(matchsticks) // 4
        # Initialize four sides of the square with a length of 0
        sides = [0] * 4
        
        # Check if the total length of matchsticks is divisible by 4, if not return False
        if sum(matchsticks) % 4 != 0:
            return False

        # Sort the matchsticks in descending order
        matchsticks.sort(reverse=True)

        # Define a backtrack function to try different combinations
        def backtrack(i):
            # If all matchsticks are used, return True
            if i == len(matchsticks):
                return True
            
            # Try adding the current matchstick to each side
            for j in range(4):
                # Check if adding the matchstick does not exceed the side length
                if sides[j] + matchsticks[i] <= length:
                    # Add the matchstick to the current side
                    sides[j] += matchsticks[i]
                    # Recursively call backtrack for the next matchstick
                    if backtrack(i + 1):
                        return True
                    # Backtrack: remove the matchstick from the current side
                    sides[j] -= matchsticks[i]
            # If no valid combination is found, return False
            return False
        
        # Start the backtrack process with the first matchstick
        return backtrack(0)
