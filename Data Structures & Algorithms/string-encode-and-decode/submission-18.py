class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for ele in strs:
            s += str(len(ele))
            s += "#"
            s += ele
        return s

    def decode(self, s: str) -> List[str]:
        index = 0
        answer = []
        while(index < len(s)):
            if s[index].isdigit() and index+1 <= len(s)-1 and s[index+1] == "#":
                answer.append(s[index+2 : index+2+int(s[index])])
                index += 2 + int(s[index])
            else:
                index += 1
        return answer