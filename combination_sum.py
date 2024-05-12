class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] #store all unique combinations that sum up to target
        
        def backtrack(start, combination, current_sum):
            #if current sum == target, add current combination to target
            if current_sum == target:
                res.append(combination[:])
                return #return to explore other combinations
            
            #if current sum exceeds path, stop exploring
            if current_sum > target:
                return
            
            #iterate thru nums starting from start index to avoid using same elements repeatedly
            for i in range(start, len(candidates)):
                #add current number to combination
                combination.append(candidates[i])
                #recurse with updated sum and current index [i], not i + 1 because we can reuse elements
                backtrack(i, combination, current_sum + candidates[i])
                #remove last element added to backtrack to explore next potential number
                combination.pop()
                
        backtrack(0, [], 0)
        return res