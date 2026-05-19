class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = j = 0
        while i < len(nums) and j < len(nums):
            if i != j and nums[i] == nums[j]:
                if abs(i - j) <= k:
                    return True
                else:
                    i += 1
            else:
                if abs(i - j) >= k:
                    i += 1
                else:
                    j += 1
        return False