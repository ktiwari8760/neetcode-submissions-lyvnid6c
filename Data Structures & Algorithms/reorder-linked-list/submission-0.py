# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1 : Split linked list to half
        slow = head
        fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        # We reverse the linked list from here
        temp = mid
        prev = None
        while(temp):
            nextNode = temp.next
            temp.next = prev
            prev = temp
            temp = nextNode
        
        first, second = head, prev
        
        while second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2