class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftnum = 0

        for i in range(len(nums)):
            rightnum = total - nums[i] - leftnum
            if leftnum == rightnum:
                return i
            leftnum += nums[i]
        return -1