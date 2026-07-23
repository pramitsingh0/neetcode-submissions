class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = ["/"]
        res = ""
        for p in path.split("/"):
            if p:
                stack.append(p)
                if p == ".":
                    stack.pop()
                elif p == "..":
                    if stack:
                        stack.pop()
                        stack.pop()
                        if not stack:
                            stack.append("/")
        
        for ele in stack:
            if (ele == "/") or (res and res[-1] == "/"): res += ele
            else: res += "/" + ele
        
        return res