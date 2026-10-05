class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Edge case: If 1 row or string is too short, pattern doesn't zigzag
        if numRows == 1 or numRows >= len(s):
            return s
        
        # 1. Create a list of empty strings for each row
        rows = [''] * numRows
        current_row = 0
        step = -1  # Starts by flipping to +1 on the very first character
        
        # 2. Place each character in its row and bounce
        for char in s:
            rows[current_row] += char
            
            # Reverse direction at the top or bottom row
            if current_row == 0 or current_row == numRows - 1:
                step = -step
                
            current_row += step
            
        # 3. Join all rows together
        return "".join(rows)
