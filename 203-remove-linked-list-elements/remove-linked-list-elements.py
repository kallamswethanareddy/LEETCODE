# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        head1=ListNode()
        t=head1
        for i in arr:
            if i!=val:
                t1=ListNode(i)
                t.next=t1
                t=t.next
        return head1.next
