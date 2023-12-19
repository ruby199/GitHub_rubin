class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Return False immediately if s1 is longer than s2
        if len(s1) > len(s2):
            return False
        
        # Initialize two arrays to keep count of characters in s1 and the first part of s2
        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            # Count characters in s1 and the first part of s2
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        # Initialize a variable to track the number of matches between s1Count and s2Count
        matches = 0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            # If all counts match, then s1 is a permutation of the current substring of s2
            if matches == 26: return True

            # Adjust the count for the new character in the window
            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            # Update the matches count if necessary
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1
            
            # Adjust the count for the character leaving the window
            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            # Update the matches count if necessary
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1
        
        # Check if all counts match at the end
        return matches == 26