"""
Problem Link: https://leetcode.com/problems/design-circular-queue/description/

Two approaches:
    1. Array-base approach
    2. Linked List

"""

# Runtime: Beats 97.93% of users with Python3
# Memory: Beats 41.86% of users with Python3
class MyCircularQueue_Array:
    def __init__(self, k: int):
        self.queue = [0] * k
        self.max_size = k
        self.size = 0
        self.front = 0
        self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.max_size
        self.queue[self.rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.max_size
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size

# Runtime: Beats 72.46% of users with Python3
# Memory: Beats 7.42% of users with Python3
class ListNode:
    def __init__(self, val, next, prev):
        self.val, self.next, self.prev = val, next, prev

class MyCircularQueue_LinkedList:
    def __init__(self,k : int):
        self.space = k
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, None, self.left)
        self.left.next = self.right
    
    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        cur = ListNode(value, self.right, self.right.prev)
        self.right.prev.next = cur 
        self.right.prev = cur 
        self.space -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.left.next = self.left.next.next
        self.left.next.prev = self.left
        self.space += 1
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.left.next.val
    
    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.space == 0