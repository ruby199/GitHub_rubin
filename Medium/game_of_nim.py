"""
Problem Link: https://leetcode.com/problems/game-of-nim/description/

Topics: Array, math, dynamic programming, bit manipulation, brainteaser, game theory

[Approach]: Sumulation - Dynamic Programming

Conditions:
    - a player wins if at least one move exists where the opponent loses.
    - a player loses if the opponent wins in all the moves available
    - a player loses when they have no moves available. 


[DEF] Minimax: n game theory, minimax is a decision rule used to minimize the worst-case potential loss; in other words, a player considers all of the best opponent responses to his strategies, and selects the strategy such that the opponent's best strategy gives a payoff as large as possible.

"""

# def isWinner(state):
#     # termination condition, when all the piles are zero.
#     # the current player loses the game
#     if all([ v == 0 for v in piles]):
#         return False
    
#     for nextState in allNextStates:
#         # nextState is for the next player's turn
#         # if the next player loses, the current player wins
#         if not isWinner(nextState):
#             return True
    
#     # the next player wins in all states after a move
#     # so the current player loses the game
#     return False



class Solution:
    def nimGame(self, piles):
        # Hash map for memoization
        memo = {}

        def is_next_person_winner(piles, remaining): # The function iterates through each pile and each possible move.

            # make a key by concatenating the count of stones
            key = tuple(piles)
            # print(key)

            if key in memo:
                return memo[key]
            
            if remaining == 0: # Base case: if no stones are remaining, the current player loses
                return False
            
            # If the current player has no more moves -> check if the opponent loses the game in any of them
            for i in range(len(piles)):
                if piles[i] > 0:
                    for j in range(1, piles[i] + 1):
                        # Take j stones from the i-th place
                        next_piles = piles[:] # creating a shallow copy of piles
                        next_piles[i] -= j

                        # If the next player cannot win, the current player wins
                        if not is_next_person_winner(next_piles, remaining - j):
                            memo[key] = True
                            return True
                    
            memo[key] = False
            return False

        return is_next_person_winner(piles, sum(piles))


sol = Solution()
piles = [1,2,3]
print(sol.nimGame(piles))