class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []

        def backtrack(stack, openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append('(')
                backtrack(stack, openN + 1, closeN) # 3 fasi
                stack.pop()
            
            if closeN < openN:
                stack.append(')')
                backtrack(stack, openN, closeN + 1)
                stack.pop()
        

        backtrack(stack, 0, 0)
        return res


# TEST
# 1 si ferma al primo backtrack --> (
# 2 si ferma al primo backtrack --> ((
# 3 si ferma al primo backtrack --> (((
# 4 open == n si passa al second if. si ferma al secondo backtrack ((()
# 5 si ferma al secondo backtrack ((())
# 6 si ferma al secondo backtrack ((()))
# 7 ritorna 
#torna al 6 e fa pop ((())
#torna al 5 e fa pop ((()
#torna al 4 e fa pop (((
#torna al 3 e fa pop (( però adesso la funzione NON FINISCE --> c'è il secondo if quindi si continua da aggiungengo una prima chiusa (()

