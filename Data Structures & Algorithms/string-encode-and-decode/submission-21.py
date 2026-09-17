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
            length = ""
            while s[index].isdigit():
                length += s[index]
                index += 1
            if length:
                length = int(length)
                answer.append(s[index+1 : index+length+1])
                index = index+length
            index += 1
        return answer