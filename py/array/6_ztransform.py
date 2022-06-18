"""
6. Z 字形变换
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 思路：将问题抽象成数学模型，将字符串按横向的Z字形放到字符串列表里。
        # 找规律，字符串的索引与对应放置位置的行索引的和是以2*numRows - 2为周期，
        # 同时能发现每放置2*numRows - 2个数，就是一个重复周期。

        # 1. 初始化
        size = len(s)
        str_list = ['' for _ in range(size)]
        T = 2*numRows - 2
        # 2. 特殊处理情况 (numRows < 2包含0和1两种)
        
        if size < 2 or numRows < 2:
            return s

        # 3. 遍历字符串
        for i in range(size):
            j = i % T # 易错点：T可能为0的情况
            if j < numRows:
               str_list[j] += s[i]
            else:
                str_list[T - j] += s[i]
        
        # 4. 将列表中字符串元素拼接返回 易错点：注意与其他语言中数组转字符串的区别
        # return str_list.join('')
        return ''.join(str_list)

