class MinStack:
    # we want this four operations to work in constant time
    # stack (add, pop, top...) - array/linked list

    def __init__(self):
        self.stack = []
        self.minStack = []

        

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    # O(1) // by defult stack does not support this opperation
    def getMin(self) -> int:
        # looking one by one ==> O(n)
        # how can we do it in O(1)?
        # [Hint] Consider each node in the stack having a minimum value.
        return self.minStack[-1]


        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()