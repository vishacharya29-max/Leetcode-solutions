class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = set()       # Set to hold characters in the current window
        left = 0           # Left border of the window
        max_len = 0        # Result to store maximum length
        
        for right in range(len(s)):
            # If current character is already in the window, shrink from left
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                
            # Add current character to window
            seen.add(s[right])
            
            # Calculate window size: (right - left + 1)
            current_window = right - left + 1
            if current_window > max_len:
                max_len = current_window
                
        return max_len
