class FreqStack:

    def __init__(self):
        self.countMap = {}
        self.groupMap = collections.defaultdict(list)
        self.maxCount = 0

    def push(self, val: int) -> None:
        self.countMap[val] = self.countMap.get(val, 0) + 1
        self.groupMap[self.countMap[val]].append(val)
        self.maxCount = max(self.maxCount, self.countMap[val])

    def pop(self) -> int:
        val = self.groupMap[self.maxCount].pop()
        self.countMap[val] -= 1
        if not self.groupMap[self.maxCount]: self.maxCount -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()