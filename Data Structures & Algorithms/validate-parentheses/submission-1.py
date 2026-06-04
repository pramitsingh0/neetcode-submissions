class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren_map = {")": "(", "}": "{", "]" : "["}

        for c in s:
            if c in paren_map:
                if stack and stack[-1] == paren_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False