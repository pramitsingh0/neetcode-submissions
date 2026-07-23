class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        res = ""
        for p in path.split("/"):
            if p:
                stack.append(p)
                if p == ".":
                    stack.pop()
                elif p == "..":
                    i = 0
                    while stack and i < 2:
                        stack.pop()
                        i += 1
        
        return "/" + "/".join(stack)