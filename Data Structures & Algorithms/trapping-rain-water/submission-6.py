class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1

        minHeight = 0
        water = 0

        while i <= j:
            a = height[i]
            b = height[j]

            water_a = max(minHeight - a, 0)
            water_b = max(minHeight - b, 0)
            water = water + water_a + water_b

            minHeight = max(min(a, b), minHeight)

            if a > b:
                j = j - 1
            else:
                i = i + 1
        
        return water

