'''
Author: your name
Date: 2022-04-25 17:24:06
LastEditTime: 2022-04-25 17:24:21
LastEditors: your name
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /leetcode_bake/py/array/44_isMatch.py
'''
class Solution:
    """
    44. 通配符匹配
    给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
    '?' 可以匹配任何单个字符。
    '*' 可以匹配任意字符串（包括空字符串）。
    两个字符串完全匹配才算匹配成功。
    说明:
    s 可能为空，且只包含从 a-z 的小写字母。
    p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *
    """
    def isMatch(self, s: str, p: str) -> bool:
        # 思路：可以使用深度搜索，也可以使用动态规划，这里使用最优解双指针法
        # 1. 初始化及特殊处理
        sp = 0
        pp = 0
        s_len = len(s)
        p_len = len(p)
        match = 0
        star_p = -1

        # 2. 遍历s串
        while sp < s_len:
            # 分支内需要考虑双指针sp、pp的移动情况
            if pp < p_len and (s[sp] == p[pp] or p[pp] == '?'):
                sp += 1
                pp += 1
            # 这种情况下，sp并未右移，下次循环继续处理sp的情况
            # 此时sp并不能移动，因为可能p的下一个值就匹配上这个s[sp]的值
            elif pp < p_len and p[pp] == '*':
                star_p = pp
                match = sp
                pp += 1
            # 核心处理逻辑
            elif star_p != -1:
                match += 1
                # sp += 1
                # 易错点：注意sp指针此时要跟着match走
                sp = match
                pp = star_p + 1
            else:
                return False
        
        # 3. 遍历完s串，处理还有未处理p串的情况
        # while pp < p_len:
        #     if p[pp] == '*':
        #         pp += 1
        # 易错点：注意while循环的写法
        while pp < p_len and p[pp] == '*':
            pp += 1
        
        # 4. 返回结果
        # 易错点：注意不是pp == p_len - 1 
        return pp == p_len
