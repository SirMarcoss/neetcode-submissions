class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # static heap --> minimum distance --> max-heap of the distance 

        maxHeap = []

        for x, y in points:
            distance = -(x ** 2 + y ** 2)
            heapq.heappush(maxHeap, [distance, x, y])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        res = []

        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x, y])
        
        return res

        
        
       




        