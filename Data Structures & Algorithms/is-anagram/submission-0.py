class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return len(set(s)) > len(t)