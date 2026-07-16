class Solution:
    def isValid(self, s: str) -> bool:

        # STACK --> data structure LIFO (last in first out)

        #[(] --> ) --> extract (
        #[ (,[ ] ) --> [ == ) --> False
        # Time complexity = O(N) 
        # Space coplexity = O(N)

        stack = []


        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)

            elif char == ')':
                if stack and stack[-1] == '(': # --> which is the last value inside of the stack? --> stack[-1]
                    stack.pop() # --> extract the first value of the stack 
                else:
                    return False
            
            elif char == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
            
            elif char == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False


# test
# s = "([{}])"
# '(' --> stack.append(char) --> ['(']
# '[' --> stack append(char) --> ['(', '[']
# '{' --> stack.append(char) --> ['(', '[', '{']
# '}' --> stack[-1] = '{' --> stack.pop() --> ['(', '['] --> '{' it has been extracted
            
