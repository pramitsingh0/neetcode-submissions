class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_arr = []
        one_arr = []
        two_arr = []

        for n in nums:
            if n == 0:
                zero_arr.append(n)
            if n == 1:
                one_arr.append(n)
            if n == 2:
                two_arr.append(n)

        print(zero_arr, one_arr, two_arr)

        i = 0
        secondary_ind = 0
        while i < len(nums) and secondary_ind < len(zero_arr):
            nums[i] = zero_arr[secondary_ind]
            i += 1
            secondary_ind += 1
        
        secondary_ind = 0
        while i < len(nums) and secondary_ind < len(one_arr):
            nums[i] = one_arr[secondary_ind]
            i += 1
            secondary_ind += 1
        
        secondary_ind = 0
        while i < len(nums) and secondary_ind < len(two_arr):
            nums[i] = two_arr[secondary_ind]
            i += 1
            secondary_ind += 1

