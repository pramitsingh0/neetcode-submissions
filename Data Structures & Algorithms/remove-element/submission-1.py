class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        given a list of nums, remove the numbers that are equal to val in-place
        and return the size of the array after removing the vals
        """
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1


        return k