class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0

        i, j = 0, 0

        length = 1
        seen = set()

        while j < len(s):
            if s[j] in seen:
                length = max(length, j - i)
                i += 1
                j = i
                seen = set([s[i]])
            else:
                seen.add(s[j])
                length = max(length, j - i + 1)
            j += 1
        

        return length
                
            
