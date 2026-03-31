class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []

        def helper(open_count , closed_count , string):
            if len(string) == n*2:
                answer.append(string)
                return 
            if len(string) > n*2:
                return
            if open_count< n:
                helper(open_count+1 , closed_count , string+"(")
            if closed_count < open_count:
                helper(open_count , closed_count+1 , string+")")
        helper(0 , 0 , "")
        return answer