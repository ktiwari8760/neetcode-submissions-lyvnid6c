class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        def get_next_greater(index):
            value = nums2[index]
            for i in range(index+1 , len(nums2)):
                if nums2[i] > value:
                    return nums2[i]
            return -1

        hash = {}

        for i , ele in enumerate(nums2):
            hash[ele] = i
        
        answer = []
        for ele in nums1:
            nums2_index = hash[ele]
            answer.append(get_next_greater(nums2_index))
        return answer

        