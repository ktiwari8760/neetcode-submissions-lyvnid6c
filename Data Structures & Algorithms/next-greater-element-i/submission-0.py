class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    ele = nums1[i]
                    j = j+1
                    while(j < len(nums2) and nums2[j] < ele ):
                        print("here" , j)
                        j+=1
                    if j == len(nums2):
                        answer.append(-1)
                    else:
                        answer.append(nums2[j])
        return answer