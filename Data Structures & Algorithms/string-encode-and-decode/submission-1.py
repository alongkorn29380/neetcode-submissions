class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += str(len(i)) + "#" + i
        return res
        

    def decode(self, s: str) -> List[str]:
        res = []
        x = 0
        while x < len(s):
            j = s.find('#', x)
            length = int(s[x:j])
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            x = j + 1 + length
        return res