
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if len(B) < len(A):
            A, B = B, A

        total = len(A) + len(B)                  # CHANGED
        half = (total + 1) // 2                  # CHANGED

        left = 0
        right = len(A)                           # CHANGED

        while left <= right:
            mid = (left + right) // 2
            j = half - mid                        # CHANGED

            Aleft = A[mid - 1] if mid > 0 else float('-inf')  # CHANGED
            Aright = A[mid] if mid < len(A) else float('inf') # CHANGED

            Bleft = B[j - 1] if j > 0 else float('-inf')      # CHANGED
            Bright = B[j] if j < len(B) else float('inf')     # CHANGED

            if Aleft <= Bright and Bleft <= Aright:
                # Correct partition
                if total % 2:
                    return max(Aleft, Bleft)    # CHANGED
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                right = mid - 1                # CHANGED
            else:
                left = mid + 1
