class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        
        nums.sort()

        streak, maxStreak = 1, 1


        for i, x in enumerate(nums):
            if i == 0:
                continue
            if x == nums[i-1]:
                continue
            if x == nums[i-1] + 1:
                streak += 1
            else:
                maxStreak = max(streak, maxStreak)
                streak = 1

        
        maxStreak = max(streak, maxStreak)

        return maxStreak
