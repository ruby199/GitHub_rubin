class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = "" # current filepath or directory we are at

        for c in path + "/":
            if c == "/":
                if cur == "..":
                    if stack: # if the stack is non-empty
                        stack.pop()
                elif cur != "" and cur != ".":
                    stack.append(cur) # take the current file and update our stack
                cur = "" # reset our current

            else:
                cur += c

        return "/" + "/".join(stack)
