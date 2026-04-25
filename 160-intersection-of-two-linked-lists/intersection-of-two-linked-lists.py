# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lista=headA
        listB=headB
        while lista!=listB:
            lista=lista.next if lista else headB
            listB=listB.next if listB else headA
        return listB