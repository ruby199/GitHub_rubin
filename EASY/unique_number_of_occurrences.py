class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        occurrence = list()
        for i in range(len(arr)):
            if count[i] in occurrence:
                return False
            occurrence.append(count[i])
        return True

# class Solution:
    # def uniqueOccurrences(self, arr: List[int]) -> bool:
    #     count = Counter(arr)
    #     return len(count.values()) == len(set(count.values()))