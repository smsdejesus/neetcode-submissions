import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for i in range(len(points)):
            x = points[i][0]
            y = points[i][1]

            dist = math.sqrt((x**2) + (y**2))
            heapq.heappush(minHeap,(dist,points[i]))
        
        ans = []
        for n in range(k):
            tup = heapq.heappop(minHeap)
            ans.append(tup[1])

        return ans