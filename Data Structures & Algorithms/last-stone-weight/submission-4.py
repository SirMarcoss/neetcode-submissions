class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # right child = 2i +2
        # continuos integration --> Max-Heap (two heaviest stones)
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones) # O(N)

        while len(stones) > 1:

            first = heapq.heappop(stones) 
            second = heapq.heappop(stones)

            if first < second:
                heapq.heappush(stones, first - second) # O(3 * log N)


        if stones:    
            return abs(stones[0])
        else:
            return 0

        
# space complexity O(1)
# time complexity O(N)