class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # floyd algorithm

        # we can use two pointers: fast and slow pointers
        # if fast == slow --> we can identify if there's a cycle inside the linked list
        # we must use another pointer --> slow2
        # if slow == slow2 --> we can return hat value becuase it is the start of the cycle, as well as, the duplicate number
        # rules:
        # we can use this algorithm beacause:
        # 1. the lenght of the array is N +1
        # the range of the numbers is [1,n] --> array[0] is not included in the cycle

        # time complexity = O(2N) --> O(N)
        #   space complexity = O(1) -->

        slow = 0
        fast = 0

        while True:
            slow = nums[slow] 
            fast = nums[nums[fast]]
            if fast == slow:
                break

        slow2 = 0

        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                return slow # or nums[slow2] cause are the same 

    # TEST
    #  [1,2,3,2,2]
    # slow = nums[0] --> 1 --> slow is moving only by one step
    # fast = nums[nums[0]] --> nums[1] = 2 --> fast is moving by two steps
