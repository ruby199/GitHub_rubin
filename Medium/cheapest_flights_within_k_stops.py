class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Initialize a list to store the minimum prices from the source to each city. 
        # Initially set all the prices to infinity.
        prices = [float("inf")] * n
        
        # Set the source city price to 0 as there's no cost to travel from a city to itself.
        prices[src] = 0

        # Iterate up to k times. 
        # Each iteration considers an additional stop.
        for i in range(k + 1):
            # Create a copy of the current prices list to store updates for this iteration.
            tmpPrices = prices.copy()
            
            # For each flight (represented by source city 's', destination city 'd', and price 'p'),
            # check if we can find a cheaper price by using this flight.
            for s, d, p in flights:
                # If the price to the current source city is infinity, 
                # it means it's not reachable, so we skip this flight.
                if prices[s] == float("inf"):
                    continue
                # If the current price to the source city + the flight's price is cheaper than the current price 
                # to the destination city, update the temporary price for the destination city.
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p

            # After checking all flights for this iteration, update the main prices list.
            prices = tmpPrices
        
        # After k iterations, if the price to the destination city is still infinity,
        # it means the city is not reachable with up to k stops, so return -1.
        # Otherwise, return the found minimum price to the destination city.
        return -1 if prices[dst] == float("inf") else prices[dst]
