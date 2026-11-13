class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prve = {}

        for i, n in enumerate(nums):
            curSum = target - n
            if curSum in prve:
                return [prve[curSum], i]
            prve[n] = i