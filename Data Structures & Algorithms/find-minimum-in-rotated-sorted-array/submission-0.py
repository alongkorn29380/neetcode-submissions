class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            min = (l + r) // 2
            if nums[min] > nums[r]:
                l = min + 1
            else:
                r = min
        return nums[l]