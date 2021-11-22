import heapq as heap
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        idx = 0
        for i in range(k):
            x,y = points[i]
            heap.heappush(res,(-1*math.sqrt(x**2+y**2),i))
        for i in range(k,len(points)):
            x,y = points[i]
            if math.sqrt(x**2+y**2) < res[0][0]*-1:
                heap.heappop(res)
                heap.heappush(res,(-1*math.sqrt(x**2+y**2),i))
        result = []
        while len(res)>0:
            _,idx = heap.heappop(res)
            result.append(points[idx])
        return result