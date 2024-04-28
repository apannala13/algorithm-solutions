class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1 or not s2 or len(s1) > len(s2):
            return False 
        hash1, hash2 = {}, {}
        
        for i in range(len(s1)):
            hash1[s1[i]] = 1 + hash1.get(s1[i], 0)
        
        for i in range(len(s1)):
            if i < len(s2):
                hash2[s2[i]] = 1 + hash2.get(s2[i], 0)
            
            
        def helper(hash1, hash2):
            return True if hash1 == hash2 else False
        
        
        l = 0 
        for r in range(len(s1), len(s2)):
            if helper(hash1, hash2):
                return True
            hash2[s2[r]] = 1 + hash2.get(s2[r], 0)
            hash2[s2[l]] -= 1 
            if hash2[s2[l]] == 0:
                del hash2[s2[l]]
            l += 1
        
        return True if helper(hash1, hash2) else False



