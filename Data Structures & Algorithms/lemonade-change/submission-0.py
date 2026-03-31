class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill5 = 0
        bill10 = 0
        bill20 = 0
        flag = True
        for ele in bills:
            if ele == 5:
                bill5 += 1
            if ele == 10:
                if bill5 >= 1:
                    bill5 -= 1
                    bill10 += 1
                else:
                    return False
            if ele == 20:
                if bill5 >= 3:
                    bill5 -= 3
                    bill20 += 1
                elif bill10 >= 1 and bill5 >= 1:
                    bill10 -= 1
                    bill5 -= 1
                    bill20 += 1
                else:
                    return False
        return True
