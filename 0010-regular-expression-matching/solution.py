class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo = {}

        def dfs(i, j):
            # If already calculated, reuse answer
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base case: pattern is finished
            if j == len(p):
                return i == len(s)
            
            # Check if current letters match
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            # Case 1: Next character is '*'
            if j + 1 < len(p) and p[j + 1] == '*':
                # Option A: skip 'char*' (use 0 times)
                # Option B: use '*' if current letters match
                ans = dfs(i, j + 2) or (match and dfs(i + 1, j))
            else:
                # Case 2: Normal step forward
                ans = match and dfs(i + 1, j + 1)
                
            memo[(i, j)] = ans
            return ans

        return dfs(0, 0)
