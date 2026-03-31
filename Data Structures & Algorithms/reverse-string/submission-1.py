class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # One way could have been if we had returned s[::-1] but since we have to
        # Modify the original list
        # we use two pointer algorithm
        # left at start and right at end and swap each element
        left = 0
        right = len(s)-1

        while(left <= right):
            s[left] , s[right] = s[right] , s[left]
            left += 1
            right -= 1
            
        