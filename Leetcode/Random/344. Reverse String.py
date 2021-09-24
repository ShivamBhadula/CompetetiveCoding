class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start=0
        end=-1
        for i in range(len(s)//2):
            s[start],s[end]=s[end],s[start]
            start=start+1
            end=end-1
