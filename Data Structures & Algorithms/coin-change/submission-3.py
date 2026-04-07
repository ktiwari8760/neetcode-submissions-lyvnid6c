class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = float('inf')
        coins.sort(reverse = True)
        def function(start , coin , total):
            nonlocal min_coins
            if total == amount:
                min_coins = min(min_coins , coin )
                return
            if coin >= min_coins:
                return
            if total > amount:
                return
            for i in range(start , len(coins)):
                function(i , coin+1 ,  total + coins[i])
        function(0 , 0 , 0)
        return min_coins if min_coins != float('inf') else -1