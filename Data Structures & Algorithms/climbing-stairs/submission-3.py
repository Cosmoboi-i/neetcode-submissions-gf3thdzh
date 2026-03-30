class Solution:
    def climbStairs(self, n: int) -> int:

        if n <= 2:
            return n

        prevPrev, prev = 1, 2

        for i in range(3, n + 1):
            cur = prev + prevPrev
            prevPrev = prev
            prev = cur
        
        return cur
        
        