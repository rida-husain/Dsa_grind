class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        seen = set()

        i = 0
        for i in range(i, len(nums)):
            if nums[i] in seen:
                return True

            seen.add(nums[i])

        return False
