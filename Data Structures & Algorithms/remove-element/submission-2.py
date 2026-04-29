class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        k = 0
        j = len(nums) - 1

        while i <= j:
            if (nums[i] != val):
                k += 1
                i += 1
            else:
                nums[i] = nums[j]
                j -= 1
            
        return k
        