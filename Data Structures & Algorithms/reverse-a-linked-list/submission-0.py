# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr != None:
            # store the next node
            next = curr.next
            # reverse the link
            curr.next = prev
            # move pointers one step ahead
            prev = curr
            curr = next
        head = prev
        return head