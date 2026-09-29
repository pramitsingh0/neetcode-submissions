class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        zipped = list(zip(profits, capital))
        zipped.sort(key=lambda z: z[1])
        
        maxHeap = []
        i = 0
        while k:
            while i < len(zipped) and zipped[i][1] <= w:
                heapq.heappush_max(maxHeap, zipped[i][0])
                i += 1

            if maxHeap:
                curProfit = heapq.heappop_max(maxHeap)
                w += curProfit
                k -= 1
            else:
                break
        return w
