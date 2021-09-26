class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''sliding window approach'''
        window={}
        start=0
        end=0
        longest=0
        
        while end < len(s) and start<=end:
            
            if s[end] in window:
                window.pop(s[start])
                start+=1
                
            else:
                window[s[end]]=True
                end+=1
                
                longest=max(longest,len(window))
                
        return longest
            
                
                    
            
            
            
            
        
