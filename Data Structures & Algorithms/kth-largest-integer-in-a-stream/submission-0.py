class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap) # O(N)

        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap) # O(log N)
        

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val) #(log N)
        else:
            heapq.heappushpop(self.min_heap, val)
        
        return self.min_heap[0]
        
