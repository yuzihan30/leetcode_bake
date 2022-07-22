class Solution:
    """
    63. 不同路径 II
    一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。
现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
网格中的障碍物和空位置分别用 1 和 0 来表示。
    """
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 思路：和62题相似，使用动态规划思想，求状态转移方程；特殊点在于存在障碍时f[i][j]为0
        # 1. 初始化及特殊处理
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # 易错点：注意m、n关系
        # 初始化的同时已将有障碍的地方置为0， 后续只需处理无障碍的地方
        f = [[0]*n for _ in range(m)]

        # 2. 遍历求状态转移方程
        for i in range(m):
            for j in range(n):
                # 存在障碍时跳过
                if obstacleGrid[i][j] == 1: continue
                # 行索引和列索引都为零时
                if not i and not j:
                    f[i][j] = 1
                # 行索引不为0，列索引为0 
                elif i and not j:
                    f[i][j] = f[i-1][j]
                # 行索引为0，列索引不为0 
                elif not i and j:
                    f[i][j] = f[i][j-1]
                # 行索引不为0，列索引也不为0 
                else:
                    f[i][j] = f[i-1][j] + f[i][j-1]

        # 3. 返回结果值
        return f[m-1][n-1]
