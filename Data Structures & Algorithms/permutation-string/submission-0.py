class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = {}
        s2Count = {}
        for r in range(len(s1)):
            s1Count[s1[r]] = 1 + s1Count.get(s1[r], 0)
            s2Count[s2[r]] = 1 + s2Count.get(s2[r], 0)
        
        if s1Count == s2Count:
            return True
        else:
            for r in range(len(s1), len(s2)):
                s2Count[s2[r]] = 1 + s2Count.get(s2[r], 0)
                lchar = s2[r - len(s1)]
                s2Count[lchar] -= 1
                if s2Count[lchar] == 0:
                    del s2Count[lchar]

                if s1Count == s2Count:
                    return True
            return False
                