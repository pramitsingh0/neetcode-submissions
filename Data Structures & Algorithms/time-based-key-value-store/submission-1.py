class TimeMap:

    def __init__(self):
        self.timeMap = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        res, val = "", self.timeMap.get(key, [])
        l, r = 0, len(val) - 1

        while l <= r:
            m = l + (r - l) // 2

            if val[m][1] == timestamp: return val[m][0]
            if val[m][1] < timestamp:
                res = val[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

        
