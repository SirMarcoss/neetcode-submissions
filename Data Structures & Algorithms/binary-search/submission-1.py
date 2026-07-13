class Solution:
    def search(self, nums: List[int], target: int) -> int:
        inf = 0
        sup = len(nums) -1
        mid  = (sup + inf) // 2

        while inf <= sup:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                sup = mid -1
            else:
                inf = mid + 1
            mid = (sup + inf) // 2
        return -1
        