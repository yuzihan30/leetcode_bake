from typing import List
class Solution:
    """
    48. 旋转图像
    给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。
你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 思路： 找规律，先主对角线反转，再左右反转即可得到结果
        # 1. 初始化及特殊处理
        n = len(matrix)
        if n <= 1:
            return

        # 2. 两次反转
        # 主对角线反转
        for i in range(n):
            for j in range(i):
                matrix[i][j],  matrix[j][i] = matrix[j][i],  matrix[i][j]

        # 左右反转
        for i in range(n):
            for j in range(n // 2):
                # 左右对称的两列索引之和为n-1
                # matrix[i][j],  matrix[i][n-1-j] = matrix[n-1-j][i],  matrix[i][j]
                matrix[i][j],  matrix[i][n-1-j] = matrix[i][n-1-j],  matrix[i][j]