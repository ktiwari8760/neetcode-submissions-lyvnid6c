class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for _ in range(len(temperatures))]
        stack = []

        for i, ele in enumerate(temperatures):
            print(stack)
            while stack and stack[-1][0] < ele:
                temp, index = stack.pop()
                answer[index] = i - index

            stack.append((ele, i))

        return answer
