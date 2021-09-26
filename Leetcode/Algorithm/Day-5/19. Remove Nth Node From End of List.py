# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:        
        first=head
        length=0
        
        while first:
            first=first.next
            length+=1
            
        rem=length-n
        
        if rem==0:
            head=head.next
            return head
        
        count=0
        first=head
        
        while first:
            if count==rem-1:
                first.next=first.next.next
                break
            first=first.next
            count+=1
            
        return head
            
            
        
