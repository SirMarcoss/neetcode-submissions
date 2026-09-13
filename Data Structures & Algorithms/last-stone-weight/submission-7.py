class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #variable lenght --> heaviest stones --> maxHeap


        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if first < second:
                heapq.heappush(stones, first - second)
        
        if stones:
            return abs(stones[0])
        else:
            return 0






