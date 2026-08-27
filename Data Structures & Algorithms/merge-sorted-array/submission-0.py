class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # basically it's given that len(nums1) = m + n
        # we have to put num2 in num1 and sort them in place
        def swap(arr: list[int], i: int, j: int):
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

        i = j = 0

        while i < len(nums1) and j < n:
            if nums1[i] == 0 or nums1[i] > nums2[j]:
                swap(nums1, i, m)
                nums1[i] = nums2[j]
                j += 1
                m += 1

            i += 1