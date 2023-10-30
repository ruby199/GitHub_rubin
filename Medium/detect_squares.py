from ast import List
from collections import defaultdict

# Class to detect squares formed by points added
class DetectSquares:

    # Initializer for the class
    def __init__(self):
        # Use defaultdict to count occurrences of each point 
        self.ptsCount = defaultdict(int)
        # List to store all the points added
        self.pts = []

    # Function to add a point to the list and update its occurrence count
    def add(self, point: List[int]) -> None:
        # Increase the count for the given point
        self.ptsCount[tuple(point)] += 1
        # Append the point to the list
        self.pts.append(point)

    # Function to count how many squares can be formed using the provided point as one of its vertices
    def count(self, point: List[int]) -> int:
        # Result variable to keep the count of squares
        res = 0
        # Unpack the point into x and y coordinates
        px, py = point
        # Loop through all the stored points
        for x, y in self.pts:
            # Check if the point is not diagonal or is the same as the given point, 
            # if so, skip the current iteration
            if (abs(py - y) != abs(px -x)) or x == px or y == py:
                continue
            # If the two diagonal points for a square exist, add their product 
            # to the result (this accounts for multiple overlapping squares)
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        # Return the total count of squares
        return res


# DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)