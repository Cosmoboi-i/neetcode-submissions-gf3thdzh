class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        def helper(self, nums):
            prevPrev, prev = 0, 0

            for i in range(0, len(nums)):
                cur = max(prev, prevPrev + nums[i])
                prevPrev = prev
                prev = cur
            
            return prev
        
        return max(nums[0], helper(self, nums[1:n]), helper(self, nums[0:-1]))