class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left1 = m-1
        left2 = n-1
        right1 = len(nums1)-1

        while(left1 >= 0 and left2 >= 0):
            if nums1[left1] > nums2[left2]:
                nums1[left1] , nums1[right1] = nums1[right1] , nums1[left1]
                left1 -= 1
                right1 -= 1
            else:
                nums2[left2] , nums1[right1] = nums1[right1] , nums2[left2]
                left2 -= 1
                right1 -= 1
        
        while(left2 >= 0):
            nums2[left2] , nums1[right1] = nums1[right1] , nums2[left2]
            left2 -= 1
            right1 -= 1
        
        