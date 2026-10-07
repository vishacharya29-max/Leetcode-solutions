class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # Sort the strings lexicographically
        strs.sort()
        
        first = strs[0]
        last = strs[-1]
        common = []
        
        # Compare characters between the first and last strings
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            common.append(first[i])
            
        return "".join(common)
