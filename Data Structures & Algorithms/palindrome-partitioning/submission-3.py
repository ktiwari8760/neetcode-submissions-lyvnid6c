class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def isPalindrome(string):
            return string == string[::-1]
        answer = []
        def helper(index , arr):
            if index == len(s):
                answer.append(arr.copy())
                return
            for i in range(index , len(s)):
                if isPalindrome(s[index:i+1]):
                    arr.append(s[index:i+1])
                    helper(i+1 , arr)
                    arr.pop()
        helper(0 , [])
        return answer