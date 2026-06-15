# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        if len(arr)==1:
            return None
        mid = len(arr) // 2
        head1=ListNode()
        t=head1
        for i in range(len(arr)):
            if i!=mid:
                t.next=ListNode(arr[i])
                t=t.next
        return head1.next