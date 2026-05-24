class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if len(s) == len(t):
            if s == t:
                return s 
        hash = {}
        for ele in t:
            hash[ele] = hash.get(ele , 0) + 1
        print(hash)
        left = 0
        right = 0
        answer = ""
        while(left <= right and right < len(s)):
            print(right)
            if s[right] in hash.keys():
                counter = 1
                local_hash =hash.copy() 
                local_hash[s[right]] -= 1
                substring = s[right]
                falg = False
                for i in range(right+1 , len(s)):
                    if counter == len(t):
                        falg = True
                        break
                    if s[i] in local_hash and local_hash[s[i]] > 0:
                        local_hash[s[i]] -= 1
                        counter += 1
                    substring += s[i]
                if falg or counter == len(t):
                    if not answer:
                        answer = substring
                    elif len(answer) > len(substring):
                        answer = substring
            right += 1
        return answer
