class Solution:
    """
    37. 解数独
    编写一个程序，通过填充空格来解决数独问题。
    数独的解法需 遵循如下规则：
    数字 1-9 在每一行只能出现一次。
    数字 1-9 在每一列只能出现一次。
    数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
    数独部分空格内已填入了数字，空白格用 '.' 表示。
    """
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # 思路：回溯法，先保存每行、每列、每个九宫格已出现的数，然后遍历每个小格子，遍历过程中会用到回溯，参考视频：
        # https://www.bilibili.com/video/BV1j54y1z7iZ?spm_id_from=333.337.search-card.all.click
        # 1. 初始化及特殊处理
        # 1.1 row_dict用于记录每行出现过哪些数
        row_dict = [set() for _ in range(9)]
        # 1.2 col_dict用于记录每列出现过哪些数
        col_dict = [set() for _ in range(9)]
        # 1.3 square_dict用于记录每个九宫格子中出现的数字
        square_dict = [set() for _ in range(9)]
        # 1.4 遍历每个小格子，存储每行每列以及每个九宫格出现的数字
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    row_dict[i].add(num)
                    col_dict[j].add(num)
                    # i // 3 * 3 + j // 3计算出第几个九宫大格子
                    square_dict[i // 3 * 3 + j // 3].add(num)
        flag = False  # 标记是否已完成数独填写
        
        # 2. 定义回溯方法，定义为嵌套函数是因为需要和外部方法共享一些变量
        def back_track(row: int, col: int) -> bool:
            nonlocal flag
            square_index = row // 3 * 3 + col // 3
            if board[row][col] == '.':
                for i in range(1, 10):
                    # if i not in row_dict and i not in col_dict and i not in square_dict:
                    if i not in row_dict[row] and i not in col_dict[col] and i not in square_dict[square_index]:
                        board[row][col] = str(i)
                        row_dict[row].add(i)
                        col_dict[col].add(i)
                        square_dict[square_index].add(i)
                        if col == 8 and row == 8:
                            flag = True
                            return 
                        if col < 8:
                            back_track(row, col + 1)
                        else:
                            back_track(row + 1, 0)
                        # 如果后面的节点没找到合适的数填写，就回溯到上一个节点
                        # 递归返回有两种结果，一种已经解决数独，另一种需要当前节点换另一个数试
                        if flag:  # 关键点
                            return 
                        # 当前节点所有可以用的数试完了都不行的话，需要将该节点复原
                        # 这个主要保证最后一个能用的数无效之后，恢复当前节点，回溯上一节点
                        board[row][col] = '.'  
                        row_dict[row].remove(i)
                        col_dict[col].remove(i)
                        square_dict[square_index].remove(i)
            else:
                if col == 8 and row == 8:
                    flag = True
                    return 
                if col < 8:
                    back_track(row, col + 1)
                else:
                    back_track(row + 1, 0)
                # 下个节点递归返回的时候，无论有没有解决数独都会执行完，因不需要复原节点，所以也不需要提前返回
                # if flag:
                #     return
        # 3. 调用回溯方法
        back_track(0, 0)