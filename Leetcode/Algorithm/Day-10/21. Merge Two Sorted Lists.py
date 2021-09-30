# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
       def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            p1, p2, res = l1, l2, ListNode()
            p3 = res
            while p1 and p2:
                if p1.val < p2.val:
                    p3.next = p1
                    p1 = p1.next
                else:
                    p3.next = p2
                    p2 = p2.next
                p3 = p3.next
            p3.next = p1 if p1 else p2 # splice the rest from either @p1 or @p2
            return res.next
        
