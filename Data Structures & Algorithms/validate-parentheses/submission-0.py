class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dicpar = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in dicpar:
                if stack and stack[-1] == dicpar[c]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(c)

        return True if not stack else False
        