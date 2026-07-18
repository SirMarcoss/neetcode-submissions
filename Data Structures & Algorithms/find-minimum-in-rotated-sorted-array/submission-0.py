class Solution:
    def findMin(self, nums: List[int]) -> int:

        # rotated array --> array that is rotated N times.
        #brute force solution:
        # we can use a for loop 
        # Time complexity = O(N) which is not the optimal way to resolve this problem



        # mid point --> [3,4,5,6,1,2] --> 5
        # if array[left] <= 5 --> we have to search in this sub array
        # if array[right] >= 5 --> we don't have to search in this sub array
        # 2 sub-arrays--> [3,4,5,6] [1,2]
        # [3,4,5,6] this is the array where we must search the value
        # we can use the binary search on this sub-array
        # Time complexity = O(LogN)
        # Space complexcity = O(1) --> we are not using other data structure to operate inside this algorithm

        res = nums[0]

        inf = 0
        sup = len(nums) -1

        while inf <= sup:
            if nums[inf] < nums[sup]:
                res = min(res,nums[inf])
                break
            
            mid = (inf + sup) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[inf]:
                inf = mid +1
            else:
                sup = mid -1
        return res

        