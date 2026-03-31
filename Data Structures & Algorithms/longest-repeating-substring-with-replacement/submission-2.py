class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        left = 0
        max_f = 0
        length = 0
        for right in range(len(s)):
            hashmap[s[right]] = hashmap.get(s[right] , 0) + 1
            max_f = max(max_f , hashmap[s[right]])

            while((right-left+1)-max_f > k):
                hashmap[s[left]] -= 1
                left += 1 
            length = max(length , right-left+1)
        return length