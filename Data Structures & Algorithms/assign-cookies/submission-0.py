class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # We have to maximise this 

        g.sort() # O(n log n ) --> greed of the child
        s.sort() #  O(n log n ) --> cookies

        greed = 0
        cookie = 0
        counter = 0
        while greed < len(g) and cookie < len(s):
            if g[greed] <= s[cookie]:
                greed += 1
                cookie += 1
                counter += 1
            else:
                cookie += 1
        return counter

