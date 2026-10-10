class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        res = []
        
        def backtrack(index, path):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            
            letters = phone_map[digits[index]]
            for letter in letters:
                path.append(letter)
                backtrack(index + 1, path)
                path.pop()  # Backtrack step
                
        backtrack(0, [])
        return res
