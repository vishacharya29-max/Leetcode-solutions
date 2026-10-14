class Solution:
    def isValid(self, s):
        # Map each closing bracket to its corresponding opening bracket
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        
        for char in s:
            if char in bracket_map:
                # Pop the top element if stack is non-empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # Check if the opening bracket matches
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push onto stack
                stack.append(char)
                
        # Valid only if all opened brackets were closed
        return not stack
