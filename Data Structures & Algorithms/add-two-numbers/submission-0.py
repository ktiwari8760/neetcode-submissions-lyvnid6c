# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(-1)
        temp = dummyNode
        carry = 0
        temp1 = l1
        temp2 = l2

        while(temp1 and temp2):
            sum_ = temp1.val + temp2.val + carry

            value = sum_ % 10
            carry = sum_ // 10

            temp.next = ListNode(value)

            temp = temp.next
            temp1 = temp1.next
            temp2 = temp2.next
        
        while(temp1):
            sum_ = temp1.val+ carry
            value = sum_ % 10
            carry = sum_ // 10
            temp.next = ListNode(value)
            temp = temp.next
            temp1 = temp1.next
        while(temp2):
            sum_ = temp2.val + carry
            value = sum_ % 10
            carry = sum_ // 10
            temp.next = ListNode(value)
            temp = temp.next
            temp2 = temp2.next
        if carry:
            temp.next = ListNode(carry)
            temp = temp.next
        
        return dummyNode.next


            