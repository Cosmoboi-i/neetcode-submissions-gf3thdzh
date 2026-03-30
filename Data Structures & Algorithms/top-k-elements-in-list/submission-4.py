
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freqTable = [[] for _ in nums]

        for x in nums:
            count[x] += 1
        
        for key in count:
            freqTable[count[key] - 1].append(key)
        
        print('ft', freqTable)
        arr = []
        counter = 0
        for x in reversed(freqTable):
            if counter == k:
                break
            if len(x) != 0:
                for y in x:
                    arr.append(y)
                    counter += 1
            

        return arr


        