class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # binary search --> time complexity = O(logN)
        # we can use binary search because the array is sorted in ascending order.
        # the array could be rotated.
        # Space complexity = O(1)   = costant
        
        #brute force solution:
        # use a for loop:
        # time complexcity = O(N) 

        # [3,4,5,6,1,2], target = 1
        #  ^ --> inf
        #.           ^ --> sup
        # trivial case: nums[inf] < nums[sup] --> the array is not rotated or it is rotated N times where N is the number of values

        inf = 0
        sup = len(nums) - 1
        mid = (sup + inf) // 2

        while inf <= sup:
            if nums[mid] == target:
                return mid
            
            if nums[mid] >= nums[inf]:
                if nums[inf] <= target < nums[mid]:
                    sup = mid - 1
                else:
                    inf = mid + 1
                
            else:
                if nums[mid] < target <= nums[sup]:
                    inf = mid + 1
                else:
                    sup = mid - 1
            mid = (sup + inf) // 2
        return -1 
