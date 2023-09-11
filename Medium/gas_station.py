class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Check if the total gas available is less than the total cost needed.
        # If so, it's impossible to complete the circuit, so return -1 immediately.
        if sum(gas) < sum(cost):
            return -1

        total = 0  # Keeps track of the net gas amount (gas - cost) while traveling.
        start = 0  # The starting index of the gas station.

        # Iterate through each gas station.
        for i in range(len(gas)):
            # Add the difference between gas and cost to the total.
            # This helps in determining if the car can move from this gas station to the next.
            total += (gas[i] - cost[i])

            # If total goes negative, it means the car can't reach from the previous starting point 
            # to this station, so set the next station as the new starting point.
            if total < 0:
                total = 0
                start = i + 1
            
        # If the loop completes, return the starting gas station's index.
        return start
