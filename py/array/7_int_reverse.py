class Solution:
    """
    7. 整数反转
    给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
    如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
    假设环境不允许存储 64 位整数（有符号或无符号）。
    """
    def reverse(self, x: int) -> int:
        # 方法：字符串法
        # 关键点：切片步长为负数时，按照指定步长反向切片，[::-1]值默认从尾部到头部
        # 1. 将整数转为字符串做反转处理，处理完后转换会整数. 
        # 字符串转回数字时高位0会自动删除掉
        strx = str(x)
        x = int('-' + strx[1:][::-1]) if x < 0 else int(strx[::-1])
        # 2. 特殊情况处理, 易错点：是反转后的整数越界而非反转前的整数越界
        return 0 if x < -2**31 or x > 2**31-1 else x


class Solution:
    def reverse(self, x: int) -> int:
        # 方法：除数余数法
        # 1. 初始化
        flag = -1 if x < 0 else 1 # 关键点：1非负-1负
        x = abs(x)
        res = 0
        # 2. 数学逻辑处理
        while x:
            res = res*10 + x%10
            x //= 10
        res = flag * res
        return 0 if res < -2**31 or res > 2**31 - 1  else res