class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        given a list of nums, remove the numbers that are equal to val in-place
        and return the size of the array after removing the vals
        """
        n = len(nums)

        i = 0
        while i < n:
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
            else:
                i += 1


        return n