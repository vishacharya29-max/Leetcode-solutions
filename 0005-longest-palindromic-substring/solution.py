class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        
        # Helper function to expand around center
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]
        
        # Check every possible center
        for i in range(len(s)):
            # Odd length center (e.g., "aba")
            odd = expand(i, i)
            if len(odd) > len(res):
                res = odd
                
            # Even length center (e.g., "abba")
            even = expand(i, i + 1)
            if len(even) > len(res):
                res = even
                
        return res
