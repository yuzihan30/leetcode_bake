class Solution:
    """
    28. 实现 strStr()
    实现 strStr() 函数。
    给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出needle字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回-1 。
    """
    def strStr(self, haystack: str, needle: str) -> int:
        # 思路：直接上KMP算法，参考左神视频
        # https://www.bilibili.com/video/BV1xP4y1h7Ga?spm_id_from=333.999.0.0
        # 1. 初始化及特殊处理
        if not needle:
            return 0
        n, m = len(haystack), len(needle)
        if n < m:
            return -1
        i, j = 0, 0
        
        # 2. 求匹配串的next数组, next数组决定下次j移动的位置
        next = self.getNext(needle)

        # 3. 遍历
        while i < n and j < m:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            elif next[j] == -1: # next[j] == -1的位置其实就是j=0的位置
                i += 1
            else:
                j = next[j]

        # 4. 计算返回值
        return i - m if j == m else -1 

    def getNext(self, needle: str) -> List:
        # 1. 初始化及特殊处理
        if not needle:
            return []
        m = len(needle)
        if m < 2:
            return [-1]
        # next = [-1, 0]
        # next[0] = -1
        # next[1] = 0
        next = [0 for _ in range(m)]
        next[0] = -1
        next[1] = 0
        i = 2
        # cn = next[i-1]
        cn = 0 # 记录next[i+1]的回找的位置， 初始值是i为2回找的0

        # 2. 遍历求值
        while i < m:
            if needle[i-1] == needle[cn]:
                next[i] = cn + 1 # cn其实就是next[i-1]
                i += 1 # 向右移动时，对于next[i+1]需要比较next[i] 和cn + 1处的值，也就需要cn自增，
                # 从上一句也能看出来， 新的next[i]就是cn + 1
                cn += 1 
            elif cn > 0:
                cn = next[cn]
            else:
                next[i] = 0
                i += 1
        
        # 3. 返回next数组
        return next