import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        siz = len(stones)
        if siz == 1:
            return stones[0]
        if siz == 0:
            return 0

        
        max_heap = stones
        heapq.heapify_max(max_heap)

        while len(max_heap) > 1:
            s1 = heapq.heappop_max(max_heap)
            s2 = heapq.heappop_max(max_heap)
            if s1 > s2:
                diff = s1 - s2
                heapq.heappush_max(max_heap,diff)
        
        max_heap.append(0)
        return max_heap[0]