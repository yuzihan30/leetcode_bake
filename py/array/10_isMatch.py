# -*- coding: utf-8 -*-
"""
10.正则表达式匹配
给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。'.' 匹配任意单个字符
    '*' 匹配零个或多个前面的那一个元素。所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 思路：抽象成m+1行，n+1列的二维数组，或者看成dataframe，字符串s前加个空字符作为行头，
        # 正则表达式前加空字符作为列头，典型的动态规划题目，需要对动态转移方程做初始化
        # 1. 初始化：设置二维数组的元素默认False, 并初始化第一行和第一列，因第一行和第一列
        #    处理比较特殊
        m, n = len(s), len(p)
        match = [[False] * (n + 1) for _ in range(m + 1)]  # 第一列的其它值相当于已经初始化为False
        match[0][0] = True  # 初始化第一行第一列的值
        # 初始化第一行的其它值，即j大于等于1的值
        for j in range(1, n + 1):
            # match[0][j]对应的列头为p[j-1]
            if j > 1:  # j大于1和j等于1分别处理
                if p[j - 1] == '*':  # else对应的部分已经默认初始化为false
                    match[0][j] = match[0][j - 2]
            else:
                if p[j - 1] == '*':
                    match[0][j] = True  # 其实j就是1

        # 2. 求第一行、第一列外的其他元素值
        # 第二行、第二列的索引从1开始
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    match[i][j] = match[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if j > 1:  # j等于1时都是False
                        if match[i][j - 2]:
                            match[i][j] = True
                        else:  # 易错点：易忽略 or p[j-2] == '.'
                            if (p[j - 2] == s[i - 1] or p[j - 2] == '.') and match[i - 1][j]:
                                match[i][j] = True

        return match[i][j]


if __name__ == '__main__':
    solution = Solution()
    print(solution.isMatch('abc', 'a*.c'))

