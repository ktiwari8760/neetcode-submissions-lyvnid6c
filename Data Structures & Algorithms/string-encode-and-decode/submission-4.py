class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in range(len(strs)):
            length = len(strs[i])
            s += str(length) + "#" + strs[i]
        return s

    def decode(self, strs: str) -> List[str]:
        string = []
        i = 0
        while i < len(strs):
            j = i
            while strs[j] != "#":
                j+=1
            length = int(strs[i:j])
            i = j+1
            j = i+length
            string.append(strs[i:j])
            i = j
        return string