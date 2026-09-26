class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t: t[1])
        minHeap = []
        curCapacity = 0
        for numPass, start, end in trips:
            while minHeap and minHeap[0][0] <= start:
                end2, numPass2 = heapq.heappop(minHeap)
                curCapacity -= numPass2
            
            curCapacity += numPass
            if curCapacity > capacity:
                return False
            heapq.heappush(minHeap, [end, numPass])
        return True
