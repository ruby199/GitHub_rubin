class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Combine position and speed into pairs
        pair = [[p, s] for p, s in zip(position, speed)]

        # Initialize an empty stack to keep track of the fleets
        stack = []
        # Iterate over the car position-speed pairs in reverse-sorted order
        # This means we start from the car closest to the destination
        for p, s in sorted(pair)[::-1]: # Sorting and then reversing the list
            # Calculate time to reach the target for each car
            # and add it to the stack
            stack.append((target - p) / s)

            # Check if the last two elements in the stack form a fleet
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                # if the last car (newly added) can reach the target in the same or less time than the second last car, they form a fleet. 
                # Remove the last car from the stack as it's now part of a fleet. 
                stack.pop()
        # The remaining elements in the stack represent individual fleets
        return len(stack)