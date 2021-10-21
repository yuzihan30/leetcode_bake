class Solution:
    """
    8. 字符串转换整数 (atoi)
    请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。
    """
    def myAtoi(self, s: str) -> int:
        # 1. 清空左侧空格
        s = s.lstrip()
        # 2. 处理特殊情况 易错点：py中逻辑非运算符不是"!"
        if len(s) == 0 or (not s[0].isdigit() and s[0] not in ['+', '-']):
            return 0
        
        # 3. 循环处理后续字符
        res, i = s[0], 1
        while i < len(s) and s[i].isdigit():
            res += s[i]
            i += 1
        
        try:
            # 易错点：res不能写成s
            int_s = int(res) # 如果报错会走except处理
            return min(max(int_s, -2**31), 2**31 - 1)
        except: 
            return 0

        
