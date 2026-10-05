class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Store values and symbols from biggest to smallest
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        
        ans = ""
        
        # Check each value starting from 1000
        for i in range(len(values)):
            # While the number is large enough, keep subtracting and adding the symbol
            while num >= values[i]:
                ans += symbols[i]
                num -= values[i]
                
        return ans
