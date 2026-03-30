class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for s in strs:
            n = len(s)
            res += str(n) + '#' + s

        return res

        
        

    def decode(self, s: str) -> List[str]:
        
        rem = s
        res = []

        while rem:
            item = ""
            [n, rem] = rem.split('#', 1)
            n = int(n)
            for i in range(n):
                item += rem[i]
            res.append(item)

            rem = rem[n:]
        
        return res
        