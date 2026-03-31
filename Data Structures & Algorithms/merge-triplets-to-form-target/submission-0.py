class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid_triplets = []
        for ele in triplets:
            counter = 0
            for i in range(3):
                if ele[i] <= target[i]:
                    counter += 1
            if counter == 3:
                valid_triplets.append(ele)
        
        for i in range(3):
            local_counter = 0
            for ele in valid_triplets:
                if ele[i] == target[i]:
                    local_counter += 1
            if local_counter == 0:
                return False
        return True
