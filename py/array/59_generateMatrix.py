class Solution:
    """
    59. 螺旋矩阵 II
    给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
    """
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 思路：参考54题，54题是依次取出，59题是依次放入；关键依然是双层遍历
        # 1. 初始化及特殊处理
        if n == 1:
            return [[1]]
        # 关键点：初始化填充的第一个数
        num = 1
        # res = [[0] * n] * n
        res = [[0] * n for i in range(n)]
        count = 0 # 记录已存数据在helper_list中的索引
        l, r, t, d = 0, n-1, 0, n-1

        # 2. 双层遍历
        while True:
            for i in range(l, r + 1):
                res[t][i] = num
                num = num + 1
            t = t + 1
            if t > d: break

            for i in range(t, d + 1):
                res[i][r] = num
                num = num + 1
            r = r - 1
            if r < l: break

            for i in range(r, l - 1, -1):
                res[d][i] = num
                num = num + 1
            d = d - 1
            if d < t: break

            for i in range(d, t-1, -1):
                res[i][l] = num
                num = num + 1
            l = l + 1
            if l > r: break

        # 3. 返回结果值
        return res