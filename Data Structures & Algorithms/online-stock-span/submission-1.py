class StockSpanner:

    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        count = 1
        j = len(self.stocks) - 1
        while j >= 0 and self.stocks[j] <= price:
            count += 1
            j -= 1
        self.stocks.append(price)
        return count
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)