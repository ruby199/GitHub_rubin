# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Overall, the TimeMap class uses a dictionary to store values and timestamps for each key and employs binary search to efficiently retrieve the value corresponding to the closest timestamp that is not greater than the given timestamp.

class TimeMap:

    def __init__(self):
        self.store = {} # key=string, value=[list of value, timestamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # O(1)
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])

        # binary search
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
            



# TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)