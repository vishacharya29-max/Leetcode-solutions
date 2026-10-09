class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]
        n = len(nums)
        
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                # If exact match found, return immediately
                if current_sum == target:
                    return current_sum
                
                # Check if this sum is closer to the target
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                    
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return closest_sum
