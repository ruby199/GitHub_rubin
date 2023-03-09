# bottom-up dynamic programming

class Solution:
    def climbStairs(n):
        one, two = 1, 1

        for i in range(n - 1):

            temp = one
            one = one + two # adding the two previous values and get a new result
            two = temp

        return one

description = "You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?"
print(description)
userPrompt = input("Enter n: ")
print(Solution.climbStairs(int(userPrompt)))

