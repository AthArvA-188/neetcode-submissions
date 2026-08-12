class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        n =len(s)

        i, j = 0, n-1
        while i<j:
            while i<j and not s[i].isalnum():
                i+=1
            while i<j and not s[j].isalnum():
                j-=1
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True



        # while i<j:
        #     if s[i]==s[j]:
        #         i+=1
        #         j-=1
        #     elif s[i] == " ":
        #         i+=1
        #     elif s[j] == ' ':
        #         j-=1
        #     else:
        #         return False
        # return True
        