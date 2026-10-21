class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pset = {')': '(', '}': '{', ']': '['}

        for b in s:
            if b in pset:
                if stack and stack[-1] == pset[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        if stack:
            return False
        else:
            return True

        