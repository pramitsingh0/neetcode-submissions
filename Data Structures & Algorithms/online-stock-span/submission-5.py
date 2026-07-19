class StockSpanner:

    def __init__(self):
        self.monotonicStack = []

    def next(self, price: int) -> int:
        span = 1

        while self.monotonicStack and self.monotonicStack[-1][0] <= price:
            span += self.monotonicStack.pop()[1]
        self.monotonicStack.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)