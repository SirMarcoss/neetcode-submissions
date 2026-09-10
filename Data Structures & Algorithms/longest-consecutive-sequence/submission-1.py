class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #brute force solution: we can sort the array --> analyse if every number is incremening only by 1
        #time complexity: O(NlogN)
        # WE CANNOT SORT THE ARRAY

        # dictionary: key--> number, value --> frquency of the number
        # we can use a for loop by key and values:
        #the minimum key of the hashtable 

        hashset = set(nums)
        counter = 0

        for num in nums:
            if (num - 1) not in hashset:
                lenght = 1
                while (num + lenght) in hashset:
                    lenght += 1
                
                counter = max(counter, lenght)
        return counter


# test
# does 2 - 1 exist? no --> lenght = 1
# 2+1 in hashset? yes --> lenght = 2
# 3 +1 in hashset? yes --> lenght = 3
# 4 + 1 = 5 in hashset? yes --> lenght = 4
# 5 + 1 = 6 in hashset? no --> counter = lenght 

# max because we have to pick only the longest path.
#does 20-1 exist? no --> lenght = 1
#20 +1 no --> if we use counter = lenght we have only one--> that is not true. For this reason we have to use the max function





        
        