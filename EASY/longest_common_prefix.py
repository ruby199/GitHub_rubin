class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        

        min_length = min(len(string) for string in strs)

        common_prefix = ""

        for i in range(min_length):
            current_char = strs[0][i]
            if all(string[i] == current_char for string in strs):
                common_prefix += current_char
            else:
                break
        return common_prefix