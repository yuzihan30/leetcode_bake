class Solution:
    """
    有效数字（按顺序）可以分成以下几个部分：
        1.一个 小数 或者 整数
        2.（可选）一个 'e' 或 'E' ，后面跟着一个 整数
    小数（按顺序）可以分成以下几个部分：
        1.（可选）一个符号字符（'+' 或 '-'）
        2. 下述格式之一：
            至少一位数字，后面跟着一个点 '.'
            至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
            一个点 '.' ，后面跟着至少一位数字
    整数（按顺序）可以分成以下几个部分：
        1.（可选）一个符号字符（'+' 或 '-'）
        2. 至少一位数字
部分有效数字列举如下：["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
部分无效数字列举如下：["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。
    """
    def isNumber(self, s: str) -> bool:
        # 思路：根据题意得出有效数字的公式为 整数/小数[e/E 整数]; 小数和整数的必要条件是至少一位数字，
        # 可选条件是符号位，二者区别是小数必须有小数点; 关键是区分是否有e/E两种情况处理，
        # 无e/E的时候需要判断是否是小数或者整数，有e/E的时候判断e/E前是整数或者小数，e/E后面是整数
        # 1. 初始化及特殊处理
        n = len(s)
        e_idx = -1

        # 2. 判断是否有e/E，多于一个e/E直接返回false
        for i in range(n):
            if s[i] == 'e' or s[i] == 'E':
                # 多于一个e/E的情况
                if e_idx != -1:
                    return False
                else:
                    e_idx = i
        # 3. 无e/E时，必须是整数或者小数
        if e_idx == -1:
            return self.check(s, 0, n, False)
        
        # 4. 有e/E时，e/E之前需要是整数或者小数，e/E之后必须是整数
        return self.check(s, 0, e_idx, False) and self.check(s, e_idx+1, n, True)

    # 判断是整数或者是小数，must_int为True时只判断是整数
    def check(self, s: str, start: int, end: int, must_int: bool) -> bool:
        # 特殊处理, 易错点：因为左开右闭[start, end)，所以start要小于end，否则越界
        if start >= end: return False
        # 处理符号位
        if s[start] == '+' or s[start] == '-': start += 1
        # 判断是否是小数点，是否是数字
        point, digit = False, False
        # 遍历处理
        for i in range(start, end):
            # 是否有小数点区分整数或者小数
            if s[i] == '.':
                if must_int: return False
                #  有>1个小数点
                elif point: return False
                else: point = True
            # 是数字
            elif s[i].isdigit():
                digit = True
            # 既不是数字也不是小数点
            else:
                return False
        # 易错点：至少有一位数字，因此最后要根据digit来判断是否为整数或者小数
        # return True        
        return digit      

