class MedianFinder:

    def __init__(self):
        self.small = [] # maxHeap
        self.large = [] # minHeap
        self.size = 0
        
    def isBalanced(self) -> bool:
        return abs(len(self.large) - len(self.small)) <= 1
    
    def balance(self):
        # wherever is bigger, pop element from them and push to other.
        if len(self.small) > len(self.large):
            ele = heapq.heappop_max(self.small)
            heapq.heappush(self.large, ele)
        elif len(self.small) < len(self.large):
            ele = heapq.heappop(self.large)
            heapq.heappush_max(self.small, ele)


    def addNum(self, num: int) -> None:
        if not self.large:
            self.large.append(num)
            return
        if num >= self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush_max(self.small, num)
        
        if not self.isBalanced():
            self.balance()
        

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return float(self.large[0])
        elif len(self.large) < len(self.small):
            return float(self.small[0])
        else:
            ele1 = self.large[0]
            ele2 = self.small[0]
            return (ele1 + ele2) / 2

        
        