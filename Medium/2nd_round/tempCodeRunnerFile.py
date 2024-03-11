    def countSubstringsDiffByOneChar(s: str, t: str) -> int:
        def countMatches(s, t):
            count = 0
            for i in range(len(s)):
                for j in range(len(t)):
                    mismatch = 0
                    k = 0
                    while i + k < len(s) and j + k < len(t) and mismatch <= 1:
                        if s[i + k] != t[j + k]:
                            mismatch += 1
                        if mismatch == 1:
                            count += 1
                        k += 1
            return count
        
        return countMatches(s, t)
                        
                    