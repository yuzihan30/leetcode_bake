'''
Author: your name
Date: 2022-04-05 11:24:43
LastEditTime: 2022-04-05 11:25:02
LastEditors: your name
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /leetcode_bake/py/array/38_countAndSay.py
'''
class Solution:
    """
    38. 外观数列
    给定一个正整数 n ，输出外观数列的第 n 项。
    「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。
    你可以将其视作是由递归公式定义的数字字符串序列：
    countAndSay(1) = "1"
    countAndSay(n) 是对 countAndSay(n-1) 的描述，然后转换成另一个数字字符串。
    """
    def countAndSay(self, n: int) -> str:
        # 思路： 递推法，求f(n), 需要知道f(n-1)
        # 1. 初始化及特殊处理
        if n == 1: return '1'
        if n == 2: return '11'
        # 每次f(n)的结果，形式是将数字个数和对应数字追加到数组的末尾
        # 转化成数组的形式方便递推处理
        res = [1, 1] 
        # res = ['1', '11']

        # 2. 递推遍历， cur对应当前分组的数字，num对应当前分组数字的个数
        for i in range(3, n+1):
            # 每次遍历做初始化
            new_res = []
            num = 1 # 记录f(n-1)当前数的个数
            # 关键点：记录当前f(n-1)每个分组数字对应的个数，初始化为f(n-1)当前的第一个数
            cur = res[0] 
            # 遍历f(n-1)第一个数后的每个数， 只能追加到最后一组数的前一组数的统计结果
            for value in res[1:]:
                if value == cur:
                    num += 1
                else:
                    new_res.append(num)
                    new_res.append(cur)
                    cur = value
                    num = 1
            # 追加最后一个组数的统计结果
            new_res.append(num)
            new_res.append(cur)
            res = new_res  # 易错点：记得每次更新res

        # 3. 处理并返回结果值
        return ''.join(list(map(str, res)))

            

