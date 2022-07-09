class Solution:
    """
    54. 螺旋矩阵
    给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 思路：顺时针，上右下左依次遍历边界，并向内移动边界，当上边界低于下边界，
        # 或者右边界小于左边界，终止遍历
        # 1. 初始化及特殊处理
        row, col = len(matrix), len(matrix[0])
        l,r,t,d = 0, col-1, 0, row-1
        res = []

        # 2. 遍历处理，关键点，外层是while循环比较特殊，终止条件为True，靠内部break中断
        while True:
            for i in range(l, r+1):
                res.append(matrix[t][i])
            t = t + 1
            if t > d: break

            for i in range(t, d+1):
                res.append(matrix[i][r])
            r = r - 1 
            if r < l: break

            for i in range(r, l-1, -1):
                res.append(matrix[d][i])
            d = d - 1
            if d < t: break

            for i in range(d, t-1, -1):
                res.append(matrix[i][l])
            l = l + 1
            if l > r: break

        # 3. 返回结果
        return res