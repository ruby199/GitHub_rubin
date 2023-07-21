class Solution:
    def decodeString(self, s: str) -> str:
        # stack = []
        # curr_num = 0
        # curr_str = ""

        # for char in s:
        #     if char.isdigit():
        #         curr_num = curr_num * 10 + int(char)
        #     elif char == '[':
        #         stack.append(curr_num)
        #         stack.append(curr_str)
        #         curr_num = 0
        #         curr_str = ""
        #     elif char == ']':
        #         prev_str = stack.pop()
        #         repeat_num = stack.pop()
        #         curr_str = prev_str + repeat_num * curr_str
        #     else:
        #         curr_str += char

        # return curr_str

        # slightly more memory-efficient version
        stack= []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                stack.append(int(k) * substr)

        return "".join(stack)
                

