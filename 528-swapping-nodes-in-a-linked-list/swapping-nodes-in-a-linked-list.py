# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        a=arr[k-1]
        b=arr[-k]
        arr[-k]=a
        arr[k-1]=b
        head1=ListNode()
        t=head1
        for i in arr:
            t.next=ListNode(i)
            t=t.next
        return head1.next