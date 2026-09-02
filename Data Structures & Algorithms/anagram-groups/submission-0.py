class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for x in strs:
            sorts = ''.join(sorted(x))
            if sorts not in group:
                group[sorts] = []
            group[sorts].append(x)
        return list(group.values())
