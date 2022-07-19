class Solution:
    """
    60. 排列序列
    给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。
按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。
    """
    def getPermutation(self, n: int, k: int) -> str:
        # 思路：确定第一位后，后面就有n-1的阶乘种情况，通过循环求商和余数，得到第k个排列的每一位
        # 1. 初始化及特殊处理
        from math import factorial
        seq = [str(i) for i in range(1, n+1)]
        # 第k个序列对应索引为k-1
        n, k = len(seq), k-1
        ans = ''

        # 2. 循环处理
        while n > 0:
            # divmod返回商和余数组成的元组
            idx, k = divmod(k, factorial(n-1))
            # 依次取出当前位的字符数字
            ans += seq.pop(idx)
            n -= 1
        
        # 3. 返回结果值
        return ans


