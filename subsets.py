class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] #to hold all possible subsets

        def backtrack(start, current):
            nonlocal res 
            res.append(current[:]) #append the current subset
            for i in range(start, len(nums)):
                #include current number from nums 
                current.append(nums[i])
                #move to next element in nums
                backtrack(i + 1, current)
                ##backtrack, remove the number from the current subset to explore next possible subset
                current.pop()

        backtrack(0, [])
        return res 


