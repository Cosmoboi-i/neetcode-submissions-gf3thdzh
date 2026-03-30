class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        maxWater = 0

        while i < j:
            a, b = heights[i], heights[j]
            print(i, j, a, b)
            water = min([a, b]) * (j - i)
            maxWater = max([maxWater, water])
            if a > b:
                j -= 1
            else:
                i += 1
        
        return maxWater

            

            
            