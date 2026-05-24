class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if s == t:
            return s
        
        need = {}

        for ele in t:
            need[ele] = need.get(ele , 0) + 1
        
        print(need)

        have = {}
        formed = 0
        required = len(need)
        answer = [-1 , -1]
        max_length = float('inf')
        left = 0
        for right in range(len(s)):
            curr = s[right]
            have[curr] = have.get(curr , 0) + 1
            if curr in need and have[curr] == need[curr]:
                formed += 1
            while(formed == required):
                if (right - left+1) < max_length:
                    max_length = right-left+1
                    answer = [left , right]
                left_ele = s[left]
                have[left_ele] -= 1
                if left_ele in need and need[left_ele] > have[left_ele]:
                    formed -= 1
                left += 1
        l , r = answer
        return s[l:r+1] if l != -1 and r != -1 else ""

