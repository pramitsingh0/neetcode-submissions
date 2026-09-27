class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        zipped = list(zip(profits, capital))

        zipped.sort(key=lambda z: z[1])

        profit = 0
        i = 0
        maxHeap = []
        while k:
            while i < len(zipped) and zipped[i][1] <= w:
                heapq.heappush_max(maxHeap, zipped[i])
                i += 1
            
            if maxHeap:
                estProfit, reqCapital = heapq.heappop_max(maxHeap)
                profit += estProfit
                w += estProfit
                k -= 1
            else: break


        return w

            
