class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0 
        for weight in w:
            prefix_sum += weight 
            print(prefix_sum)
            self.prefix_sums.append(prefix_sum)
        self.total = prefix_sum
        print(self.total)

    def pickIndex(self) -> int:
        target = self.total * random.random()
        
        l, r = 0, len(self.prefix_sums)

        while l < r:
            mid = (l + r)//2
            if target > self.prefix_sums[mid]:
                l = mid + 1
            else:
                r = mid 
        return l 


