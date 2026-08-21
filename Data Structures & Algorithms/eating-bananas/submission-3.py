import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_max = max(piles)
        k_min = 1
        k_best = k_max

        while k_min <= k_max:
            hours_needed = 0
            k_m = (k_max+k_min) // 2
            for pile in piles:
                hours_needed += math.ceil(pile/k_m)
            if hours_needed <= h:
                k_best = k_m
                k_max = k_m-1
            else:
                k_min = k_m+1
        
        return k_best


