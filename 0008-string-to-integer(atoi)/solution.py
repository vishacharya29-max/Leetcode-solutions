class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 1. Remove leading whitespace
        s = s.lstrip()
        if not s:
            return 0
        
        # 2. Check sign
        sign = 1
        i = 0
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1
            
        # 3. Read digits
        res = 0
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
            
        # Apply sign
        res = res * sign
        
        # 4. Clamp within 32-bit integer boundaries [-2^31, 2^31 - 1]
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if res < INT_MIN:
            return INT_MIN
        if res > INT_MAX:
            return INT_MAX
            
        return res
