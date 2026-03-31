class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []
        def isPalindrome(string):
            left = 0
            right = len(string)-1

            while(left <= right):
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True
            
        def helper(start , path):
            # Base condition

            if start == len(s):
                answer.append(path.copy())
                return
            
            for end in range(start , len(s)):
                if isPalindrome(s[start:end+1]):
                    path.append(s[start:end+1])
                    helper(end+1 , path)
                    path.pop()
        helper(0 , [])
        return answer