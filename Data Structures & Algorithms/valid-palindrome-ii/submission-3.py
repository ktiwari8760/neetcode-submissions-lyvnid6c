class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def function(left , right):
            print(s[left:right+1])
            while (left <= right):
                if s[left] != s[right]:
                    return False , left , right
                left += 1
                right -= 1
            return True , left , right
        
        left = 0
        right = len(s)-1
        flag = False
        while left <= right:
            ans , ans_left , ans_right = function(0 , right)
            if ans == False and not flag:
                flag = True
                ans1 , ans1_left , ans1_right = function(ans_left+1 , ans_right)
                ans2 , ans2_left , ans2_right = function(ans_left , ans_right-1)
                print(ans1  ,ans2)
                if ans1 or ans2:
                    return True
                else:
                    return False
            if ans:
                return True
            left += 1
            right -= 1
        return False