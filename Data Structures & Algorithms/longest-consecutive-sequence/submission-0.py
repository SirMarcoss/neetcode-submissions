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
        for number in hashset:
            if (number - 1) not in hashset:
                lenght = 1
                while (number + lenght) in hashset:
                    lenght +=1
                counter = max(lenght, counter)
        return counter
        






        
        