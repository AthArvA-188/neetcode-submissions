class Solution:
    def isValid(self, s: str) -> bool:
        
        stack =deque()
        pairs = {'}':'{', ')':'(', ']':'['}

        for ch in s:
            if ch in pairs.values():
                stack.append(ch)
            elif ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                return False
        return not stack
