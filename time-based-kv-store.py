
"""
Design a time based key value data structure that can store 
multiple values for the same key at diff time stamps
and retrieve the key's value at a certain timestamp.

timestamp_prev <= timestamp 

binary serach O(log n) implementation.
    
"""

class TimeMap:
    def __init__(self):
        self.hashmap = {} #will store key with list of (timestamp, value) pairs
        
    def set(self, key:str, value:str, timestamp:int) -> None:
        if not key in self.hashmap:
            #if new key, initialize empty list for (timestamp, value) pairs
            self.hashmap[key] = []      
        #append (timestamp, value) tuple to list for key 
        self.hashmap[key].append((timestamp, value))

    
    def get(self, key:str, timestamp:int) -> str:
        if not key in self.hashmap:
            return "" #if key not found

        values = self.hashmap[key] #get list of (timestamp, value) pairs for the key
        res = ""
        l, r = 0, len(values) - 1

        while l <= r:
            mid = (l + r)//2
            if values[mid][0] <= timestamp: 
                res = values[mid][1] #update res if current timestamp <= target timestamp
                l = mid + 1 #update left to find closer timestamp
            else:
                r = mid - 1 #too high, move right pointer left

        return res 

if __name__ == "__main__":
    t = TimeMap()
    t.set("sample", "data", 1)
    print(t.get("sample", 1))
    print(t.get("sample", 2))
    
                
        

        
