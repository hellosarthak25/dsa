# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head==None:
            return None
        if left==right:
            return head
        t=head
        before=None
        pos=1
        while pos<left:
            before=t
            t=t.next
            pos+=1
        curr=t
        prev=None
        times=right-left+1
        while(times!=0):
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex
            times-=1
        if before!=None:
            before.next=prev
            t.next=curr
            return head
        else:
            t.next=curr
            return prev


