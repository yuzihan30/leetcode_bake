class Solution:
    """
    62. 不同路径
    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？
    """
    def uniquePaths(self, m: int, n: int) -> int:
        # 思路：动态规划，状态转移方程为f(i, j) = f(i-1, j) + f(i, j-1)
        # 第一行和第一列的值均为1
        # 1. 初始化二维数组保存状态值
        # helper_matrix = [[1]*m for _ in range(n)] # 易错点
        helper_matrix = [[1]*n for _ in range(m)]

        # 2. 双层遍历
        for i in range(1, m):
            for j in range(1, n):
                helper_matrix[i][j] = helper_matrix[i-1][j] + helper_matrix[i][j-1]

        # 3. 返回结果值
        return helper_matrix[m-1][n-1]