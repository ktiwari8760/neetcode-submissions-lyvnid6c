class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # We can have maximum of 2 elements such which are having elements more than n/3

        freq_a = 0
        freq_b = 0
        a = None
        b = None

        for ele in nums:
            if freq_a == 0:
                a = ele
                freq_a += 1
            elif freq_b == 0 and ele != a:
                freq_b += 1
                b = ele
            elif ele == a:
                freq_a += 1
            elif ele == b:
                freq_b += 1
            else:
                freq_a -= 1
                freq_b -= 1
        print(a , b)

        freq_a = 0
        freq_b = 0

        for ele in nums:
            if ele == a:
                freq_a += 1
            elif ele == b:
                freq_b += 1
        answer = []
        if freq_a > len(nums)/3:
            answer.append(a)
        if freq_b > len(nums)/3:
            answer.append(b)
        return answer