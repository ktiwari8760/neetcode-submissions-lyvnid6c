class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for ele in strs:
            string += f"{len(ele)}#{ele}"
        return string

    def decode(self, s: str) -> List[str]:
        strings = []
        i = 0
        while(i < len(s)):
            j = i
            while(s[j] != "#"):
                j += 1
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            strings.append(word)
            i = j+1+length
        return strings



