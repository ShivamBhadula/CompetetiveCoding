class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums=[x**2 for x in nums]
        nums.sort()
        return nums
        
