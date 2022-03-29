'''
Author: your name
Date: 2022-03-29 19:54:31
LastEditTime: 2022-03-29 19:54:51
LastEditors: your name
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /leetcode_bake/py/array/36_isValidSudoku.py
'''
class Solution:
    """
    36. 有效的数独
    请你判断一个 9 x 9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。
数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
注意：
一个有效的数独（部分已被填充）不一定是可解的。
只需要根据以上规则，验证已经填入的数字是否有效即可。
空白格用 '.' 表示。
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 思路：三次遍历，第一次双层循环遍历每行，第二次双层循环遍历每列，
        # 第三次四层循环，外层双循环遍历9个盒子（三行三列），内层双循环遍历没个小盒子（三行三列）
        # 1. 初始化及特殊处理
        # 题目要求输入就是9行9列字符串，这里可以不用边界处理
        if len(board) != 9:
            return False
        
        # 2. 遍历
        # 2.1 遍历行
        for i in range(9):
            # 遍历每行都要重置numSet
            numSet = set()
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in numSet:
                    numSet.add(board[i][j])
                else:
                    return False
        # 2.2 遍历列
        for j in range(9):
            # 遍历每列都要重置numSet
            numSet = set()
            for i in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in numSet:
                    numSet.add(board[i][j])
                else:
                    return False   
        # 2.3 遍历九宫格的小盒子
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                # 遍历每个小盒子都要重置numSet
                numSet = set() 
                for x in range(3):
                    for y in range(3):
                        if board[i+x][j+y] == '.':
                            continue
                        if board[i+x][j+y] not in numSet:
                            numSet.add(board[i+x][j+y])
                        else:
                            return False 

        # 3. 返回结果值
        return True