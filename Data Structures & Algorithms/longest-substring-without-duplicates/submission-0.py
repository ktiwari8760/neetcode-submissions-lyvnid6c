class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        counter = 0
        maxcounter = 0
        start = 0
        for ele in s:
            if ele not in hashset:
                hashset.add(ele)
                counter += 1    
                maxcounter = max(maxcounter , counter)
            else:
                start += 1
                counter = 0
                hashset = set()
        return maxcounter

