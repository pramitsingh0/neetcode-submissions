class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        def swap(arr: list[int], i: int, j: int):
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

        i = j = 0

        while i < len(nums1) and j < n:
            while nums1[i] < nums2[j] and i < m:
                i += 1
            r = m
            while r > i:
                nums1[r] = nums1[r - 1]
                r -= 1

            nums1[i] = nums2[j]
            j += 1
            m += 1
            