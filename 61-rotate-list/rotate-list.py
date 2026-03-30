# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        
        k=k%len(arr)
        if k==0:
            return head
        arr[:]=arr[-k:]+arr[:-k]
        head1=ListNode()
        t=head1
        for i in range(len(arr)):
            temp1=ListNode(arr[i])
            t.next=temp1
            t=t.next
        return head1.next