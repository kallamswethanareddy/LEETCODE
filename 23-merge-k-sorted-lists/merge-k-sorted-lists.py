# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr=[]
        for l in lists:
            while l:
                arr.append(l.val)
                l=l.next
        if not arr:
            return None
        arr.sort()

        head1=ListNode()
        t=head1
        for i in arr:
            temp=ListNode(i)
            t.next=temp
            t=t.next
        return head1.next