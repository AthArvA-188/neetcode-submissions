class Solution:
    def isHappy(self, n: int) -> bool:
    #     visit = set()

    #     while n not in visit:
    #         visit.add(n)
    #         n = self.ssq(n)
    #         if n==1:
    #             return True
    #     return False
    
    # def ssq(self, n):
    #     op = 0
    #     while n:
    #         digit = n%10
    #         digit = digit**2
    #         op+=digit
    #         n=n//10
    #     return op

        slow, fast = n , self.ssq(n)

        while slow != fast:
            fast = self.ssq(self.ssq(fast))
            slow = self.ssq(slow)
        return True if fast==1 else False
    
    def ssq(self, n):
        output =0
        while n:
            digit = n%10
            digit = digit**2
            output +=digit
            n=n//10
        return output
