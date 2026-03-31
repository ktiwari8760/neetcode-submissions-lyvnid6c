class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def helper(current , open_count , close_count):
            if len(current) == 2*n:
                answer.append(current)
                return
            if open_count < n:
                helper(current + "(" , open_count+1 , close_count)
            if close_count < open_count:
                helper(current + ")" , open_count , close_count+1)
        helper("" , 0 , 0)
        return answer
