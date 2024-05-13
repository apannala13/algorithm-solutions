import math 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #O(log (max(p)) * p)

        l, r = 1, max(piles)

        #maximum value in piles, which is the highest possible speed
        res = max(piles)

        while l <= r:
            #midpoint 'k', the current candidate for the minimum speed
            k = (l + r)//2
            #track total hours needed with the current speed 'k'
            hours = 0
            #calculate the hours needed to eat the pile at speed 'k'
            #e.g.: 3/2 + 6/2 + 7/2 + 11/2 should be <= k
            for pile in piles:
                hours += math.ceil((pile/k)) #round up since partial hours count as full hours
            #If the total hours with speed 'k' are less than or equal to 'h'
            if hours <= h:
                res = min(res, k) #update 'res' to the smaller of the current 'res' or 'k'
                r = k - 1 #decrease 'r' to narrow the search bounds, ignoring speeds higher than 'k'
            else:
                l = k + 1 #increase 'l' to narrow the search bounds, ignoring speeds lower than 'k'
        return res #smallest speed found that allows all bananas to be eaten within 'h' hours
        
