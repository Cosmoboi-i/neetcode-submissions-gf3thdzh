class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqTable = {}

        for x in nums:
            freqTable[x] = freqTable.get(x, 0) + 1
        
        sortedTable = dict(sorted(freqTable.items(), key= lambda item : item[1], reverse=True))

        ans = list(sortedTable.keys())

        return ans[:k]