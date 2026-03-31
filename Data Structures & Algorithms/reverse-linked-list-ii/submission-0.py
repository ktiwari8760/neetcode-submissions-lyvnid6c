class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        def reverse_linked_list(left_node, right_node, left_prev, right_next):
            temp2 = left_node
            prev = right_next   # ✅ important fix

            # reverse till right_node (inclusive)
            while temp2 != right_next:
                temp3 = temp2.next
                temp2.next = prev
                prev = temp2
                temp2 = temp3

            # connect left_prev to new head
            if left_prev:
                left_prev.next = prev

            return prev   # new head of reversed part

        
        l = left - 1
        r = right - 1

        if l > r or l < 0 or r < 0:
            return head   # ✅ fix

        temp = head
        counter = 0
        prev = None

        left_prev = None
        right_next = None 
        left_pointer = None

        while temp:
            if counter == l:
                left_pointer = temp
                left_prev = prev
            if counter == r:
                right_next = temp.next
                break   # ✅ stop early once right found
            prev = temp
            temp = temp.next
            counter += 1

        # reverse
        new_head_part = reverse_linked_list(left_pointer, temp, left_prev, right_next)

        # if reversing from head
        if left_prev is None:
            return new_head_part   # ✅ new head

        return head   # otherwise original head stays