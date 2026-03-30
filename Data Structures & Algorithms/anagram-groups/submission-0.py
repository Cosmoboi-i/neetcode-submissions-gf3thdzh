class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashTable = {}

        for str in strs:
            charList = [0] * 26
            for i in str:
                charList[ord(i) - ord('a')] += 1
            
            key = tuple(charList)
            if key in hashTable:
                hashTable[key].append(str)
            else:
                hashTable[key] = [str]
        
        return hashTable.values()
