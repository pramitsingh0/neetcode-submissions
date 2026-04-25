class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        given a listof numbers, of size n, return the majority element; majority element is the element that appears more than n / 2 times in the array. 
        ASSUME: Majority element always exists in the array
        """
        # One possible solution is create a hashmap of freq of nums in array and find the element with the largest frequence > n / 2
        candidate = nums[0]
        count = 0
        for n in nums:
            if count == 0:
                candidate = n
            if n == candidate:
                count += 1
            else:
                count -= 1
        return candidate