class Solution:
    def trap(self, height: List[int]) -> int:

        i, j = 0, len(height) - 1

        minH = 0
        sum = 0

        while i < j:
            a = height[i]
            b = height[j]
            minH = max(minH, min(a, b))
            sum += max(0, minH - a)
            sum += max(0, minH - b)

            if a < b:
                i += 1
            else:
                j -= 1
        
        return sum



            