class MyQueue:

    def __init__(self):
        self.queue = []
        self.helper = []

    def push(self, x: int) -> None:
        self.queue.append(x)
        

    def pop(self) -> int:
        for i in range(len(self.queue) - 1):
            self.helper.append(self.queue.pop())
        res = self.queue.pop()
        for i in range(len(self.helper)):
            self.queue.append(self.helper.pop())
        return res
        

    def peek(self) -> int:
        return self.queue[0]
        

    def empty(self) -> bool:
        return len(self.queue) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()