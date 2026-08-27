class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(nums: List[int]):
            l, r = 0, len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    return m
            return -1
        l, r = 0, len(nums) - 1
        if nums[l] <= nums[r]:
            return binarySearch(nums)
        while l <= r:
            m = (l + r) // 2

            if target > nums[m]:
                if target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            elif target < nums[m]:
                if target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                return m
        return -1