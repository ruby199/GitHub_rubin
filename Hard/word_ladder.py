"""
Problem Link: https://leetcode.com/problems/word-ladder/description/?envType=study-plan-v2&envId=top-interview-150

Topics: Hash Table, String, Breadth-First Search

"""

from collections import deque


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
    
        # BFS initialization (using queue)
        q = deque() # will store tuples of (current word, # of steps taken to reach that word)
        q.append((beginWord, 1))

        # Prepare wordList
        wordSet = set(wordList) # for O(1) complexity check

        # BFS
        while q:
            word, steps = q.popleft()
            # generate all possible wors that are one letter different from the current word
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordSet:
                        if next_word == endWord:
                            return steps + 1
                        q.append((next_word, steps + 1))
                        wordSet.remove(next_word)
        
        return 0 # No path found

                




beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

sol = Solution()
print(sol.ladderLength(beginWord, endWord, wordList))