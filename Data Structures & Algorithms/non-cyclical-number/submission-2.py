class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def square_of_number(n):
            answer = 0
            while n:
                answer += (n%10) ** 2
                n = n //10
            return answer
        
        while True:
            print(n)
            if n == 1:
                return True
            if n in seen:
                return False
            seen.add(n)
            n = square_of_number(n)
