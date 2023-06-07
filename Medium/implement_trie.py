class TrieNode:
    def __init__(self):
        self.children = {} # children["a"] = TrieNode()
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()  # Instantiate TrieNode
            cur = cur.children[c] # Last character of the word
        
        # Mark end of word
        cur.endOfWord = True # if it is not a word - our function will return false

    def search(self, word: str) -> bool:
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root

        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True