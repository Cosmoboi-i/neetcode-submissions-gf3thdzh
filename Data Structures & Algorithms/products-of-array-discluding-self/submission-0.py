class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = 1
        zeroFlag = False

        for x in nums:
            if x == 0 and zeroFlag == False:
                zeroFlag = True
                continue
            n *= x
        
        arr = []

        if zeroFlag:
            for x in nums:
                if x == 0:
                    arr.append(n)
                else:
                    arr.append(0)
        else:
            for x in nums:
                arr.append(int(n / x))

        return arr