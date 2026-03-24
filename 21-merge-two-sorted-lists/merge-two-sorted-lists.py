# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        a1=[]
        temp1=list1
        a2=[]
        temp2=list2
        while temp1:
            a1.append(temp1.val)
            temp1=temp1.next
        while temp2:
            a2.append(temp2.val)
            temp2=temp2.next
        a1.extend(a2)
        a1.sort()
        head1=ListNode()
        t1=head1
        for i in range(len(a1)):
            b=ListNode(a1[i])
            t1.next=b
            t1=t1.next
        return head1.next