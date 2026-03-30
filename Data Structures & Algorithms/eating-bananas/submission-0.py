class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        res = -1

        while l <= r:
            m = l + (r - l) // 2
            sum = 0
            for x in piles:
                sum += x // m
                if x % m:
                    sum += 1
            if sum <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res

        