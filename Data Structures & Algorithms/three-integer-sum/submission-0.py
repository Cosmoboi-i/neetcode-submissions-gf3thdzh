class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        res = set()
        
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1

            while j < k:
                sum = nums[j] + nums[k]

                if sum > -nums[i]:
                    k -= 1
                if sum < -nums[i]:
                    j += 1
                if sum == -nums[i]:
                   triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                   res.add(triplet)
                   j += 1
                   k -= 1

        resList = [list(t) for t in res]
        return resList