from collections import deque
from typing import List

class LockingTree:
    
    def __init__(self, parent: List[int]):
        # The parent array representing the tree structure. 
        # parent[i] is the parent node of i, with parent[0] = -1 since it's the root.
        self.parent = parent
        
        # Array to track the user who has locked a specific node. 
        # None means the node is unlocked, otherwise it holds the user's ID.
        self.locked = [None] * len(parent)
        
        # A dictionary to track children for each node.
        self.child = { i : [] for i in range(len(parent)) }
        for i in range(1, len(parent)):
            self.child[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        # If the node is already locked, return False.
        if self.locked[num]: return False
        
        # Lock the node with the given user's ID.
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        # If the node is not locked by the given user, return False.
        if self.locked[num] != user: return False
        
        # Unlock the node.
        self.locked[num] = None
        return True

    def upgrade(self, num: int, user: int) -> bool:
        # Start at the given node and move up towards the root.
        # If any ancestor node is locked, return False.
        i = num 
        while i != -1: 
            if self.locked[i]:
                return False
            i = self.parent[i]
        
        # Count the locked descendant nodes and unlock them.
        lockedCount, q = 0, deque([num])
        while q:
            n = q.popleft()
            if self.locked[n]:
                self.locked[n] = None
                lockedCount += 1
            # Add children to the queue for BFS traversal.
            q.extend(self.child[n])
        
        # If there were any locked descendants, lock the current node.
        if lockedCount > 0:
            self.locked[num] = user
        return lockedCount > 0

# Sample usage of LockingTree
# obj = LockingTree(parent)
# param_1 = obj.lock(num, user)
# param_2 = obj.unlock(num, user)
# param_3 = obj.upgrade(num, user)
