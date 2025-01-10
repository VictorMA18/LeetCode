from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        memo = {}
        
        def dp(i: int, bought: bool) -> int:
            if i >= n:
                return 0
                
            if (i, bought) in memo:
                return memo[(i, bought)]
            
            sig = dp(i + 1, bought)
            
            if not bought:
                c = dp(i + 1, True) - prices[i]
                memo[(i, bought)] = max(sig, c)
            else:
                v = prices[i]
                memo[(i, bought)] = max(sig, v)
            
            return memo[(i, bought)]
            
        return dp(0, False)
    
