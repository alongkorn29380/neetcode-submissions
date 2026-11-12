class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in stack:
                l = max(l, stack[s[r]] + 1)
            stack[s[r]] = r
            res = max(res, r - l + 1)
        return res