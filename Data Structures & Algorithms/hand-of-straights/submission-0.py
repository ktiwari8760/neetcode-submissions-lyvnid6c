class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = {}
        for key in hand:
            freq[key] = 1 + freq.get(key, 0)
        hand.sort()

        print(freq)

        for ele in hand:
            print(ele , freq)
            min_freq = freq.get(ele)
            if min_freq <= 0:
                continue
            for internal_ele in range(ele , ele+groupSize):
                internal_ele_freq = freq.get(internal_ele , 0)
                if internal_ele_freq < min_freq:
                    return False
                if internal_ele in freq.keys():
                    freq[internal_ele] -= 1
                else:
                    return False
        print(freq)
        for key , value in freq.items():
            if value > 0:
                return False
        return True
