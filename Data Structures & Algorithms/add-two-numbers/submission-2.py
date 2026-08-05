# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        temp1 = l1
        temp2 = l2
        temp = dummy
        carry = 0
        while(temp1 and temp2):
            sum_ = temp1.val +temp2.val + carry

            newNode = ListNode(sum_ % 10)

            carry = sum_ // 10

            temp.next = newNode

            temp = temp.next
            temp1 = temp1.next
            temp2 = temp2.next
        
        while(temp1):
            sum_ = temp1.val+carry
            newNode = ListNode(sum_ % 10)
            carry = sum_ // 10
            temp.next = newNode
            temp1 = temp1.next
            temp = temp.next
        while temp2:
            sum_ = temp2.val+carry
            newNode = ListNode(sum_ % 10)
            carry = sum_ // 10
            temp.next = newNode
            temp2 = temp2.next
            temp = temp.next
        if carry:
            temp.next = ListNode(carry)
        return dummy.next


