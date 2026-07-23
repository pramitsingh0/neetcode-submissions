class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        res = ""
        for p in path.split("/"):
            if p:
                if p == "..":
                    if stack:
                        stack.pop()
                elif p != ".":
                    stack.append(p)
        
        return "/" + "/".join(stack)