class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        heash = set()

        for n in nums:
            if n in heash:
                return True
            heash.add(n)
        return False