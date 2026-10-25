class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

     map = {}

    
     for i in range(len(nums)):
       ans = target - nums[i]

       if ans in map:
        return [map[ans],i]
       
       map[nums[i]] = i

     return []

        