# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        a,b=[],[]
        for i in range(len(arr)):
            if i%2!=0:
                a.append(arr[i])
            else:
                b.append(arr[i])
        b.extend(a)
        head1=ListNode()
        t=head1
        for i in range(len(b)):
            temp1=ListNode(b[i])
            t.next=temp1
            t=t.next
        return head1.next