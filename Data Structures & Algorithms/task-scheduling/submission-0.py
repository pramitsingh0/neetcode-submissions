class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        countMap = {}
        for t in tasks:
            countMap[t] = countMap.get(t, 0) + 1
        
        maxHeap = list(countMap.values())
        heapq.heapify_max(maxHeap)
        q = collections.deque()
        time = 0
        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = heapq.heappop_max(maxHeap) - 1
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush_max(maxHeap, q.popleft()[0])
        return time