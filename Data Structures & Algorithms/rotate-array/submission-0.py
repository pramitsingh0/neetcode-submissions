class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_tmp = [0] * (len(nums))
        for i in range(len(nums)):
            new_ind = (i + k) % len(nums)

            nums_tmp[new_ind] = nums[i]
        
        for i in range(len(nums_tmp)):
            nums[i] = nums_tmp[i]