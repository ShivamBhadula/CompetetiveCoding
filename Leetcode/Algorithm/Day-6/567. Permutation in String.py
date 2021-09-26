class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        
        for i in range(len(s2)):
            window=s2[i:len(s1)+i]
            if Counter(window)==Counter(s1):
                return True
            
        return False
            
            
        
        
