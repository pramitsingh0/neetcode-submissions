class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            # we pop the two heaviest element
            ele1 = heapq.heappop_max(stones)
            ele2 = heapq.heappop_max(stones)
            res = 0
            # then we smash them
            if ele1 == ele2:
                res = 0
            elif ele1 < ele2:
                res = ele2 - ele1
            else:
                res = ele1 - ele2
            
            if res:
                heapq.heappush_max(stones, res)
        
        return stones[0] if len(stones) else 0