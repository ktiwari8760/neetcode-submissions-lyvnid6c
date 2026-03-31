class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_bits(k):
            res = 0

            for i in range(0 , 32):
                mask = 1 << i

                is_one = mask & k

                if is_one != 0:
                    res += 1
                else:
                    continue
            return res
        answer = []
        for j in range(0 , n+1):
            answer.append(count_bits(j))
        return answer

