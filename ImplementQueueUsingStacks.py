class MyQueue:

    def __init__(self):
        self.check = []
    def push(self, x: int) -> None:
        self.check.append(x)
    def pop(self) -> int:
        stack = []
        ele = self.check[0]
        for i in range(1, len(self.check)):
            stack.append(self.check[i])
        self.check = stack[::]
        return ele
    def peek(self) -> int:
        return self.check[0]
    def empty(self) -> bool:
        return len(self.check) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()