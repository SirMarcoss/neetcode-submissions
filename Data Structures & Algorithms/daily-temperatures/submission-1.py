class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # [] --> stack
        # [30] --> [38, 30,]
        #Time complexity = O(N) ammortized 
        # Space complecity = O(N) --> we're using a stack

        stack = []
        res = [0] * len(temperatures)

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stackInd, stackTemp = stack.pop()
                res[stackInd] = index - stackInd
            
            stack.append((index, temp))
        return res