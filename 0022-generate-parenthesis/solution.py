class Solution:
    def generateParenthesis(self, n):
        res = []
        
        def backtrack(open_count, close_count, current):
            # Base case: valid combination of 2 * n characters formed
            if len(current) == 2 * n:
                res.append("".join(current))
                return
            
            # Can add an open parenthesis if we haven't placed n of them
            if open_count < n:
                current.append('(')
                backtrack(open_count + 1, close_count, current)
                current.pop()  # Backtrack step
                
            # Can add a close parenthesis only if it doesn't exceed open parentheses
            if close_count < open_count:
                current.append(')')
                backtrack(open_count, close_count + 1, current)
                current.pop()  # Backtrack step
                
        backtrack(0, 0, [])
        return res
