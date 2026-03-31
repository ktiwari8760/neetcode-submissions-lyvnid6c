class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        length = sum(matchsticks) //4

        sides = [0] * 4

        matchsticks.sort(reverse = True)

        def helper(index):
            if index == len(matchsticks):
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[index] <= length:
                    sides[j] += matchsticks[index]
                    if helper(index+1):
                        return True
                    sides[j] -= matchsticks[index]
            return False
        return helper(0)