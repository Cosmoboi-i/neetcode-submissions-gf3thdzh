class Solution:
    def trap(self, height: List[int]) -> int:

        if height == []:
            return 0


        res = 0
        i, j = 0, len(height) - 1
        lMax, rMax = 0, 0

        while i < j:
            a, b = height[i], height[j]

            lMax = max(lMax, a)
            rMax = max(rMax, b)

            res += min(lMax, rMax) - min(a, b)

            if lMax > rMax:
                j -= 1
            else:
                i += 1
        
        return res

            