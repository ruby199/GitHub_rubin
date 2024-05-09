        self.permute(half, 0, mid, result)
        return list(result)
        
    def canPermutePalindrome(self, counter):
        return sum(count % 2 for count in counter.values()) <= 1
        # odd_count = sum(1 for count in counter.values() if count % 2 != 0)
        # if odd_count > 1:
        #     return -1

    def permute(self, s, l, mid, result):
        if l == len(s):
            palindrome = ''.join(s) + (mid or '') + ''.join(s[::-1])
            result.add(palindrome)
        else:
            seen = set()
            for i in range(l, len(s)):
                if s[i] not in seen:
                    self.swap(s, l, i)
                    self.permute(s, l + 1, mid, result)
                    self.swap(s, l, i)

