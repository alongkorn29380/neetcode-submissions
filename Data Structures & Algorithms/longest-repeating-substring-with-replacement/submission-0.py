class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        maxFreq = 0
        const = {}

        for r in range(len(s)):
            const[s[r]] = 1 + const.get(s[r], 0)
            maxFreq = max(maxFreq, const[s[r]])
            while (r - l + 1) - maxFreq > k:
                const[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res