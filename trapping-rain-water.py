class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        #store the maximum heights encountered from the left and right sides
        #will store max water level up to that point 
        leftheight, rightheight = height[l], height[r]
        
        #total water accumulated
        res = 0 
        
        #until pointers meet
        while l < r:
            #move the pointer from the side with the shorter height because the
            #height of the shorter side limits the maximum water level
            if height[l] < height[r]:
                l += 1
                #update the maximum height seen so far from the left
                leftheight = max(leftheight, height[l])
                 #the difference between the current maximum height and the current height
                #is the volume of water that can be trapped at this index
                res += leftheight - height[l]
            else:
                r -= 1
                #same principle as left
                rightheight = max(rightheight, height[r])
                #same principle here
                res += rightheight - height[r]
                
        return res 
    

        
