class Solution:
    def isValid(self, s: str) -> bool:
        paren = {"}" : "{", "]" : "[", ")" : "("}
        stack = []

        for char in s:
            if char in paren:
                if stack and stack[-1] == paren[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return len(stack) == 0