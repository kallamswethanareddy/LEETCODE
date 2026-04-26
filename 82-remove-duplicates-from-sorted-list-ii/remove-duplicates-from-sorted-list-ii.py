# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        a=[]
        temp=head
        while temp:
            arr.append(temp.val)
            temp=temp.next
        arr1=list(set(arr))
        for i in arr1:
            if arr.count(i)!=1:
                a.append(i)
        a1=[i for i in arr if i not in a]
        head1=ListNode()
        t=head1
        for i in a1:
            t.next=ListNode(i)
            t=t.next
        return head1.next