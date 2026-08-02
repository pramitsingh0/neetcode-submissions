class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target: return True
            if nums[m] > nums[l]:
                # we're in the left sorted half
                if target < nums[m] and target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] < nums[l]:
                # we're in the right sorted half
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                # we can't determine in which half we're
                l += 1
        return False