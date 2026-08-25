class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        given an aray of integers; produce a list of indices of two numbers such that they add up to target
        ASSUME: each input would have exactly one solution
        VARIANT: cannot use the same element twice
        """
        num_ind: dict = {}
        for i, n in enumerate( nums ):
            num_ind[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in num_ind and i != num_ind[diff]:
                return [i, num_ind[diff]]

        return []