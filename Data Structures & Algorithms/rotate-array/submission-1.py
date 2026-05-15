class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        count = 0
        current = start = 0

        while count < n:
            current = start
            prev = nums[start]
            while True:
                new_ind = (current + k) % n
                prev, nums[new_ind] = nums[new_ind], prev
                current = new_ind
                count += 1

                if current == start:
                    break
            
            start += 1