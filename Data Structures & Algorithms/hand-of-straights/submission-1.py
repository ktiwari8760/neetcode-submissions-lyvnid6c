class Solution:
    def isNStraightHand(self, hand: List[int], gs: int) -> bool:
        n = len(hand)
        if len(hand) % gs != 0:
            return False
        hash = {}
        for ele in hand:
            hash[ele] = hash.get(ele , 0) + 1
        hand.sort()
        max_ele = max(hand)
        answer= [[] for i in range(n // gs)]
        print(answer)
        for i , ele in enumerate(hand):
            to_add = ele
            flag = False
            for ans in answer:
                if len(ans) >= gs:
                    continue
                if (not ans) or (ans[-1] == to_add-1):
                    ans.append(to_add)
                    flag = True
                    break
            if not flag:
                return False
        return True
