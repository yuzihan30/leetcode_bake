'''
Author: your name
Date: 2022-04-25 15:54:24
LastEditTime: 2022-04-25 15:54:36
LastEditors: your name
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /leetcode_bake/py/array/43_multiply.py
'''
class Solution:
    """
    43. 字符串相乘
    给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。
    """
    def multiply(self, num1: str, num2: str) -> str:
        # 思路：将两数的每一位从字符串转为整数，num1和num2倒着遍历，i位和j位相乘结果先不进位，
        # 放到结果数组的i+j+1位（找规律），后面统一处理进位问题；
        # 而且两数相乘的结果长度要么是num1 + num2位，要么是num1 + num2 - 1位
        # 1. 初始化及特殊处理
        if num1 == '0' or num2 == '0':
            return '0'
        n1 = len(num1)
        n2 = len(num2) 
        # ans_arr = [0] * (n1 * n2)
        # 易错点
        ans_arr = [0] * (n1 + n2)
        # ans = [0] * (n1 * n2)

        # 2. 处理两数每位的乘积结果
        for j in reversed(range(n2)):
            y = int(num2[j])
            for i in reversed(range(n1)):
                # 关键点：找规律j+j+1 
                # 易错点：注意是累加，因为i+j+1相同的次数比较多
               ans_arr[i+j+1] += y * int(num1[i])

        # 3. 遍历ans_arr处理进位
        # for k in reversed(range(n1 * n2)):
        for k in reversed(range(1, n1 + n2)):
            # if k == n1 * n2 - 1:
            #     ans_arr[k-1] += ans_arr[k] // 10
            #     ans_arr[k] = ans_arr[k] % 10
            ans_arr[k-1] += ans_arr[k] // 10
            ans_arr[k] %= 10
        
        # 4. 处理并返回结果值
        # ans_arr[0] == 0 ? ans_arr.del(ans_arr[0]) : None
        # ans_arr.del(ans_arr[0]) if ans_arr[0] == 0 else None
        # del(ans_arr[0]) if ans_arr[0] == 0 else None
        if ans_arr[0] == 0:
            del(ans_arr[0])
        # return ans_arr.join('')
        return ''.join([str(item) for item in ans_arr])
