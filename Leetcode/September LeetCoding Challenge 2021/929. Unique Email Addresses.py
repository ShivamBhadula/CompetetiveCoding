class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        l1=set()
        ind=-1
        for i in emails:
            word=''
            for val in i:
                
                if val=='.':
                    continue
                    
                if val=='+' or val=='@':
                    ind=i.find('@')
                    break

                word+=val
                
            word+=i[ind:]
            l1.add(word)
        return len(l1)
                
            
        
