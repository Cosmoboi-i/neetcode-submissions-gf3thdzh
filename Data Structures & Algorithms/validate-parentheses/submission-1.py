class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openingBraks = ['(', '{', '[']
        brakMatch = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for x in s:
            if x in openingBraks:
                stack.append(x)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if brakMatch[x] != last:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False