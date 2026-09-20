# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        l2 = slow.next
        slow.next = None
        temp2 = l2
        prev = None
        while temp2:
            nxt = temp2.next
            temp2.next = prev
            prev = temp2
            temp2 = nxt
        l2 = prev
        temp = head
        temp2 = l2
        while temp2:
            nxt = temp.next
            nxt2 = temp2.next
            temp.next = temp2
            temp2.next = nxt
            temp2 = nxt2
            temp = nxt
        





