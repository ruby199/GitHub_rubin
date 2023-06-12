class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # time complexity O(n) since we only have to visit each node once

        # start at city 0
        # recursively check its neighbors
        # count outgoing edges
        
        # set instead of array because we want to check if city a can reach city b
        # get each connection and add into the hash set
        edges = {(a,b) for a, b in connections}

        # use hash map
        neighbors = {city: [] for city in range(n) }

        visit = set()
        changes = 0

        for a, b in connections:
            neighbors[a].append(b) # neighbors of a includes city b
            neighbors[b].append(a) # neighbors of b includes city a

        
        # traverse the graph (dfs recursively)
        def dfs(city):
            nonlocal edges, neighbors, visit, changes

            for neighbor in neighbors[city]:
                if neighbor in visit:
                    continue
                # check if this neighbor can reach city 0
                if (neighbor, city) not in edges:
                    changes += 1
                visit.add(neighbor)
                dfs(neighbor)



        visit.add(0)
        dfs(0)
        return changes


        