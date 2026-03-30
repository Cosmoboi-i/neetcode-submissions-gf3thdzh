class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        ans = -1

        while l <= r:
            m = (r + l) // 2
            print('ss', l, r, m)
            hours = 0
            for x in piles:
                hours += -(-x // m)
            
            if hours > h:
                l = m + 1
            else:
                ans = m
                r = m - 1
        
        return ans


