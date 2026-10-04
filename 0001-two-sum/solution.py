class Solution(object):
    def twoSum(self,nums, target):
         seen = {}  # number → index
    
         for i in range(len(nums)):
             complement = target - nums[i]
        
             if complement in seen:
                  return [seen[complement], i]
        
             seen[nums[i]] = i
        
