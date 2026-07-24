class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for p in path.split("/"):
            if p:
                if p == ".":
                    continue
                elif p == "..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(p)
            
        return "/" + "/".join(stack)