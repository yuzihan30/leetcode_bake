class Solution:
    def mySqrt(self, x: int) -> int:
        l, mid, r = 0, 0, x
        ans = 0
        while l <= r:
            mid = (l+r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else: 
                r = mid - 1

        return ans
