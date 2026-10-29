class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
     
        i=0
        
        for j  in range (1,len(nums)):
         
         if nums[i] != nums[j]:
          i += 1
          nums[i] = nums[j]
   

         else:
            j+=1

        return i+1    
