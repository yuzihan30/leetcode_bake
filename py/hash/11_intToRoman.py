# -*- coding: utf-8 -*-
"""
作者：yuzihan
日期：2022年02月13日
"""
class Solution:
    """
    12. 整数转罗马数字
    """
    def intToRoman(self, num: int) -> str:
        # 思路：使用贪心算法，关键设置合理的字典。题目中已限制1 <= num <= 3999
        # 1. 设置排好序的字典
        dic = { 'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100,
        'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1 }
        res = '' # 初始化返回值
        count = 0 # 初始化对应位的值
        # 2. 遍历字典，从高位到低位处理整数
        for key, value in dic.items():
            count = num // value
            if count:
                res += count * key
                num %= value
        return res