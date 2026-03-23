# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        arr[left-1:right]=arr[left-1:right][::-1]
        head1=ListNode()
        t=head1
        for i in range(len(arr)):
            temp1=ListNode(arr[i])
            t.next=temp1
            t=t.next
        return head1.next