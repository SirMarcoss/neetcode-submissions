class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # HEAP --> static heap --> min-heap
        res = []

        heap = []
        hashtable = {}

        for num in nums:
            if num not in hashtable:
                hashtable[num] = 1
            else:
                hashtable[num] += 1
        
        for t, v in hashtable.items():
            heapq.heappush(heap, (v, t))
        
        while len(heap) > k:
            heapq.heappop(heap)
        
        while heap:
            v, t = heapq.heappop(heap)
            res.append(t)
        
        return res

