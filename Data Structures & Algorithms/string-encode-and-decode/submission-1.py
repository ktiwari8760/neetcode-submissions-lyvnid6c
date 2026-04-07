class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for i in range(len(strs)):
            length = len(strs[i])
            s += str(length) + "#" + strs[i]
        return s

    def decode(self, strs: str) -> List[str]:
        string = []
        for i in range(len(strs)-1):
            if strs[i] in ["1","2","3","4","5","6","7","8","9","0"] and strs[i+1] == "#":
                length = int(strs[i])
                i += 2
                string.append(strs[i:i+length])
        return string
