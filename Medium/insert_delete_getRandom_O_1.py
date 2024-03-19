"""
Problem Link: https://leetcode.com/problems/insert-delete-getrandom-o1/description/

Topics: Array, Hash Table, Math, Design, Randomized

Time Complexity: O(n)
Space Complexity: O(n)

"""
import random

class RandomizedSet_1:
    def __init__(self):
        self.values = []
    
    def insert(self, val: int) -> bool:
        if val not in self.values:
            self.values.append(val)
            return True
        else:
            return False
        
    def remove(self, val: int) -> bool:
        if val in self.values:
            self.values.remove(val)
            return True
        else:
            return False
    
    def getRandom(self) -> int:
        return random.choices(self.values)
    


class RandomizedSet_2:
    def __init__(self):
        self.numMap = {}
        self.numList = []
    
    def insert(self, val: int) -> bool:
        # does the value exist?
        result = val not in self.numMap
        
        if result: # if it does not exist
            # add it to the map
            self.numMap[val] = len(self.numList)
            self.numList.append(val)
        return result
    
    def remove(self, val: int) -> bool:
        result = val in self.numMap

        if result: # if true, we are able to remove it
            # get the index from the hashMap
            idx = self.numMap[val]
            lastVal = self.numList[-1]
            self.numList[idx] = lastVal
            self.numList.pop()
            self.numMap[lastVal] = idx
            del self.numMap[val]
        return result
    
    def getRandom(self) -> int:
        return random.choice(self.numList)
    



def test_randomized_set(set_class):
    operations = ["insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
    values = [[1], [2], [2], [], [1], [2], []]
    expected_outputs = [None, True, False, True, "Random", True, False, "Random"]
    
    obj = set_class()  # Create an instance of RandomizedSet_1 or RandomizedSet_2
    print("Testing:", obj.__class__.__name__)
    
    for i, operation in enumerate(operations):
        if operation == "insert":
            result = obj.insert(*values[i])
            print(f"{operation}({values[i][0]}): Expected {expected_outputs[i]}, got {result}")
        elif operation == "remove":
            result = obj.remove(*values[i])
            print(f"{operation}({values[i][0]}): Expected {expected_outputs[i]}, got {result}")
        elif operation == "getRandom":
            result = obj.getRandom()
            print(f"{operation}(): Got {result}")
    
    print("-----")

# Test RandomizedSet_1
# test_randomized_set(RandomizedSet_1)

# Test RandomizedSet_2
test_randomized_set(RandomizedSet_2)
