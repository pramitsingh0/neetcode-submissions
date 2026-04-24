from collections import defaultdict
class Solution:
    def groupAnagrams(self, los: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for s in los:
            charCount = [0] * 26
            for c in s:
                charCount[ord(c) - ord("a")] += 1
            
            res[tuple(charCount)].append(s)
        return [s for s in res.values()]