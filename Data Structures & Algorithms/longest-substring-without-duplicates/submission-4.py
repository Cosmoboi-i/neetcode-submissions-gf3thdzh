class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        i, j = 0, 0

        length = 1
        seen = set()

        while j < len(s):
            while s[j] in seen:
                seen.remove(s[i])
                i += 1
            else:
                seen.add(s[j])
                length = max(length, j - i + 1)
                j += 1
        

        return length
                
            
