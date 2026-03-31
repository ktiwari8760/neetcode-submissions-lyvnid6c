class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        answer = []
        def isPalindrome(left , right):
            while(left<= right):
                if s[left] != s[right]:
                    return False
                left+=1
                right -= 1
            return True
        
        def helper(start , path):
            if start == len(s):
                answer.append(path.copy())
                return 
            
            for end in range(start , len(s)):
                if isPalindrome(start , end):
                    path.append(s[start:end+1])
                    helper(end+1 , path)
                    path.pop()
        helper(0 , [])
        return answer
