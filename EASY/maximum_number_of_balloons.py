# |Good parts:
# |- The code defines a class and a method within it, which makes it easy to reuse and maintain.
# |- The method takes a string as input and returns an integer, which is a clear indication of what the method does and what it expects as input and output.
# |- The code uses a list to store the letters of the word "balloon", which makes it easy to check if all the letters are present in the input string.
# |- The code uses a loop to iterate over each character in the input string, which is an efficient way to process the string.
# |
# |Bad parts:
# |- The code modifies the "balloon" list inside the loop, which can lead to unexpected behavior and errors. Instead, the code should create a copy of the list and modify the copy.
# |- The code assumes that the input string contains only lowercase letters, which may not always be the case. It would be better to convert the input string to lowercase before processing it.
# |- The code does not handle the case where the input string does not contain the word "balloon". In this case, the method should return 0.
# |

class Solution1:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = ['b', 'a', 'l', 'l', 'o', 'o', 'n']
        n = 0
        for char in text:
            if char in balloon:
                balloon.remove(char)
            if not balloon:
                n += 1
                balloon = ['b', 'a', 'l', 'l', 'o', 'o', 'n']
        return n


# |- The code uses the Counter class from the collections module to count the occurrences of each character in the input string.
# |- It uses a hash map to store the count of each character in the input string and the count of each character in the word "balloon".
# |- The code uses the min() function to update the minimum value of the result variable, which is initialized to infinity.
# |- The code returns the final result.

from collections import Counter


class Solution2:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)  # hash map counting each character
        balloon = Counter("balloon")

        res = float("inf") # set up a inf value
        # Or:
        # res = len(text)

        for c in balloon:
            res = min(res, countText[c] // balloon[c]) # use min() to update the minimum value

        return res
