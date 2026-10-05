class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # 1. Width between lines
            width = right - left
            
            # 2. Water height is bounded by the shorter wall
            h = min(height[left], height[right])
            
            # 3. Calculate current area
            current_water = width * h
            if current_water > max_water:
                max_water = current_water
                
            # 4. Move the smaller bar inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water
