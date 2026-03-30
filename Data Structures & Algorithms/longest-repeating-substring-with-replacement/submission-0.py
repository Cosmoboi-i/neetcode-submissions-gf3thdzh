class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}

        i, j, res, maxF = 0, 0, 0, 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxF = max(maxF, count[s[r]])

            while(r - i + 1) - maxF > k:
                count[s[i]] = count[s[i]] - 1
                i += 1
            
            res = max(res, r - i + 1)

        
        return res