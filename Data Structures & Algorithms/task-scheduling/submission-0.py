class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashtable = {}

        for task in tasks:
            if task not in hashtable:
                hashtable[task] = 1
            else:
                hashtable[task] += 1
        
        maxHeap = [-cnt for cnt in hashtable.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # [- cnt, idleTime]

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        
        return time


