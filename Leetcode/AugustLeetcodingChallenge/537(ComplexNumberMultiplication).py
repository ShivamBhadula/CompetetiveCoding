class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        char1=num1.find('+')
        char2=num2.find('+')
        r1=int(num1[0:char1])
        r2=int(num2[0:char2])
        i1=int(num1[char1+1:-1])
        i2=int(num2[char2+1:-1])
        mul=(r1*r2)+(i1*i2*-1)
        s1=(r1*i2)+(r2*i1)
        res=str(mul)+'+'+str(s1)+'i'
        return res
        
