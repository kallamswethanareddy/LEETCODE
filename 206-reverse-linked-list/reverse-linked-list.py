# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next
        if not arr:
            return None
        head1 = ListNode(arr[-1])
        t = head1
        for i in range(len(arr)-2, -1, -1):
            temp1 = ListNode(arr[i])
            t.next = temp1
            t=t.next
        return head1
