class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        answer = []
        for ele in range(1 , len(nums)+1):
            if not ele in set(nums):
                answer.append(ele)
        return answer