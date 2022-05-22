'''
Author: yuzihan yuzihanyuzihan@163.com
Date: 2022-05-22 18:14:42
LastEditors: yuzihan yuzihanyuzihan@163.com
LastEditTime: 2022-05-22 18:14:51
FilePath: /leetcode_bake/py/array/50_myPow.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
class Solution:
    """
    50. Pow(x, n)
    实现 pow(x, n) ，即计算 x 的 n 次幂函数（即，xn ）。
    """
    def myPow(self, x: float, n: int) -> float:
        # 思路：分治思想做递归
        # 1. 初始化及特殊处理
        # if n == 0:
        if n == 0 or x == 1:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        # 2. 递归处理并返回结果
        # if n % 2 == 1:
        #     half = self.myPow(x, n // 2)
        #     return half * half * x
        # else:
        #     half = self.myPow(x, n // 2)
        #     return half * half 
        half = self.myPow(x, n // 2)
        return half * half * x if n % 2 == 1 else  half * half