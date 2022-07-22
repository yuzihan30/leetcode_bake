class Solution:
    """
    64. 最小路径和
    给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。说明：每次只能向下或者向右移动一步
    """
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 思路：动态规划，f[i][j]代表到达[i, j]的最小数字总和
        # f[i][j] = min(f[i-1][j], f[i][j-1]) + grid[i][j]
        # 1. 初始化及特殊处理
        m = len(grid)
        n = len(grid[0])
        f = [[0]*n for _ in range(m)]

        # 2. 遍历
        for i in range(m):
            for j in range(n):
                if not i and not j: f[i][j] = grid[i][j]
                else:
                    if i and not j: f[i][j] = f[i-1][j] + grid[i][j]
                    elif j and not i: f[i][j] = f[i][j-1] + grid[i][j]
                    else: f[i][j] = min(f[i-1][j], f[i][j-1]) + grid[i][j]
        
        # 3. 返回结果值
        return f[m-1][n-1]
