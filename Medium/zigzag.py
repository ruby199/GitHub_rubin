class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:  # No need to convert if numRows is 1
            return s

        res = ""

        for r in range(numRows):
            increment = 2 * (numRows - 1)

            for i in range(r, len(s), increment):
                res += s[i]  # Adding the character each time
                if r > 0 and r < numRows - 1 and i + increment - 2 * r < len(s):
                    # In the middle row, adding the character from the alternate position
                    res += s[i + increment - 2 * r]

        return res
