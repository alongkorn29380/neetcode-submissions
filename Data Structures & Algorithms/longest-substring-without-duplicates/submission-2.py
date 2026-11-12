class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L, Res = 0, 0 
        stack = {}

        for R in range(len(s)): 
            if s[R] in stack: 
                L = max(L, stack[s[R]] + 1) 
            stack[s[R]] = R 
            Res = max(Res, R - L + 1) 
        return Res