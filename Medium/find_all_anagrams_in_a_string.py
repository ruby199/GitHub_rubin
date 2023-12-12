class Solution:
    def findAnagrams(self, s, p):
        # Edge case: If p is longer than s, no anagrams are possible
        if len(p) > len(s): return []

        # Initialize dictionaries to count character frequencies in p and s
        pCount, sCount = {}, {}

        # Count frequencies of characters in p and the first window of s
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)

        # Check if the first window is an anagram of p
        res = [0] if sCount == pCount else []

        # Initialize the left pointer of the window
        l = 0

        # Slide the window through s
        for i in range(len(p), len(s)):
            # Add the new character to the window
            sCount[s[i]] = 1 + sCount.get(s[i], 0)

            # Remove the old character from the window
            sCount[s[l]] -= 1

            # Remove the character count from the dictionary if it becomes zero
            if sCount[s[l]] == 0:
                sCount.pop(s[l])

            # Move the left pointer to the right
            l += 1

            # Check if the current window is an anagram of p
            if sCount == pCount:
                res.append(l)

        # Return the list of starting indices of anagrams of p in s
        return res

def test_findAnagrams():
    solution = Solution()

    # Test case 1
    s1, p1 = "cbaebabacd", "abc"
    expected1 = [0, 6]
    assert solution.findAnagrams(s1, p1) == expected1, f"Test 1 failed: expected {expected1}, got {solution.findAnagrams(s1, p1)}"

    # Test case 2
    s2, p2 = "abab", "ab"
    expected2 = [0, 1, 2]
    assert solution.findAnagrams(s2, p2) == expected2, f"Test 2 failed: expected {expected2}, got {solution.findAnagrams(s2, p2)}"

    # Add more test cases as needed
    # ...

    print("All tests passed!")

# Call the test function
test_findAnagrams()