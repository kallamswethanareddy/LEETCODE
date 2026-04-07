# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        b=[i for i in arr if i<x]
        c=[i for i in arr if i>=x]
        d=b+c
        head1=ListNode()
        t=head1
        for i in d:
            t.next=ListNode(i)
            t=t.next
        return head1.next