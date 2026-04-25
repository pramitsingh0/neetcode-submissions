class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        given a listof numbers, of size n, return the majority element; majority element is the element that appears more than n / 2 times in the array. 
        ASSUME: Majority element always exists in the array
        """
        # One possible solution is create a hashmap of freq of nums in array and find the element with the largest frequence > n / 2
        numFreq: dict = {}
        res = -1
        sizeLon = len(nums)
        for n in nums:
            numFreq[n] = numFreq.get(n, 0) + 1

        for k, v in numFreq.items():
            if v > sizeLon / 2:
                res = max(k, res)
        return res