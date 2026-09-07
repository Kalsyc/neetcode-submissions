class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Upper bound is max(piles) ceil(x/k) -> k
        # [1, 4, 3, 2]
        left = 1
        right = max(piles)
        res = right
        while left <= right:
            k = (left + right) // 2
            time_taken = 0
            for p in piles:
                time_taken += math.ceil(float(p) / k)
            if time_taken <= h:
                res = k
                right = k - 1
            else:
                left = k + 1
        return res