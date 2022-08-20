class Solution:
    """
    67. 二进制求和
    给你两个二进制字符串，返回它们的和（用二进制表示）。输入为 非空 字符串且只包含数字 1 和 0。
    """
    def addBinary(self, a: str, b: str) -> str:
        # 思路：两个指针分别从低位到高位遍历a和b,每次遍历需要将结果和进位模2进行拼接，
        # 进位除以2进入下一次循环
        # 1. 初始化
        ans = ''
        i, j = len(a)-1, len(b)-1
        carry = 0

        # 2. while循环遍历
        while i >= 0 or j >= 0 or carry > 0:
            if i >= 0: 
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            # ans += str(carry % 2) 易错点：拼接顺序不能反了
            ans = str(carry % 2) + ans
            carry //= 2

        # 3. 返回结果值
        return ans