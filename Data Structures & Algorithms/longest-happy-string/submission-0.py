class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        maxHeap = []

        for cnt, char in [(a, "a"), (b, "b"), (c, "c")]:
            if cnt:
                heapq.heappush_max(maxHeap, (cnt, char))
        
        while maxHeap:
            cnt, char = heapq.heappop_max(maxHeap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break
                cnt2, char2 = heapq.heappop_max(maxHeap)
                cnt2 -= 1
                res += char2
                if cnt2:
                    heapq.heappush_max(maxHeap, (cnt2, char2))
            else:
                res += char
                cnt -= 1
            if cnt:
                heapq.heappush_max(maxHeap, (cnt, char))
        return res