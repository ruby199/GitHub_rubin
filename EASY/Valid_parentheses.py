class Solution:
    def isValid(s):
        # we are using stack data structure
        stack = []
        # we are mapping close&open using hash map (dic for all types of paretheses)
        closeToOpen = { 
            ")" : "(", "]" : "[", "}": "{"
        }
        # build our stack
        for c in s:
            if c in closeToOpen: # if this character is a closing paretheses to open map
            # make sure our stack is not empty, and value at the top of our stack is the matching opening paretheses
                if stack and stack[-1] == closeToOpen[c]:
                    # pop out the matching
                    stack.pop()
                else:
                    # if they don't match or stack is empty return FASLE - not matching
                    return False
            else:
                # add to our stack
                stack.append(c)

        return True if not stack else False # if not empty return True!

if (Solution.isValid("()[]{}")):
    print("Valid.")
else:
    print("Not Valid.")
