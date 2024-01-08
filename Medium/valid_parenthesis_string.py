"""
Problem Link: https://leetcode.com/problems/valid-parenthesis-string/description/

Trail_1: (wrong) 
- The logic doesn’t adequately handle the flexibility of '*' being able to represent different characters under different conditions.
- If you consider a string like ())*, a forward pass alone would consider this string valid (treating '' as '('). But, in reality, the string is invalid because there is an unmatched ')' before any '' appears. The backward pass correctly identifies this 

Trail_2: (correct, most efficient) Two-pass approach
String: (*)
    Forward Pass: Treating '*' as '(', the string becomes ((), which is valid as every ')' has a matching '('.
    Backward Pass: Treating '*' as ')', the string becomes ()), which is also valid as every '(' has a matching ')'.

- It’s more efficient because it accurately handles the ambiguity of '*', ensuring the string is valid in all possible interpretations.

Trail_3: (correct) "min-max" approach
- The algorithm maintains two counters: leftMin and leftMax.
    - leftMin represents the minimum number of open left parentheses, assuming some '*' characters are used as either empty strings or right parentheses.
    - leftMax represents the maximum number of open left parentheses, assuming all '*' characters are used as left parentheses.
- The range [leftMin, leftMax] defines the possible number of open left parentheses at any point in the string.
issue.

"""


from collections import deque


class Solution:
    def checkValidString_trial_1(self, s: str) -> bool:
        # This solution cannot pass the test case: s = "(((((()*)(*)*))())())(()())())))((**)))))(()())()"

        # Convert string into list
        s_list = []
        s_list[:0] = s
        stack = deque(s_list)

        num_close = 0
        num_star = 0

        # Track ")" and "*"
        for i in range(len(s_list)):
            cur = stack.pop()
            if cur == ')':
                num_close += 1
            elif cur == '*':
                num_star += 1
            else:
                if num_close:
                    num_close -= 1
                elif num_star:
                    num_star -= 1
                else:
                    return False
        if "(" in stack:
            return False
        return True

    # Runtime: Beats 97.83%of users with Python3
    # Memory: Beats 36.49%of users with Python3
    def checkValidString_trial_2(self, s: str) -> bool:
        # Forward pass
        open_brackets = 0
        for char in s:
            if char in "(*":
                open_brackets += 1
            else:  # char is ')'
                open_brackets -= 1
                if open_brackets < 0:
                    return False

        # If open brackets are balanced, they might be correctly closed
        if open_brackets == 0:
            return True

        # Backward pass
        open_brackets = 0 # Reset the counter for open brackets
        for char in reversed(s):
            if char in "*)":
                open_brackets += 1
            else:  # char is '('
                open_brackets -= 1
                if open_brackets < 0:
                    return False

        return True

    # Runtime: Beats 30.85%of users with Python3
    # Memory: Beats 28.80%of users with Python3
    def checkValidString_trial_3(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0: # s = ( * ) (
                leftMin = 0 
        
        return leftMin == 0

# Test loop
def test_checkValidString():
    solution = Solution()

    # Test cases
    test_cases = [
        ("()", True),
        ("(*)", True),
        ("(*))", True),
        # Add more test cases here
    ]

    for s, expected in test_cases:
        result = solution.checkValidString_trial_2(s)
        assert result == expected, f"Failed on {s}: expected {expected}, got {result}"

# Run the test
test_checkValidString()
