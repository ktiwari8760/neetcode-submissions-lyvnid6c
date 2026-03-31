class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def time(position , speed):
            distance = target - position
            return distance/speed
        dict1 = {}
        for i in range(len(position)):
            dict1[position[i]] = speed[i]
        print(dict1)
        stack = []
        position = sorted(position)
        for i in range(len(position)-1 , -1 , -1):
            if stack and time(stack[-1] , dict1[stack[-1]]) >= time(position[i] , dict1[position[i]]):
                car1 = stack.pop()
                if dict1[car1] < dict1[position[i]]:
                    stack.append(car1)
                else:
                    stack.append(position[i])
            elif stack and time(stack[-1] , dict1[stack[-1]]) < time(position[i] , dict1[position[i]]):
                stack.append(position[i])
            else:
                stack.append(position[i])
        return len(stack)