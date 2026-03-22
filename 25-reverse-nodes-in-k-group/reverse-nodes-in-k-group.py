# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        a=0
        b=k-1
        while b<len(arr):
            arr[a:b+1]=arr[a:b+1][::-1]
            a=b+1
            b=b+k
        head1=ListNode()
        t=head1
        for i in range(len(arr)):
            temp1=ListNode(arr[i])
            t.next=temp1
            t=t.next
        return head1.next