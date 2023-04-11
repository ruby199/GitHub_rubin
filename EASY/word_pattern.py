class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        # check if it's valid
        if len(pattern) != len(words):
            return False
        
        charToWord = {} # hash map
        wordToChar = {} # hash map

        for c, w in zip(pattern, words):
            if c in charToWord and charToWord[c] != w:
                return False

            if w in wordToChar and wordToChar[w] != c:
                return False
        
            charToWord[c] = w
            wordToChar[w] = c
            
        return True
