class TimeMap:

    def __init__(self):
        self.timeMap = collections.defaultdict(list) # stores key value pairs in tuple


    def set(self, key: 
        str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.timeMap[key]
        l, r = 0, len(arr) - 1
        res = 0
        while l <= r:
            m = l + (r - l) // 2
            if arr[m][0] > timestamp:
                r = m - 1
            elif arr[m][0] < timestamp:
                res = max(m, res)
                l = m + 1
            else:
                return arr[m][1]
        return arr[res][1] if arr else ""
        
