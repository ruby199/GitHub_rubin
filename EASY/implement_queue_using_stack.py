"""
Problem Link: https://leetcode.com/problems/implement-queue-using-stacks/solutions/4641109/beats-100-users-c-java-python-javascript-explained/?envType=daily-question&envId=2024-01-29

"""

class MyQueue_basic: # simple queue class

    def __init__(self):
        self.stack = []
        self.count = 0
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.count += 1

    def pop(self) -> int:
        self.count -= 1
        return self.stack.pop(0)

    def peek(self) -> int:
        return self.stack[0]
        

    def empty(self) -> bool:
        return self.count == 0
        

class MyQueue: # queue class using only two stacks
    """
    Time complexity:
    Enqueue (push): O(n)O(n)O(n)
    Dequeue (pop): O(1)O(1)O(1)
    Peek (peek): O(1)O(1)O(1)
    Empty Check (empty): O(1)O(1)O(1)
    (where n is the number of elements in the queue.)

    Space complexity:
    O(n)O(n)O(n)
    """

    def __init__(self):
        self.s1 = [] # acts as the primary stack for enqueue
        self.s2 = [] # helps in reversing the order of elements for efficient dequeuing

    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()




    def peek(self) -> int:
        return self.s1[-1]


    def empty(self) -> bool:
        return not self.s1
        




# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()