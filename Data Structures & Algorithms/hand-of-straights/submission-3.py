class Solution:
    def isNStraightHand(self, hand: List[int], gs: int) -> bool:
        from collections import Counter

        hash = Counter(hand)

        hand.sort()

        for ele in hand:
            while(hash[ele] > 0):
                for e in range(ele , ele+gs):
                    if hash.get(e , 0) == 0:
                        return False
                    hash[e] -= 1
        return True