class Solution:

    def encode(self, strs: List[str]) -> str:
        string_ = ""
        for ele in strs:
            length = len(ele)
            string_ += f"{length}#{ele}"
        print(string_)
        return string_
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while(i < len(s)):
            j = i
            while(s[j] != "#"):
                j += 1
            if s[i:j].isdigit():
                length = int(s[i:j])
                start = j+1
                end = start + length
                result.append(s[start:end])
                i = end
            else:
                i += 1
        return result
        