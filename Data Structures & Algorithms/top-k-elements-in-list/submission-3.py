class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtable = {}
        res = []

        for num in nums:
            if num not in hashtable:
                hashtable[num] = 1
            else:
                hashtable[num] += 1
        
        arr = [(freq, num) for num,freq in hashtable.items()]
       

        heapq.heapify(arr)
        
        while len(arr) > k:
            heapq.heappop(arr)
        
        for freq,num in arr:
            res.append(num)
        
        return res
            

        
