class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    
        # stack --> data stracture that use the method LIFO (Last in First out)
        #["1","2","+","3","*","4","-"]
        # [1,2] --> 1 + 2 = 3 --> [3]
        # [3,3] --> 3 * 3 = 9 --> [9]
        #[9, 4] --> 9 - 4 = 5 --> return 5
        # when we have an empty stack, we can return the result
        
        # Time complexity = O(N) --> we use a simple iteration through the input array
        # Space complxity = O(N) -- > we are using a Stack as a data structure

        stack = []

        if len(tokens) == 0:
            return 0
        
        for value in tokens:
            if value == '+':
                stack.append(stack.pop() + stack.pop())

            elif value == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            
            elif value == '*':
                stack.append(stack.pop() * stack.pop())
            
            elif value == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            else:
                stack.append(int(value))
        return stack[-1]





# ["2","1","+","3","*"]
# 2 --> [2]
# 1 --> [2,1]
# + --> 2 + 1 = 3 --> [3]
# 3 --> [3,3]
# * --> 3 * 3 = 9 --> [9]
# return stack[-1] --> 9

