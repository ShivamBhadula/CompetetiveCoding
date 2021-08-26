class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i=2
        while(c>=i*i):
            count=0
            if c%i==0:
                while(c%i==0):
                    count+=1
                    c=int(c/i)
                if i%4==3 and count%2!=0:
                    return False
            i+=1
        if (c%4!=3):
            return True
        else:
            return False
        
     
