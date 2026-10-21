class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        for i in s:
            if i in closeToOpen:
                if stack and stack[-1] == closeToOpen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if len(stack) > 0:
            return False 
        else:
            return True
        