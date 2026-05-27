class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        if n == 0:
            return []
        if n == 1:
            return [[1]]
        answer = [[1]]

        for i in range(n-1):
            nums = [0] + answer[-1].copy() + [0]
            level_arr = []
            a = 0
            b = 1
            while(b < len(nums)):
                level_arr.append(nums[a]+ nums[b])
                a +=1
                b +=1
            answer.append(level_arr)
        return answer

