class StockSpanner:
    def __init__(self):
        self.p = [None]
        self.i = [0]

    def next(self, price: int) -> int:
        index = 1
        while self.p[-1] and price >= self.p[-1]:
            index += self.i[-1]
            self.p.pop()
            self.i.pop()
        self.i.append(index)
        self.p.append(price)
        return self.i[-1]


# Your StockSpanner object will be instantiated and called as such:

# obj = StockSpanner()
# param_1 = obj.next(price)
