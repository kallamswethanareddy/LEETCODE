# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        arr=[]
        temp=head
        while temp:
            if temp in arr:
                return True
            arr.append(temp)
            temp=temp.next
        return False