class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        ans=[]
        for val in nums:
            if val%2==0:
                even.append(val)
            else:
                odd.append(val)
        
        for i in range(len(nums)//2):
            ans.append(even[i])
            ans.append(odd[i])
            
        return ans
    
        
                
                
        
                    
        
