class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = cut = 0

        for num in nums:
            cut = cut + 1 if num else 0
            res = max(cut, res)
        return res