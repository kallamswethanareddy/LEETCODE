# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        for i in range(0,len(arr)-1,2):
            a=arr[i]
            b=arr[i+1]
            arr[i]=b
            arr[i+1]=a
        head1=ListNode()
        t=head1
        for i in arr:
            t.next=ListNode(i)
            t=t.next
        return head1.next