class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        res = []
        num_count = [[] for _ in range(len(nums) + 1)]
        n_freq = {}
        for n in nums:
            n_freq[n] = n_freq.get(n, 0) + 1

        for key, val in n_freq.items():
            num_count[val].append(key)

        for i in range(len(num_count) - 1, 0, -1):
            for num in num_count[i]:
                res.append(num)
                if (len(res) == k):
                    return res

        return res