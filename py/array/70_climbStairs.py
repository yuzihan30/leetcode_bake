class Solution:
    """
    70. 爬楼梯
    假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
    """
    def climbStairs(self, n: int) -> int:
        # 和斐波那契数列类似，f1 = 1, f2 = 2, f3 = 3, 
        # 状态转义方程为f(n) = f(n-1) + f(n-2); 到达第n个台阶有两种方式，
        # 要么从第n-1台阶到达，要么从n-2台阶到达
        # 利用动态规划思想，将递推转化为迭代，缓存中间结果值
        # 1. 初始化及特殊处理
        if n == 1: return 1
        if n == 2: return 2
        f1 = 1
        f2 = 2

        # 2. 遍历 n-3+1 = n-2次
        for _ in range(n-2):
            f3 = f2 + f1
            f1 = f2
            f2 = f3

        # 3. 返回结果值
        return f3

        # 方法2：空间换时间
        # if n == 1: return 1
        # if n == 2: return 2
        # fn = [1] * n
        # fn[0] = 1
        # fn[1] = 2 
        # for i in range(2, n):
        #     fn[i] = fn[i-1] + fn[i-2] 
        
        # return fn[n-1]

        # 方法3：直接用递归会超时
        # if n == 1: return 1
        # if n == 2: return 2
        # return self.climbStairs(n-1) + self.climbStairs(n-2)