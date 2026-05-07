class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def helper(substring , open_ , close):
            if len(substring) == n*2 and open_ == close:
                print(substring)
                answer.append(substring)
                return
            if len(substring) > n*2:
                return
            if open_  < n:
                helper(substring + "(" , open_+1 , close)
            if close < open_:
                helper(substring + ")" , open_ , close+1)
        
        helper("" , 0 , 0)
        return answer