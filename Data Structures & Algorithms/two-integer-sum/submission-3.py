class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}

        for i, a in enumerate(nums):
            diff = target - a
            if diff in table:
                return [table[diff], i]
            table[a] = i
        
        return [0, 0]