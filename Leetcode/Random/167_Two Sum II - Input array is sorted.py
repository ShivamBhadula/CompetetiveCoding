class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        low=0
        high=len(nums)-1
        
        while low<=high:
            
            if nums[low]+nums[high]==target:
                return low+1,high+1
            
            elif nums[low]+nums[high]<target:
                low=low+1
                
            else:
                high=high-1
                
            
        
