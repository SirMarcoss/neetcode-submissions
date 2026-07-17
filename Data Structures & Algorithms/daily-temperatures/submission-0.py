class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # [] --> stack
        # [30] --> [38, 30,]
        #Time complexity = O(N) ammortized 
        # Space complecity = O(N) --> we're using a stack



        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]: # --> Time complexity = O(N) ammortized *
                stackIndex = stack.pop()
                res[stackIndex] = (i - stackIndex)
            stack.append(i)
        return res 


# * the while loop is not itering through the N values inside the inputer array

# TEST
# [30,38,30,36,35,40,28]
# 30 --> stack: [[30, 0]] res: []
# 38 --> 38 > 30 stack: [[38, 1]] res: []