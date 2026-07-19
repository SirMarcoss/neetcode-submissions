class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # Binary Search --> TIme complexity = O(NLogN) --> with sorting 
        # Space complexity = O(1) --> costant 
        # Binary Search on answer: [False, False, False, True, True, True, ...]
        # [1,4,3,2], h = 9 --> h = number of hours to eat all the bananas
        # we have to return a K value, which is the BANANAS-PER-HOUR eating rate
        # [1,4,3,2], h = 9  1st pile: 1 h
        # 2nd pile: 2 hours
        # 3rd pile: 2 hours
        # 4th pile: 1h
        # 6h < 9 --> return 2

        
        inf = 1
        sup = max(piles)

        while inf <= sup:
            mid = (inf + sup) // 2
            hours = 0

            for banana in piles:
                hours += math.ceil(banana / mid)


            if hours <= h:
                sup = mid -1
            else:
                inf = mid + 1

        return inf


# TEST 
# [1,4,3,2] --> mid = 4
# 1 // 4 = 0 --> hours = 1
# 4 // 4 = 1 --> hours = 2
# 3 // 4 = 0 --> hourse = 3
# 2 // 4 = 0 --> hourse = 4
# 4 > 9 ? --> target = 4















        