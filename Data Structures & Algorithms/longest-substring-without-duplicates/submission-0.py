class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0,0
        stack = {}
        res = 0

        for r in range(len(s)):
            if s[r] in stack:
                l = max(stack[s[r]] + 1, l)
            stack[s[r]] = r
            res = max(res, r - l + 1)
        return res
