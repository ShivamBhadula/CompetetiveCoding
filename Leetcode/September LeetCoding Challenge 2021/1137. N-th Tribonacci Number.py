class Solution:
    def tribonacci(self, n: int) -> int:
        first=0
        second=third=1
        if n==0:
            return first
        if n==1 or n==2:
            return second
        
        for i in range(3,n+1):
            ans=first+second+third
            first=second
            second=third
            third=ans
            
        return ans
        
