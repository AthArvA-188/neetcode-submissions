class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i= 0
        last = {}
        max_length = 0
        
        for j, ch in enumerate(s, 1):
            if ch in last:
                i =  max(i, last[ch])
            max_length = max(max_length, j-i)

            last[ch] = j
                
        return max_length
