class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # O(n)
        arr = [0] * 1001

        for numPass, start, end in trips:
            arr[start] += numPass
            arr[end] -= numPass
        curCapacity = 0
        for i in range(1001):
            curCapacity += arr[i]
            if curCapacity > capacity: return False
        return True

        # O(nlogn)
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
