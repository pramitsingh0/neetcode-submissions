class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        res = 0
        while k > 0:
            res = heapq.heappop_max(nums)
            k -= 1
        return res