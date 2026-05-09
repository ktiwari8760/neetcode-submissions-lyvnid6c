class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchstick_total = sum(matchsticks)
        if matchstick_total % 4 != 0:
            return False
        sidelength = matchstick_total// 4
        if any(ele > sidelength for ele in matchsticks ):
            return False
        sides = [0] * 4
        def helper(index , sides):
            if index == len(matchsticks) and sides[0] == sidelength:
                for ele in sides:
                    if ele != sidelength:
                        return False
                return True
            if any(side > sidelength for side in sides):
                return False
            
            for i in range(len(sides)):
                if sides[i] < sidelength and sides[i] + matchsticks[index] <= sidelength:
                    sides[i] +=  matchsticks[index]
                    if helper(index + 1 , sides):
                        return True
                    sides[i] -= matchsticks[index]
                else:
                    continue
            return False
        return helper(0, sides)

            