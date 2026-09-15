class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        distancePointMap = collections.defaultdict(list)

        for x, y in points:
            distanceFromOrigin = math.sqrt(x ** 2 + y ** 2)
            distancePointMap[distanceFromOrigin].append([x, y])
            distances.append(distanceFromOrigin)
        
        heapq.heapify(distances)
        res = []
        while distances:
            closest = heapq.heappop(distances)
            arr = distancePointMap[closest]
            while arr:
                res.append(arr.pop())
                if len(res) == k:
                    return res
        return res