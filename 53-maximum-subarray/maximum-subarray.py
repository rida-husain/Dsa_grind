class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        i=0
        max_sum = nums[i]
        current_sum = 0

        for i in range(i, len(nums)):
            current_sum += nums[i]

            if max_sum < current_sum:
               max_sum = current_sum

            if current_sum < 0:
                current_sum = 0

        return max_sum

        

                
