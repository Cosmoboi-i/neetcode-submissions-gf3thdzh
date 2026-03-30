class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i = i + 1
                continue
            if not s[j].isalnum():
                j = j - 1
                continue

            if s[i] != s[j]:
                return False
            
            i = i + 1
            j = j - 1
        
        return True
