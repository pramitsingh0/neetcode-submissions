class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        """
        given a list of numbers, sort the list in ascending order;
        algorithm must be O(nlogn)
        Merge Sort
        """
        def mergeSort(nums: list[int]) -> list[int]:
            if (len(nums) <= 1):
                return merge(nums, [])
            else:
                mid = len(nums) // 2
                sortedLeftHalf = mergeSort(nums[:mid])
                sortedRightHalf = mergeSort(nums[mid:])
                return merge(sortedLeftHalf, sortedRightHalf)

        def merge(arr1: list[int], arr2: list[int]) -> list[int]:
            res = []
            i = 0
            j = 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] <= arr2[j]:
                    res.append(arr1[i])
                    i += 1
                else:
                    res.append(arr2[j])
                    j += 1

            while i < len(arr1):
                res.append(arr1[i])
                i += 1
            
            while j < len(arr2):
                res.append(arr2[j])
                j += 1
            return res

        return mergeSort(nums)