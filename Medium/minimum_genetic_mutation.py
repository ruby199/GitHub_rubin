"""
Problem Link: https://leetcode.com/problems/minimum-genetic-mutation/description/?envType=study-plan-v2&envId=top-interview-150


BFS Approach.
- imagine the problem as a graph. 
    - Each gene string is a node, and mutations are the edges. Two nodes have an edge (are neighbors) if they by differ by one character.
    - The added counstraints are that the characters must be one of "ACGT" and each node must be in bank. 

    --> Q. What is the "shortest path" between start and end? --> should use BFS not DFS
    
"""


from collections import deque


class Solution:
    def minMutation_wrong(self, startGene, endGene, bank) -> int:
        """
        This solution has a logical flaw but it is not correctly simulating the sequence of mutations from the startGene to the endGene using the bank. 
        """
        if len(startGene) != len(endGene) or not bank:
            return -1

        count = 0

        for i, (s_char, e_char) in enumerate(zip(startGene, endGene)):
            if s_char != e_char:
                temp_gene1 = startGene[:i] + e_char + startGene[i+1:]
                temp_gene2 = endGene[:i] + s_char + endGene[i+1:]

                if temp_gene1 in bank:
                    count += 1
                    
                if temp_gene2 in bank:
                    count += 1

        return count
    
    def minMutation_bfs(self, startGene, endGene, bank):
        queue = deque([(startGene, 0)]) # (node, count)
        seen = {startGene}

        while queue:
            node, steps = queue.popleft()
            if node == endGene:
                return steps
        
            # Try all possible mutations for the current gene
            for c in "ACGT":
                for i in range(len(node)): # iterate through all positions in the gene
                    neighbor = node[:i] + c + node[i + 1:] # Create new mutation (replace the character)
                    if neighbor not in seen and neighbor in bank:
                        queue.append((neighbor, steps + 1))
                        seen.add(neighbor)
        return -1



# Example usage
sol = Solution()
startGene = "AAAAACCC"
endGene = "AACCCCCC"
bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
# print(sol.minMutation(startGene, endGene, bank))  # should be 3
print(sol.minMutation_bfs(startGene, endGene, bank))  # should be 3