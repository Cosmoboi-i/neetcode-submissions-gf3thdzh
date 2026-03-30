class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = {}
        n = len(nums)
        if n == 1:
            return nums[0]

        prevPrev = nums[0]
        prev = max(nums[1], nums[0])
        cur = prev

        for i in range(2, n):
            cur = max(prev, prevPrev + nums[i])
            prevPrev = prev
            prev = cur
        
        return cur