import heapq
from typing import List

points = [[3,3],[5,-1],[-2,4]]
k=2

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for (x,y) in points:
            dist = x ** 2 + y**2
            heapq.heappush(heap,(dist,x,y))

        result = []


        for _ in range(K):
            (dist, x, y) = heapq.heappop(heap)
            result.append((x,y))

        return result

print(Solution.kClosest(Solution,points,k))





