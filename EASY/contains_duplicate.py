class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # sorting the list can help reduce the time complexity
        # Time: O(nlogn), Space: O(1)

        # Trade-Off: if better  time complexity and worst space complexity (use Hash Set)
        # Time: O(n), Space(n)

        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False