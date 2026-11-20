class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prve = {}

        for i, n in enumerate(nums):
            cursum = target - n
            if cursum in prve:
                return [prve[cursum], i]
            prve[n] = i