# -*- coding: utf-8 -*-
"""
作者：yuzihan
日期：2022年02月13日
"""

class Solution:
    """
    13. 罗马数字转整数
    """
    def romanToInt(self, s: str) -> int:
        # 思路：准备字典，遍历罗马字符串，如果遇到前个字目小于后个字母，需要后面字符对应数字减去前面字符对应数字
        # 1. 初始化
        dic = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        num = len(s)
        if not num:
            return 0
        res = dic[s[0]] # 关键点1： 初始化返回值为第一个字母对应数值
        pre = ''
        cur = ''
        # 2. 遍历罗马字符
        # for i in range(1, len(s) + 1): # 易错点：len(s) + 1会导致越界
        for i in range(1, len(s)):
            pre, cur = s[i-1], s[i]
            if dic[pre] < dic[cur]:
                res += dic[cur] - 2 * dic[pre] # 关键点2：减两次前面那个数，因为前面加过一次
            else:
                res += dic[cur]
        return res