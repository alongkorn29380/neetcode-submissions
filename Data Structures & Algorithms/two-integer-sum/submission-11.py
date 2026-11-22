class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}

        for i, n in enumerate(nums):
            curSum = target - n
            if curSum in prev:
                return [prev[curSum], i]
            prev[n] = i