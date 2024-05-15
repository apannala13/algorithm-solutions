class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, end):
            if start == end: #generated complete permutation
                ans.append(nums[:])
            
            for i in range(start, end): #from start to end of nums list
                nums[start], nums[i] = nums[i], nums[start] #swap 
                backtrack(start + 1, end) #increment 
                nums[start], nums[i]  = nums[i], nums[start] #swap elements back to original positions, to explore other possibilities
                
        
        ans = []
        backtrack(0, len(nums)) #start backtracking from first index 
        return ans