class Solution:
    """
    1137. 第 N 个泰波那契数
泰波那契序列 Tn 定义如下： 
T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
给你整数 n，请返回第 n 个泰波那契数 Tn 的值。
    """
    def tribonacci(self, n: int) -> int:
        # 思路：同70题爬楼梯
        # f[0] = 0, f[1] = 1, f[2] = 1, f(n) = f(n-1) + f(n-2) + f(n-3)
        # 利用动态规划思想，将递推转化为迭代，缓存中间结果值
        # 1. 初始化及特殊处理
        if n == 0: return 0
        if n == 1: return 1
        if n == 2: return 1
        f0 = 0
        f1 = 1
        f2 = 1

        # 2. 遍历 n-3+1 = n-2次
        for _ in range(n-2):
            f3 = f2 + f1 + f0
            f0 = f1
            f1 = f2
            f2 = f3

        # 3. 返回结果值
        return f3