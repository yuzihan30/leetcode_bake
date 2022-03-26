'''
Author: your name
Date: 2022-03-26 12:23:54
LastEditTime: 2022-03-26 12:24:51
LastEditors: your name
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /leetcode_bake/py/array/29_divid.py
'''
class Solution:
    """
    29. 两数相除
    给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
    """
    def divide(self, dividend: int, divisor: int) -> int:
        # 思路：除数向左移位运算不断找比被除数小的最大数，设置辅助变量track记录每次移位除数变大的倍数
        # 参考视频：https://www.bilibili.com/video/BV1SQ4y1K7z5?spm_id_from=333.337.search-card.all.click
        # 1. 初始化及特殊处理
        # 记录最大的边界值，32位有符号数的范围[-2^31, 2^31 - 1]
        limit = 2 ** 31  
        if divisor == 0:
            raise Exception("两数相除，除数不能为0")
        if dividend == 0 and divisor != 0:
            return 0
        # 记录结果符号，True代表正数，False代表负数
        # isNeg = (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)
        isNeg = (divisor < 0) != (dividend < 0)  # 优化判断结果为负的方法
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        div, track = divisor, 1

        # 2. while循环处理
        while dividend >= divisor:
            while dividend >= (div << 1):
                # 易错点
                # div << 1
                # track << 1
                div <<= 1
                track <<= 1
            res += track  # 记录当前拆解的最大块的结果值
            # 记录剩余的dividend
            dividend -= div
            # 恢复div, track
            div, track = divisor, 1

        # 3. 返回值, 负数不存在溢出的情况，只需要考虑正数溢出的情况
        # 易错点
        # return min(limit, -res if isNeg else res)
        return min(limit-1, -res if isNeg else res)