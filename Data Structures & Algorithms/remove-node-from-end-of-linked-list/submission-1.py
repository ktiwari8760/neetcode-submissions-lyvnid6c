# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        counter = 0

        while(fast):
            fast = fast.next
            counter += 1
            if counter == n:
                break
        slow = head
        prev = None
        while(fast):
            fast = fast.next
            prev = slow
            slow = slow.next
        if prev:
            prev.next = prev.next.next
            return head
        else:
            return head.next