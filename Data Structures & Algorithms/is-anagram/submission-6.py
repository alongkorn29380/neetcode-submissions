class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return len(set(t)) != len(s)