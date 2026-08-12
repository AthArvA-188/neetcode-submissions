class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack =[]
        res = []
        def backtrack(sopen, sclose):
            if sopen ==sclose ==n:
                res.append(''.join(stack))
                return
            if sopen<n:
                stack.append('(')
                backtrack(sopen+1, sclose)
                stack.pop()
            if sclose<sopen:
                stack.append(")")
                backtrack(sopen, sclose+1)
                stack.pop()
        backtrack(0,0)
        return res