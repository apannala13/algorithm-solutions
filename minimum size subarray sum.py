class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, summ, res = 0, 0, float('inf')
        
        for r in range(0, len(nums)):
            summ += nums[r]
            
            while summ >= target:
                res = min(res, r-l+1)
                summ -= nums[l]
                l += 1
        
        return res if res != float('inf') else 0 
    
    
                
