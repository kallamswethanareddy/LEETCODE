# Definition for singly-linked list.
# class ListNode:
def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1=[]
        arr2=[]
        t1=l1
        t2=l2
        while t1:
            arr1.append(t1.val)
            t1=t1.next
        while t2:
            arr2.append(t2.val)
            t2=t2.next
        arr1=arr1[::-1]
        arr2=arr2[::-1]
        s1=''
        s2=''
        for i in arr1:
            s1+=str(i)
        for j in arr2:
            s2+=str(j)
        ans=str(int(s1)+int(s2))
        ans=ans[::-1]
        head1=ListNode()
        t=head1
        for i in ans:
            temp1=ListNode(int(i))
            t.next=temp1
            t=t.next
        return head1.next