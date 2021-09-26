class Solution:
    def reverseWords(self, s: str) -> str:
        
        l1=list(s.split())
        revstr=''
        for i in range(len(l1)):
            revstr=revstr+" "+l1[i][::-1]
        revstr=revstr.replace(" ","",1)  
        return revstr
            
                
        
