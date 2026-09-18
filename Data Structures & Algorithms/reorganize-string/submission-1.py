class Solution:
    def reorganizeString(self, s: str) -> str:
        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1
        
        maxHeap = []
        for k, v in count.items():
            maxHeap.append([v, k])
        heapq.heapify_max(maxHeap)
        
        prev = None
        res = ""
        while maxHeap or prev:
            if prev and not maxHeap:
                return ""
            
            cnt, char = heapq.heappop_max(maxHeap)
            res += char
            cnt -= 1
        
            if prev:
                heapq.heappush_max(maxHeap, prev)
                prev = None
            
            if cnt != 0:
                prev = [cnt, char]
            
        return res    

            