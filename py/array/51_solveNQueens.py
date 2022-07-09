class Solution:
    """
    51. N 皇后
    按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        # 思路：回溯法，关键点1，抽象成a[x] = y; 检查（x,y）的主对角线、辅对角线、
        # 列是否已存在皇后，因为行是从前往后遍历，所以前面的行已经存在皇后，
        # 主对角线i+a[i] = x + y, 辅对角线i - a[i] = x - y
        # 1. 初始化及特殊处理
        if n == 1:
            return [["Q"]]
        # 抽象a_list[x] = y表示 x行y列放的是皇后
        # a_list = [-1 for i in range(n)]
        a_list = [-1] * n
        # right_arr存放每一种结果的二维数组
        right_arr = [['.' for i in range(n)] for j in range(n)]
        # right_arr = [['.'] * n] * n
        # res存放最终结果
        res = []

        # 2. 定义校验坐标点（x, y）处能否放置皇后
        def check(x: int, y: int) -> bool:
            # nonlocal a_list
            for i in range(x):
                # 当前列已经存在皇后
                if a_list[i] == y: return False
                # 经过（x,y）的主对角线的右上部分存在皇后
                if x + y == i + a_list[i]: return False
                # 经过（x,y）的辅对角线的左上部分存在皇后
                if x - y == i - a_list[i]: return False
            return True

        # 3. 定义回溯方法, 如果需要共享当前外层函数内的变量，则需要定义为内层函数
        def back_track(row: int) -> None:
            # nonlocal right_arr
            # nonlocal res
            # 终止条件
            if row == n:
                res.append([''.join(right_arr[i]) for i in range(n)])
                # 回溯过程中已重置right_arr中的值，这里不必重置
                # right_arr = [['.' for i in range(n)] for j in range(n)]
                return 
            # 第row行遍历某列的时候，则第row行还没有放皇后，该行已满足没放皇后的条件，
            # 需要满足该列以前没放皇后；同时需要满足主对角线即该坐标点右上方没有皇后；
            # 以及该坐标辅对角线，即左上方没有皇后
            for j in range(n):
                if check(row, j):
                    a_list[row] = j
                    right_arr[row][j] = 'Q'
                    back_track(row+1)
                    # 回溯后需要将值清除或者恢复
                    a_list[row] = -1 
                    right_arr[row][j] = '.'
        
        # 4. 回溯
        back_track(0)

        # 5. 返回结果值
        return res