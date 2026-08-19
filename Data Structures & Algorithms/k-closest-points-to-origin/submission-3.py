class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # static heap --> minimum distance --> max-heap of the distance 

        maxHeap = []

        for x, y in points:
            distance = -(x ** 2 + y ** 2)
            heapq.heappush(maxHeap, [distance, x, y])
        
        while len(maxHeap) > k:
            heapq.heappop(maxHeap)

            # we could not use the square root beacuse we don't want to return the distance
            # but we use it to solve the problem: 5 > 4 as well as sqrt(5) > sqrt(4)

        res = []

        while maxHeap:
            dis, x, y = heapq.heappop(maxHeap)
            res.append([x,y])
        
        return res

        
       




        