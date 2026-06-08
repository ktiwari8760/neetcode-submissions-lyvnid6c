class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid_triplets = []
        for ele in triplets:
            if not any([ele[i] > target[i] for i in range(3)]):
                valid_triplets.append(ele)
        for i in range(3):
            flag = False
            for ele in valid_triplets:
                if ele[i] == target[i]:
                    flag = True
            if not flag:
                return False
        return True
