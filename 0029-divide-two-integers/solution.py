class Solution:
    def divide(self, dividend, divisor):
        # 32-bit integer boundary limits
        MAX_INT = 2147483647      # 2**31 - 1
        MIN_INT = -2147483648     # -2**31
        
        # Handle overflow case
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
            
        # Determine the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with positive numbers
        dvd = abs(dividend)
        dvs = abs(divisor)
        
        quotient = 0
        
        # Exponential doubling using bitwise shifts
        while dvd >= dvs:
            temp_dvs = dvs
            multiple = 1
            
            # Double temp_dvs until it is larger than dvd
            while dvd >= (temp_dvs << 1):
                temp_dvs <<= 1
                multiple <<= 1
                
            dvd -= temp_dvs
            quotient += multiple
            
        if negative:
            quotient = -quotient
            
        return max(MIN_INT, min(MAX_INT, quotient))
