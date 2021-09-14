class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        stack=[]
        n=len(s)
        l1=[None]*n
        for pos,alpha in enumerate(s):
            if alpha.isalpha():
                stack.append(alpha)
            else:
                l1[pos]=alpha
        for pos,alpha in enumerate(s):
            if alpha.isalpha():
                l1[pos]=stack.pop()
                
        return "".join(l1)
                    
                
                
                
                
        
